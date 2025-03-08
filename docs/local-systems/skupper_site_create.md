# `skupper site create` Command Reference

```
A site is a place where components of your application are running.
Sites are linked to form application networks.
There can be only one site definition per namespace.

Usage:
  skupper site create <name> [flags]

Examples:
skupper site create my-site --wait configured

Flags:
      --bind-host string                    A valid host or ip that can be used to bind a local port (default "0.0.0.0")
      --enable-link-access                  allow access for incoming links from remote sites (default: false)
  -h, --help                                help for create
      --link-access-type string             configure external access for links from remote sites.
                                            Choices: [route|loadbalancer]. Default: On OpenShift, route is the default; 
                                            for other Kubernetes flavors, loadbalancer is the default.
      --subject-alternative-names strings   Add subject alternative names for the router access in non kubernetes environments
      --timeout duration                    raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 3m0s)
```

🔗 **External Documentation:** [https://skupperproject.github.io/refdog/commands/site/create.html](https://skupperproject.github.io/refdog/commands/site/create.html)

