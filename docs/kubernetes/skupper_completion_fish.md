# `skupper completion fish` Command Reference (kubernetes)

```
Generate the autocompletion script for the fish shell.

To load completions in your current shell session:

	skupper completion fish | source

To load completions for every new session, execute once:

	skupper completion fish > ~/.config/fish/completions/skupper.fish

You will need to start a new shell for this setup to take effect.

Usage:
  skupper completion fish [flags]

Flags:
  -h, --help              help for fish
      --no-descriptions   disable completion descriptions

Global Flags:
  -c, --context string      Set the kubeconfig context
      --kubeconfig string   Path to the kubeconfig file to use
  -n, --namespace string    Set the namespace
  -p, --platform string     Set the platform type to use [kubernetes, podman, docker, linux]
```
