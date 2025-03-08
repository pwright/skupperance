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

Global Flags:
  -c, --context string      Set the kubeconfig context
      --kubeconfig string   Path to the kubeconfig file to use
  -n, --namespace string    Set the namespace
  -p, --platform string     Set the platform type to use [kubernetes, podman, docker, linux]

Use "skupper listener [command] --help" for more information about a command.

```
