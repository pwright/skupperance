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
  -i, --include-not-ready        If true, include server pods that are not in the ready state.
  -r, --routing-key string       The identifier used to route traffic from listeners to connectors
  -s, --selector string          A Kubernetes label selector for specifying target server pods.
      --timeout duration         raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 1m0s)
      --tls-credentials string   the name of a Kubernetes secret containing the generated or externally-supplied TLS credentials.
      --type string              The connector type. Choices: [tcp]. (default "tcp")
      --wait string              Wait for the given status before exiting. Choices: configured, ready, none (default "configured")
  -w, --workload string          A Kubernetes resource name that identifies a workload expressed like resource-type/resource-name. Expected resource types: service, daemonset, deployment, and statefulset.

Global Flags:
  -c, --context string      Set the kubeconfig context
      --kubeconfig string   Path to the kubeconfig file to use
  -n, --namespace string    Set the namespace
  -p, --platform string     Set the platform type to use [kubernetes, podman, docker, linux]

```
