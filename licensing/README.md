# License server source

Renamint uses [Keygate 0.1.19](https://github.com/tabloy/keygate/tree/v0.1.19), upstream commit `6e0e7a784bf6dd93cecbb0fff8f82c0b10954078`, under AGPL-3.0 with its original notices and attribution preserved.

[Download the complete corresponding source](keygate-0.1.19-renamint.2-source.tar.gz) for Renamint's license server, version `0.1.19-renamint.2`. [Previous deployment source](keygate-0.1.19-renamint.1-source.tar.gz) remains available.

Our change commits a paid license and its activation email into the same database transaction. Queue insertion failure rolls back license creation so Stripe retries can recover. Duplicate checkout sessions cannot enqueue a second license email. Upstream SMTP delivery, retry handling, templates and attribution remain intact.

Version 2 also records full refunds durably and serializes them with initial license issuance. A refund arriving before the completion notification cannot be forgotten, and a concurrent completion cannot revive a fully refunded purchase. The checkout verification endpoint refuses reversed payments. Partial refunds retain the upstream policy.

The archive includes all upstream tracked source, the modifications, database integration tests, dependency lockfiles and `Dockerfile.renamint`. Build with `docker buildx build --platform linux/amd64 -f Dockerfile.renamint --load -t renamint-keygate:0.1.19-payments2 .`. The runtime base is the exact upstream image identified in that Dockerfile; it supplies the unchanged frontend assets. Their complete build sources and lockfile are included in `web/`.

For the regression tests, use a dedicated PostgreSQL test database and run `TEST_DATABASE_URL=… go test ./internal/store ./internal/payment -run Renamint -count=1`. Version 2 passed 89 focused tests, plus 20 repeated runs of the four refund-order scenarios.

The source archive contains no deployment credentials, database contents, customer data, or proprietary Renamint app source.
