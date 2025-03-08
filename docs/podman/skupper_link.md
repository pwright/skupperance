# `skupper link` Command Reference (podman)

```
A site-to-site communication channel. Links serve as a transport for application connections and requests. A set of linked sites constitute a network.

Usage:
  skupper link [command]

Examples:
skupper link generate
skupper link status

Available Commands:
  delete      Delete a link
  generate    Generate a new link resource in a yaml file
  status      Display the status
  update      Change link settings

Flags:
  -h, --help   help for link

Global Flags:
  -n, --namespace string   Set the namespace
  -p, --platform string    Set the platform type to use [kubernetes, podman, docker, linux]

Use "skupper link [command] --help" for more information about a command.
```

## Subcommands
- [delete](./skupper_link_delete.md)
- [generate](./skupper_link_generate.md)
- [status](./skupper_link_status.md)
- [update](./skupper_link_update.md)
