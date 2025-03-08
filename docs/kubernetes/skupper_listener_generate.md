# `skupper listener generate` Command Reference

```
Clients at this site use the listener host and port to establish connections to the remote service.
	generate a listener to evaluate what will be created with listener create command

Usage:
  skupper listener generate <name> <port> [flags]

Examples:
skupper listener generate database 5432

Flags:
  -h, --help                     help for generate
      --host string              The hostname or IP address of the local listener. Clients at this site use the listener host and port to establish connections to the remote service.
  -o, --output string            print resources to the console instead of submitting them to the Skupper controller. Choices: json, yaml (default "yaml")
  -r, --routing-key string       The identifier used to route traffic from listeners to connectors
  -t, --tls-credentials string   the name of a Kubernetes secret containing the generated or externally-supplied TLS credentials.
      --type string              The listener type. Choices: [tcp]. (default "tcp")
```

🔗 **External Documentation:** [https://skupperproject.github.io/refdog/commands/listener/generate.html](https://skupperproject.github.io/refdog/commands/listener/generate.html)

