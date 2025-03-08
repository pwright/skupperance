# `skupper link generate` Command Reference (kubernetes)

```
Generate a new link resource with the data needed from the target site. The resultant
output needs to be applied in the site in which we want to create the link.

Usage:
  skupper link generate [flags]

Flags:
      --cost string              the configured "expense" of sending traffic over the link. (default "1")
      --generate-credential      generate the necessary credentials to create the link (default true)
  -h, --help                     help for generate
  -o, --output string            print resources to the console instead of submitting them to the Skupper controller. Choices: json, yaml (default "yaml")
      --timeout duration         raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 1m0s)
      --tls-credentials string   the name of a Kubernetes secret containing the generated or externally-supplied TLS credentials.

Global Flags:
  -c, --context string      Set the kubeconfig context
      --kubeconfig string   Path to the kubeconfig file to use
  -n, --namespace string    Set the namespace
  -p, --platform string     Set the platform type to use [kubernetes, podman, docker, linux]
```
