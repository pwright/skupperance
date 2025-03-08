# `skupper site generate` Command Reference

```
A site is a place where components of your application are running.
Sites are linked to form application networks.
There can be only one site definition per namespace.
Generate a site resource to evaluate what will be created with the site create command

Usage:
  skupper site generate <name> [flags]

Examples:
skupper site generate my-site --enable-link-access

Flags:
      --bind-host string                    A valid host or ip that can be used to bind a local port (default "0.0.0.0")
      --enable-link-access                  allow access for incoming links from remote sites (default: false)
  -h, --help                                help for generate
      --link-access-type string             configure external access for links from remote sites.
                                            Choices: [route|loadbalancer]. Default: On OpenShift, route is the default; 
                                            for other Kubernetes flavors, loadbalancer is the default.
  -o, --output string                       print resources to the console instead of submitting them to the Skupper controller. Choices: json, yaml (default "yaml")
      --subject-alternative-names strings   Add subject alternative names for the router access in non kubernetes environments
```
