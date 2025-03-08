# `skupper connector generate` Command Reference (kubernetes)

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
  -i, --include-not-ready        If true, include server pods that are not in the ready state.
  -o, --output string            print resources to the console instead of submitting them to the Skupper controller. Choices: json, yaml (default "yaml")
  -r, --routing-key string       The identifier used to route traffic from listeners to connectors
  -s, --selector string          A Kubernetes label selector for specifying target server pods.
      --tls-credentials string   the name of a Kubernetes secret containing the generated or externally-supplied TLS credentials.
      --type string              The connector type. Choices: [tcp]. (default "tcp")
  -w, --workload string          A Kubernetes resource name that identifies a workload expressed like resource-type/resource-name. Expected resource types: service, daemonset, deployment, and statefulset.

Global Flags:
  -c, --context string      Set the kubeconfig context
      --kubeconfig string   Path to the kubeconfig file to use
  -n, --namespace string    Set the namespace
  -p, --platform string     Set the platform type to use [kubernetes, podman, docker, linux]
```
