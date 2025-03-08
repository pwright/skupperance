# `skupper system` Command Reference

```
Non-kubernetes sites can be created using the standard V2 site declaration 
approach, which is based on the new set of Custom Resource Definitions (CRDs).

Usage:
  skupper system [command]

Examples:
system setup --path ./my-config-path -n my-namespace

Available Commands:
  install     Install local system infrastructure and configure the environment
  reload      Forces to overwrite an existing namespace based on input/resources
  setup       Create a non-kube site based on provided Skupper Custom Resources
  start       Start the Skupper components for the current site
  stop        Shut down the Skupper components for the current site
  teardown    Remove the Skupper components and resources from the from the current namespace
  uninstall   Remove local system infrastructure

Flags:
  -h, --help   help for system

Use "skupper system [command] --help" for more information about a command.
```

🔗 **External Documentation:** [https://skupperproject.github.io/refdog/commands/system/](https://skupperproject.github.io/refdog/commands/system/)


## Subcommands
- [install](./skupper_system_install.md)
- [reload](./skupper_system_reload.md)
- [setup](./skupper_system_setup.md)
- [start](./skupper_system_start.md)
- [stop](./skupper_system_stop.md)
- [teardown](./skupper_system_teardown.md)
- [uninstall](./skupper_system_uninstall.md)
