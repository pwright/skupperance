# `skupper listener create` Command Reference

```
Clients at this site use the listener host and port to establish connections to the remote service.

Usage:
  skupper listener create <name> <port> [flags]

Examples:
skupper listener create database 5432

Flags:
  -h, --help                     help for create
      --host string              The hostname or IP address of the local listener. Clients at this site use the listener host and port to establish connections to the remote service.
  -r, --routing-key string       The identifier used to route traffic from listeners to connectors
      --tls-credentials string   the name of a Kubernetes secret containing the generated or externally-supplied TLS credentials.
      --type string              The listener type. Choices: [tcp]. (default "tcp")
```

🔗 **External Documentation:** [https://skupperproject.github.io/refdog/commands/listener/create.html](https://skupperproject.github.io/refdog/commands/listener/create.html)

