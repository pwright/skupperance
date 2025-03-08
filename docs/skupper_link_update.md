# `skupper link update` Command Reference

```
Change link settings

Usage:
  skupper link update <name> [flags]

Flags:
      --cost string              the configured "expense" of sending traffic over the link. (default "1")
  -h, --help                     help for update
      --timeout duration         raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 1m0s)
      --tls-credentials string   the name of a Kubernetes secret containing the generated or externally-supplied TLS credentials.
      --wait string              Wait for the given status before exiting. Choices: configured, ready, none (default "ready")

Global Flags:
  -c, --context string      Set the kubeconfig context
      --kubeconfig string   Path to the kubeconfig file to use
  -n, --namespace string    Set the namespace
  -p, --platform string     Set the platform type to use [kubernetes, podman, docker, linux]

```
