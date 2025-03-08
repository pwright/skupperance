# `skupper version` Command Reference (kubernetes)

```
Report the version of the Skupper components

Usage:
  skupper version [flags]

Examples:
skupper version
skupper version -o yaml > manifest.yaml

Flags:
  -h, --help            help for version
  -o, --output string   print verbose output to the console. Choices: json, yaml

Global Flags:
  -c, --context string      Set the kubeconfig context
      --kubeconfig string   Path to the kubeconfig file to use
  -n, --namespace string    Set the namespace
  -p, --platform string     Set the platform type to use [kubernetes, podman, docker, linux]
```
