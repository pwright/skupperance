# `skupper system uninstall` Command Reference (kubernetes)

```
Remove local system infrastructure, undoing the configuration changes made by skupper system install, by disabling the Podman/Docker API.

Usage:
  skupper system uninstall [flags]

Flags:
  -f, --force   option to override even with sites present
  -h, --help    help for uninstall

Global Flags:
  -c, --context string      Set the kubeconfig context
      --kubeconfig string   Path to the kubeconfig file to use
  -n, --namespace string    Set the namespace
  -p, --platform string     Set the platform type to use [kubernetes, podman, docker, linux]
```
