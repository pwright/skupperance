# `skupper connector update` Command Reference

```
Clients at this site use the connector host and port to establish connections to the remote service.
	The user can change port, host name, TLS secret, selector, connector type and routing key

Usage:
  skupper connector update <name> [flags]

Examples:
skupper connector update database --host mysql --port 3306

Flags:
  -h, --help                     help for update
      --host string              The hostname or IP address of the local connector
      --port int                 The port of the local connector
  -r, --routing-key string       The identifier used to route traffic from listeners to connectors
      --tls-credentials string   the name of a Kubernetes secret containing the generated or externally-supplied TLS credentials.
      --type string              The connector type. Choices: [tcp]. (default "tcp")
```

🔗 **External Documentation:** [https://skupperproject.github.io/refdog/commands/connector/update.html](https://skupperproject.github.io/refdog/commands/connector/update.html)

