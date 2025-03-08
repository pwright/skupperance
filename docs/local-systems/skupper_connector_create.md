# `skupper connector create` Command Reference

```
Clients at this site use the connector host and port to establish connections to the remote service.

Usage:
  skupper connector create <name> <port> [flags]

Examples:
skupper connector create database 5432
skupper connector create backend 8080 --workload deployment/backend

Flags:
  -h, --help                     help for create
      --host string              The hostname or IP address of the local connector
  -r, --routing-key string       The identifier used to route traffic from listeners to connectors
      --tls-credentials string   the name of a Kubernetes secret containing the generated or externally-supplied TLS credentials.
      --type string              The connector type. Choices: [tcp]. (default "tcp")
```
