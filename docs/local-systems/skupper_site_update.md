# `skupper site update` Command Reference

```
Change site settings of a given site.

Usage:
  skupper site update <name> [flags]

Examples:
skupper site update my-site --enable-link-access

Flags:
      --bind-host string                    A valid host or ip that can be used to bind a local port
      --enable-link-access                  allow access for incoming links from remote sites (default: false)
  -h, --help                                help for update
      --link-access-type string             configure external access for links from remote sites.
                                            Choices: [route|loadbalancer]. Default: On OpenShift, route is the default; 
                                            for other Kubernetes flavors, loadbalancer is the default.
      --subject-alternative-names strings   Add subject alternative names for the router access in non kubernetes environments
      --timeout duration                    raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 30s)
```

🔗 **External Documentation:** [https://skupperproject.github.io/refdog/commands/site/update.html](https://skupperproject.github.io/refdog/commands/site/update.html)

