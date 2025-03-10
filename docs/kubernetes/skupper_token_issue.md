# `skupper token issue` Command Reference

```
Issue a token file redeemable for a link to the current site.

Usage:
  skupper token issue <fileName> [flags]

Examples:
skupper token issue ~/token1.yaml

Flags:
      --cost string                  the configured "expense" of sending traffic over the link. (default "1")
  -e, --expiration-window duration   The period of time in which an access token for this grant can be redeemed. (default 15m0s)
  -h, --help                         help for issue
  -r, --redemptions-allowed int      The number of times an access token for this grant can be redeemed. (default 1)
  -t, --timeout duration             raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 1m0s)
```

🔗 **External Documentation:** [https://skupperproject.github.io/refdog/commands/token/issue.html](https://skupperproject.github.io/refdog/commands/token/issue.html)

