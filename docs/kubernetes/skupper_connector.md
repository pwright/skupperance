# `skupper connector` Command Reference (kubernetes)

```
A connector is a endpoint in the local site and binds to listeners in remote sites

Usage:
  skupper connector [command]

Examples:
skupper connector create my-connector 8080
skupper connector status my-connector

Available Commands:
  create      create a connector
  delete      delete a connector
  generate    Generate a connector resource and output it to a file or screen
  status      get status of connectors
  update      update a connector

Flags:
  -h, --help   help for connector

Global Flags:
  -c, --context string      Set the kubeconfig context
      --kubeconfig string   Path to the kubeconfig file to use
  -n, --namespace string    Set the namespace
  -p, --platform string     Set the platform type to use [kubernetes, podman, docker, linux]

Use "skupper connector [command] --help" for more information about a command.
```

## Subcommands
- [create](./skupper_connector_create.md)
- [delete](./skupper_connector_delete.md)
- [generate](./skupper_connector_generate.md)
- [status](./skupper_connector_status.md)
- [update](./skupper_connector_update.md)
