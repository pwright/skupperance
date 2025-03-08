# `skupper` Command Reference

```
Skupper is an open-source tool that enables secure communication across clusters with no VPNs or special firewall rules.
For more information visit https://skupperproject.github.io/refdog/

Usage:
  skupper [command]

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  connector   Binds target workloads in the local site to listeners in remote sites.
  debug       
  help        Help about any command
  link        A site-to-site communication channel
  listener    Binds a connection endpoint in the local site to target workloads in remote sites.
  site        A site is where skupper is deployed and components of your application are running.
  system      non-kubernetes sites are static and Custom Resources need to be provided.
  token       Security mechanism for creating connections between Skupper sites.
  version     Display versions of Skupper components.

Flags:
  -h, --help               help for skupper
  -n, --namespace string   Set the namespace
  -p, --platform string    Set the platform type to use [kubernetes, podman, docker, linux]

Use "skupper [command] --help" for more information about a command.
```

## Subcommands
- [completion](./skupper_completion.md)
- [connector](./skupper_connector.md)
- [debug](./skupper_debug.md)
- [help](./skupper_help.md)
- [link](./skupper_link.md)
- [listener](./skupper_listener.md)
- [site](./skupper_site.md)
- [system](./skupper_system.md)
- [token](./skupper_token.md)
- [version](./skupper_version.md)
