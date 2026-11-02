"""Sync distribution assets only; never builds or publishes native app source."""
import base64
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

REPOSITORY = 'SufuTeam/Renamint'
ROOT = f'https://github.com/{REPOSITORY}'
ALIAS = 'Renamint-arm64.dmg'
MANIFEST = 'download-manifest.json'


def gh(*args, body=None):
    result = subprocess.run(['gh', *args], input=body, text=True, capture_output=True, check=True)
    return result.stdout


def api(path):
    return json.loads(gh('api', f'repos/{REPOSITORY}/{path}'))


def installer(release):
    tag = release.get('tag_name', '')
    match = re.fullmatch(r'v?(\d+\.\d+\.\d+)', tag)
    if not match or release.get('draft') is not False or release.get('prerelease') is not False or not release.get('published_at'):
        raise ValueError('Expected a published stable release')
    name = f'Renamint-{match[1]}-arm64.dmg'
    for asset in release.get('assets', []):
        if asset.get('name') == name and asset.get('state') == 'uploaded' and asset.get('size', 0) > 0 and asset.get('browser_download_url') == f'{ROOT}/releases/download/{tag}/{name}':
            return asset
    raise ValueError('The latest release has no complete Apple silicon installer')


def expected_sha(checksums, filename):
    matches = [match[1].lower() for line in checksums.splitlines()
               if (match := re.fullmatch(r'([a-fA-F0-9]{64})\s+\*?(.+)', line)) and match[2] == filename]
    if len(matches) != 1:
        raise ValueError('Installer must have exactly one SHA256SUMS.txt entry')
    return matches[0]


def sha(path):
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()


def download(tag, name, directory):
    gh('release', 'download', tag, '--repo', REPOSITORY, '--pattern', name, '--dir', str(directory))
    return directory / name


def sync():
    release = api('releases/latest')
    asset = installer(release)
    tag = release['tag_name']
    with tempfile.TemporaryDirectory(prefix='renamint-download-') as temporary:
        directory = Path(temporary)
        checksum_file = download(tag, 'SHA256SUMS.txt', directory)
        expected = expected_sha(checksum_file.read_text(), asset['name'])
        package = download(tag, asset['name'], directory)
        if sha(package) != expected or package.stat().st_size != asset['size']:
            raise ValueError('Published installer does not match its checksum and size')
        if asset.get('digest') and asset['digest'] != f'sha256:{expected}':
            raise ValueError('GitHub installer digest does not match its checksum')

        existing = {item['name']: item for item in release['assets']}
        if ALIAS in existing:
            alias = download(tag, ALIAS, directory)
            if sha(alias) != expected:
                raise ValueError('Existing stable-name installer differs; refusing to overwrite it')
        else:
            alias = package.rename(directory / ALIAS)
            gh('release', 'upload', tag, str(alias), '--repo', REPOSITORY)

        alias_checksum_name = ALIAS + '.sha256'
        checksum_text = f'{expected}  {ALIAS}\n'
        if alias_checksum_name in existing:
            alias_checksum = download(tag, alias_checksum_name, directory)
            if alias_checksum.read_text() != checksum_text:
                raise ValueError('Stable-name checksum differs; refusing to overwrite it')
        else:
            alias_checksum = directory / alias_checksum_name
            alias_checksum.write_text(checksum_text)
            gh('release', 'upload', tag, str(alias_checksum), '--repo', REPOSITORY)

        # Do not let a delayed workflow downgrade metadata after another release.
        current = api('releases/latest')
        if current['id'] != release['id']:
            raise RuntimeError('Latest release changed during synchronization; rerun the workflow')
        verified = next(item for item in current['assets'] if item['name'] == ALIAS)
        if verified['state'] != 'uploaded' or verified['size'] != asset['size'] or verified.get('digest') not in (None, f'sha256:{expected}'):
            raise ValueError('Uploaded stable-name installer did not verify')

        manifest = {
            'schema_version': 1, 'tag_name': tag, 'draft': False, 'prerelease': False,
            'published_at': release['published_at'], 'html_url': release['html_url'],
            'latest_download_url': f'{ROOT}/releases/latest/download/{ALIAS}',
            'sha256': expected,
            'assets': [{key: asset[key] for key in ['name', 'state', 'size', 'browser_download_url']}]
        }
        content = json.dumps(manifest, ensure_ascii=False, indent=2) + '\n'
        # List first so a missing file is distinguished from API/auth failures.
        exists = any(item['name'] == MANIFEST for item in api('contents?ref=main'))
        previous = api(f'contents/{MANIFEST}?ref=main') if exists else None
        if previous and base64.b64decode(previous['content']).decode() == content:
            print(f'{tag}: stable download and website metadata are already current')
            return
        body = {'message': f'Sync website download for {tag}', 'branch': 'main',
                'content': base64.b64encode(content.encode()).decode()}
        if previous:
            body['sha'] = previous['sha']
        gh('api', '--method', 'PUT', f'repos/{REPOSITORY}/contents/{MANIFEST}', '--input', '-', body=json.dumps(body))
        print(f'{tag}: verified {ALIAS} ({expected}) and synchronized website metadata')


if __name__ == '__main__':
    sync()
