# `skupper completion powershell` Command Reference (podman)

```
Generate the autocompletion script for powershell.

To load completions in your current shell session:

	skupper completion powershell | Out-String | Invoke-Expression

To load completions for every new session, add the output of the above command
to your powershell profile.

Usage:
  skupper completion powershell [flags]

Flags:
  -h, --help              help for powershell
      --no-descriptions   disable completion descriptions

Global Flags:
  -n, --namespace string   Set the namespace
  -p, --platform string    Set the platform type to use [kubernetes, podman, docker, linux]
```
