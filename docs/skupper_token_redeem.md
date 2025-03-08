# `skupper token redeem` Command Reference

```
Redeem a token file in order to create a link to a remote site.

Usage:
  skupper token redeem <filename> [flags]

Examples:
skupper token redeem ~/token1.yaml

Flags:
  -h, --help               help for redeem
  -t, --timeout duration   raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 1m0s)

Global Flags:
  -c, --context string      Set the kubeconfig context
      --kubeconfig string   Path to the kubeconfig file to use
  -n, --namespace string    Set the namespace
  -p, --platform string     Set the platform type to use [kubernetes, podman, docker, linux]

```
