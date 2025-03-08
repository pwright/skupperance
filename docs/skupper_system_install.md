# `skupper system install` Command Reference

```

Checks the local environment for required resources and configuration.
In some instances, configures the local environment. It starts the Podman/Docker API 
service if it is not already available.

Usage:
  skupper system install [flags]

Flags:
  -h, --help   help for install

Global Flags:
  -c, --context string      Set the kubeconfig context
      --kubeconfig string   Path to the kubeconfig file to use
  -n, --namespace string    Set the namespace
  -p, --platform string     Set the platform type to use [kubernetes, podman, docker, linux]

```
