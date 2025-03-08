# `skupper site` Command Reference

```
A site is a place where components of your application are running. Sites are linked to form application networks.

Usage:
  skupper site [command]

Examples:
skupper site create my-site
skupper site status

Available Commands:
  create      Create a new site
  delete      Delete a site
  generate    Generate a site resource and output it to a file or screen
  status      Get the site status
  update      Change site settings

Flags:
  -h, --help   help for site

Global Flags:
  -c, --context string      Set the kubeconfig context
      --kubeconfig string   Path to the kubeconfig file to use
  -n, --namespace string    Set the namespace
  -p, --platform string     Set the platform type to use [kubernetes, podman, docker, linux]

Use "skupper site [command] --help" for more information about a command.

```
