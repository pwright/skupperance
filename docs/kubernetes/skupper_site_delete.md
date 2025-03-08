# `skupper site delete` Command Reference (kubernetes)

```
Delete a site

Usage:
  skupper site delete [flags]

Examples:
skupper site delete my-site
skupper site delete my-site --wait=false
skupper site delete --all

Flags:
      --all                delete all skupper resources associated with site in current namespace
  -h, --help               help for delete
      --timeout duration   raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 1m0s)
      --wait               Wait for deletion to complete before exiting (default true)

Global Flags:
  -c, --context string      Set the kubeconfig context
      --kubeconfig string   Path to the kubeconfig file to use
  -n, --namespace string    Set the namespace
  -p, --platform string     Set the platform type to use [kubernetes, podman, docker, linux]
```
