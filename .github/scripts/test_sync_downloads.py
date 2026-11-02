import unittest
from sync_downloads import installer, expected_sha


class ReleaseRules(unittest.TestCase):
    def release(self):
        return {'tag_name': 'v1.15.0', 'draft': False, 'prerelease': False,
                'published_at': '2026-11-02T00:00:00Z', 'assets': [
                    {'name': 'Renamint-1.15.0-arm64.dmg', 'state': 'uploaded', 'size': 100,
                     'browser_download_url': 'https://github.com/SufuTeam/Renamint/releases/download/v1.15.0/Renamint-1.15.0-arm64.dmg'}]}

    def test_stable_installer(self):
        self.assertEqual(installer(self.release())['name'], 'Renamint-1.15.0-arm64.dmg')

    def test_reject_nonstable_or_missing_installer(self):
        for values in [{'draft': True}, {'prerelease': True}, {'published_at': None}, {'tag_name': 'v1.15.0-beta'}, {'assets': []}]:
            with self.subTest(values=values), self.assertRaises(ValueError):
                installer({**self.release(), **values})

    def test_reject_wrong_asset_url(self):
        release = self.release()
        release['assets'][0]['browser_download_url'] = 'https://example.com/installer.dmg'
        with self.assertRaises(ValueError):
            installer(release)

    def test_checksum_must_match_exact_filename_once(self):
        digest = 'a' * 64
        self.assertEqual(expected_sha(f'{digest}  app.dmg\n', 'app.dmg'), digest)
        self.assertEqual(expected_sha(f'{digest} *app.dmg\n', 'app.dmg'), digest)
        for text in ['', f'{digest}  old.dmg\n', f'{digest} app.dmg\n{digest} app.dmg\n', 'invalid  app.dmg\n']:
            with self.subTest(text=text), self.assertRaises(ValueError):
                expected_sha(text, 'app.dmg')


if __name__ == '__main__':
    unittest.main()
