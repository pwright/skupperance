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

Global Flags:
  -c, --context string      Set the kubeconfig context
      --kubeconfig string   Path to the kubeconfig file to use
  -n, --namespace string    Set the namespace
  -p, --platform string     Set the platform type to use [kubernetes, podman, docker, linux]

Use "skupper system [command] --help" for more information about a command.

```
