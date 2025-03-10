# `skupper listener update` Command Reference

```
Clients at this site use the listener host and port to establish connections to the remote service.
	The user can change port, host name, TLS credentials, listener type and routing key

Usage:
  skupper listener update <name> [flags]

Examples:
skupper listener update database --host mysql --port 3306

Flags:
  -h, --help                     help for update
      --host string              The hostname or IP address of the local listener. Clients at this site use the listener host and port to establish connections to the remote service.
      --port int                 The port of the local listener
  -r, --routing-key string       The identifier used to route traffic from listeners to connectors
  -t, --tls-credentials string   the name of a Kubernetes secret containing the generated or externally-supplied TLS credentials.
      --type string              The listener type. Choices: [tcp]. (default "tcp")
```

🔗 **External Documentation:** [https://skupperproject.github.io/refdog/commands/listener/update.html](https://skupperproject.github.io/refdog/commands/listener/update.html)

