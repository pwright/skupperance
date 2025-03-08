# `skupper token` Command Reference

```
A token contains connection information and necessary credentials for one Skupper 
service network to connect to another.
Issue the token on the site that was configured to allow incoming links.
Redeem the token on the other site.

Usage:
  skupper token [command]

Examples:
skupper token issue <name> ~/token.yaml

Available Commands:
  issue       issue a token
  redeem      redeem a token

Flags:
  -h, --help   help for token

Use "skupper token [command] --help" for more information about a command.
```

🔗 **External Documentation:** [https://skupperproject.github.io/refdog/commands/token/](https://skupperproject.github.io/refdog/commands/token/)


## Subcommands
- [issue](./skupper_token_issue.md)
- [redeem](./skupper_token_redeem.md)
