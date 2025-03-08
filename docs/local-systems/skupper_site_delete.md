# `skupper site delete` Command Reference

```
Delete a site

Usage:
  skupper site delete [flags]

Examples:
skupper site delete my-site
skupper site delete my-site --wait=false
skupper site delete --all

Flags:
      --all                delete all skupper resources associated with site in current namespace
  -h, --help               help for delete
      --timeout duration   raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 1m0s)
```
