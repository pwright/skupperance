# `skupper system setup` Command Reference

```
Bootstraps a nonkube Skupper site base on the provided flags.

When the path (--path) flag is provided, it will be used as the source
directory containing the Skupper custom resources to be processed,
generating a local Skupper site using the "default" namespace, unless
a namespace is set in the custom resources, or if the namespace (-n)
flag is provided.

A namespace is just a directory in the file system where all site specific
files are stored, like certificates, configurations, the original sources
(original custom resources used to bootstrap the nonkube site) and
the runtime files generated during initialization.

Namespaces are stored under ${XDG_DATA_HOME}/skupper/namespaces
for regular users when XDG_DATA_HOME environment variable is set, or under
${HOME}/.local/share/skupper/namespaces when it is not set.

As the root user, namespaces are stored under: /var/lib/skupper/namespaces.
In case the path (--path) flag is omitted, Skupper will try to process
custom resources stored at the input/resources directory of the default namespace,
or from the namespace provided through the namespace (-n) flag.

If the respective namespace already exists and you want to bootstrap it
over, you must provide the force (-f) flag. When you do that, the existing
Certificate Authorities (CAs) are preserved, so eventual existing incoming
links should be able to reconnect.

To produce a bundle, instead of rendering a site, the bundle strategy (-b)
flag must be set to "bundle" or "tarball".

Usage:
  skupper system setup [flags]

Flags:
  -f, --force             Forces to overwrite an existing namespace
  -h, --help              help for setup
      --path string       Custom resources location on the file system
  -b, --strategy string   The bundle strategy to be produced. Choices: bundle, tarball
```
