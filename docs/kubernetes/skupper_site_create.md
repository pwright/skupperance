# `skupper site create` Command Reference (kubernetes)

```
A site is a place where components of your application are running.
Sites are linked to form application networks.
There can be only one site definition per namespace.

Usage:
  skupper site create <name> [flags]

Examples:
skupper site create my-site --wait configured

Flags:
      --enable-link-access        allow access for incoming links from remote sites (default: false)
  -h, --help                      help for create
      --link-access-type string   configure external access for links from remote sites.
                                  Choices: [route|loadbalancer]. Default: On OpenShift, route is the default; 
                                  for other Kubernetes flavors, loadbalancer is the default.
      --service-account string    the Kubernetes service account under which to run the Skupper controller
      --timeout duration          raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 3m0s)
      --wait string               Wait for the given status before exiting. Choices: configured, ready, none (default "ready")

Global Flags:
  -c, --context string      Set the kubeconfig context
      --kubeconfig string   Path to the kubeconfig file to use
  -n, --namespace string    Set the namespace
  -p, --platform string     Set the platform type to use [kubernetes, podman, docker, linux]
```
