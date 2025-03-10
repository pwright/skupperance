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
  -i, --include-not-ready        If true, include server pods that are not in the ready state.
      --port int                 The port of the local connector
  -r, --routing-key string       The identifier used to route traffic from listeners to connectors
  -s, --selector string          A Kubernetes label selector for specifying target server pods.
      --timeout duration         raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 1m0s)
      --tls-credentials string   the name of a Kubernetes secret containing the generated or externally-supplied TLS credentials.
      --type string              The connector type. Choices: [tcp]. (default "tcp")
      --wait string              Wait for the given status before exiting. Choices: configured, ready, none (default "configured")
  -w, --workload string          A Kubernetes resource name that identifies a workload expressed like resource-type/resource-name. Expected resource types: service, daemonset, deployment, and statefulset.
```

🔗 **External Documentation:** [https://skupperproject.github.io/refdog/commands/connector/update.html](https://skupperproject.github.io/refdog/commands/connector/update.html)

