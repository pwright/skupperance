# `skupper listener` Command Reference

```
A listener is a connection endpoint in the local site and binds to target workloads in remote sites

Usage:
  skupper listener [command]

Examples:
skupper listener create my-listener 8080
skupper listener status my-listener

Available Commands:
  create      create a listener
  delete      delete a listener
  generate    generate a listener resource and output it to a file or screen
  status      get status of listeners
  update      update a listener

Flags:
  -h, --help   help for listener

Use "skupper listener [command] --help" for more information about a command.
```

## Subcommands
- [create](./skupper_listener_create.md)
- [delete](./skupper_listener_delete.md)
- [generate](./skupper_listener_generate.md)
- [status](./skupper_listener_status.md)
- [update](./skupper_listener_update.md)
