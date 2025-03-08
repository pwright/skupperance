# `skupper connector delete` Command Reference (podman)

```
Delete a connector <name>

Usage:
  skupper connector delete <name> [flags]

Examples:
skupper connector delete database

Flags:
  -h, --help               help for delete
  -t, --timeout duration   raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 1m0s)
      --wait               Wait for deletion to complete before exiting (default true)

Global Flags:
  -n, --namespace string   Set the namespace
  -p, --platform string    Set the platform type to use [kubernetes, podman, docker, linux]
```
