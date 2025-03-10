# `skupper completion zsh` Command Reference

```
Generate the autocompletion script for the zsh shell.

If shell completion is not already enabled in your environment you will need
to enable it.  You can execute the following once:

	echo "autoload -U compinit; compinit" >> ~/.zshrc

To load completions in your current shell session:

	source <(skupper completion zsh)

To load completions for every new session, execute once:

#### Linux:

	skupper completion zsh > "${fpath[1]}/_skupper"

#### macOS:

	skupper completion zsh > $(brew --prefix)/share/zsh/site-functions/_skupper

You will need to start a new shell for this setup to take effect.

Usage:
  skupper completion zsh [flags]

Flags:
  -h, --help              help for zsh
      --no-descriptions   disable completion descriptions
```

🔗 **External Documentation:** [https://skupperproject.github.io/refdog/commands/completion/zsh.html](https://skupperproject.github.io/refdog/commands/completion/zsh.html)

