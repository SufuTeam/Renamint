# License server source

Renamint uses [Keygate 0.1.19](https://github.com/tabloy/keygate/tree/v0.1.19), upstream commit `6e0e7a784bf6dd93cecbb0fff8f82c0b10954078`, under AGPL-3.0 with its original notices and attribution preserved.

[Download the complete corresponding source](keygate-0.1.19-renamint.1-source.tar.gz) for the Renamint deployment, version `0.1.19-renamint.1`.

Our change commits a paid license and its activation email into the same database transaction. Queue insertion failure rolls back license creation so Stripe retries can recover. Duplicate checkout sessions cannot enqueue a second license email. Upstream SMTP delivery, retry handling, templates and attribution remain intact.

The archive includes all upstream tracked source, the modification, a database integration test, dependency lockfiles and `Dockerfile.renamint`. Build with `docker buildx build --platform linux/amd64 -f Dockerfile.renamint --load -t renamint-keygate:0.1.19-outbox1 .`. The runtime base is the exact upstream image identified in that Dockerfile; it supplies the unchanged frontend assets. Their complete build sources and lockfile are included in `web/`.

For the regression test, use a disposable PostgreSQL test database and run `TEST_DATABASE_URL=… go test ./internal/store -run RenamintPurchaseOutbox -count=1`.

The source archive contains no deployment credentials, database contents, customer data, or proprietary Renamint app source.
