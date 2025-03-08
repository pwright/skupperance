# `skupper connector generate` Command Reference

```
Clients at this site use the connector host and port to establish connections to the remote service.

Usage:
  skupper connector generate <name> <port> [flags]

Examples:
skupper connector generate database 5432
skupper connector generate backend 8080 --workload deployment/backend

Flags:
  -h, --help                     help for generate
      --host string              The hostname or IP address of the local connector
  -o, --output string            print resources to the console instead of submitting them to the Skupper controller. Choices: json, yaml (default "yaml")
  -r, --routing-key string       The identifier used to route traffic from listeners to connectors
      --tls-credentials string   the name of a Kubernetes secret containing the generated or externally-supplied TLS credentials.
      --type string              The connector type. Choices: [tcp]. (default "tcp")
```
