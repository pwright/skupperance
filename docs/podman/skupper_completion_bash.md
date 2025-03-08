# `skupper completion bash` Command Reference (podman)

```
Generate the autocompletion script for the bash shell.

This script depends on the 'bash-completion' package.
If it is not installed already, you can install it via your OS's package manager.

To load completions in your current shell session:

	source <(skupper completion bash)

To load completions for every new session, execute once:

#### Linux:

	skupper completion bash > /etc/bash_completion.d/skupper

#### macOS:

	skupper completion bash > $(brew --prefix)/etc/bash_completion.d/skupper

You will need to start a new shell for this setup to take effect.

Usage:
  skupper completion bash

Flags:
  -h, --help              help for bash
      --no-descriptions   disable completion descriptions

Global Flags:
  -n, --namespace string   Set the namespace
  -p, --platform string    Set the platform type to use [kubernetes, podman, docker, linux]
```
