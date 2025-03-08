# `skupper listener status` Command Reference (kubernetes)

```
Display status of all listeners or a specific listener

Usage:
  skupper listener status <name> [flags]

Examples:
skupper listener status backend

Flags:
  -h, --help            help for status
  -o, --output string   print resources to the console instead of submitting them to the Skupper controller. Choices: json, yaml

Global Flags:
  -c, --context string      Set the kubeconfig context
      --kubeconfig string   Path to the kubeconfig file to use
  -n, --namespace string    Set the namespace
  -p, --platform string     Set the platform type to use [kubernetes, podman, docker, linux]
```
