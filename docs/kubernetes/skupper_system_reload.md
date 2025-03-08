# `skupper system reload` Command Reference (kubernetes)

```
Forces to overwrite an existing namespace based on input/resources, if the namespace is not provided, the default one is going to be reloaded

Usage:
  skupper system reload [flags]

Examples:
skupper system reload -n my-namespace

Flags:
  -h, --help   help for reload

Global Flags:
  -c, --context string      Set the kubeconfig context
      --kubeconfig string   Path to the kubeconfig file to use
  -n, --namespace string    Set the namespace
  -p, --platform string     Set the platform type to use [kubernetes, podman, docker, linux]
```
