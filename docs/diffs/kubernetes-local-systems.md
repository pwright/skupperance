# 📄 Comparison: `kubernetes` vs `local-systems`

| Category       | Count |
|---------------|------:|
| ✅ Identical Files | 30 |
| ⚠️ Different Files | 13 |

## ✅ Identical Files

- `skupper_completion.md`
- `skupper_completion_bash.md`
- `skupper_completion_fish.md`
- `skupper_completion_powershell.md`
- `skupper_completion_zsh.md`
- `skupper_connector.md`
- `skupper_connector_delete.md`
- `skupper_connector_status.md`
- `skupper_debug.md`
- `skupper_help.md`
- `skupper_link.md`
- `skupper_link_generate.md`
- `skupper_link_status.md`
- `skupper_listener.md`
- `skupper_listener_generate.md`
- `skupper_listener_status.md`
- `skupper_site.md`
- `skupper_site_status.md`
- `skupper_system.md`
- `skupper_system_install.md`
- `skupper_system_reload.md`
- `skupper_system_setup.md`
- `skupper_system_start.md`
- `skupper_system_stop.md`
- `skupper_system_teardown.md`
- `skupper_system_uninstall.md`
- `skupper_token.md`
- `skupper_token_issue.md`
- `skupper_token_redeem.md`
- `skupper_version.md`

## ⚠️ Differences

### 🔍 `skupper.md`

**kubernetes** vs **local-systems**

```diff
--- docs/kubernetes/skupper.md
+++ docs/local-systems/skupper.md
@@ -20,11 +20,9 @@
   version     Display versions of Skupper components.

 

 Flags:

-  -c, --context string      Set the kubeconfig context

-  -h, --help                help for skupper

-      --kubeconfig string   Path to the kubeconfig file to use

-  -n, --namespace string    Set the namespace

-  -p, --platform string     Set the platform type to use [kubernetes, podman, docker, linux]

+  -h, --help               help for skupper

+  -n, --namespace string   Set the namespace

+  -p, --platform string    Set the platform type to use [kubernetes, podman, docker, linux]

 

 Use "skupper [command] --help" for more information about a command.

 ```

```

### 🔍 `skupper_connector_create.md`

**kubernetes** vs **local-systems**

```diff
--- docs/kubernetes/skupper_connector_create.md
+++ docs/local-systems/skupper_connector_create.md
@@ -13,12 +13,7 @@
 Flags:

   -h, --help                     help for create

       --host string              The hostname or IP address of the local connector

-  -i, --include-not-ready        If true, include server pods that are not in the ready state.

   -r, --routing-key string       The identifier used to route traffic from listeners to connectors

-  -s, --selector string          A Kubernetes label selector for specifying target server pods.

-      --timeout duration         raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 1m0s)

       --tls-credentials string   the name of a Kubernetes secret containing the generated or externally-supplied TLS credentials.

       --type string              The connector type. Choices: [tcp]. (default "tcp")

-      --wait string              Wait for the given status before exiting. Choices: configured, ready, none (default "configured")

-  -w, --workload string          A Kubernetes resource name that identifies a workload expressed like resource-type/resource-name. Expected resource types: service, daemonset, deployment, and statefulset.

 ```

```

### 🔍 `skupper_connector_generate.md`

**kubernetes** vs **local-systems**

```diff
--- docs/kubernetes/skupper_connector_generate.md
+++ docs/local-systems/skupper_connector_generate.md
@@ -13,11 +13,8 @@
 Flags:

   -h, --help                     help for generate

       --host string              The hostname or IP address of the local connector

-  -i, --include-not-ready        If true, include server pods that are not in the ready state.

   -o, --output string            print resources to the console instead of submitting them to the Skupper controller. Choices: json, yaml (default "yaml")

   -r, --routing-key string       The identifier used to route traffic from listeners to connectors

-  -s, --selector string          A Kubernetes label selector for specifying target server pods.

       --tls-credentials string   the name of a Kubernetes secret containing the generated or externally-supplied TLS credentials.

       --type string              The connector type. Choices: [tcp]. (default "tcp")

-  -w, --workload string          A Kubernetes resource name that identifies a workload expressed like resource-type/resource-name. Expected resource types: service, daemonset, deployment, and statefulset.

 ```

```

### 🔍 `skupper_connector_update.md`

**kubernetes** vs **local-systems**

```diff
--- docs/kubernetes/skupper_connector_update.md
+++ docs/local-systems/skupper_connector_update.md
@@ -13,13 +13,8 @@
 Flags:

   -h, --help                     help for update

       --host string              The hostname or IP address of the local connector

-  -i, --include-not-ready        If true, include server pods that are not in the ready state.

       --port int                 The port of the local connector

   -r, --routing-key string       The identifier used to route traffic from listeners to connectors

-  -s, --selector string          A Kubernetes label selector for specifying target server pods.

-      --timeout duration         raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 1m0s)

       --tls-credentials string   the name of a Kubernetes secret containing the generated or externally-supplied TLS credentials.

       --type string              The connector type. Choices: [tcp]. (default "tcp")

-      --wait string              Wait for the given status before exiting. Choices: configured, ready, none (default "configured")

-  -w, --workload string          A Kubernetes resource name that identifies a workload expressed like resource-type/resource-name. Expected resource types: service, daemonset, deployment, and statefulset.

 ```

```

### 🔍 `skupper_link_delete.md`

**kubernetes** vs **local-systems**

```diff
--- docs/kubernetes/skupper_link_delete.md
+++ docs/local-systems/skupper_link_delete.md
@@ -12,5 +12,4 @@
 Flags:

   -h, --help               help for delete

       --timeout duration   raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 1m0s)

-      --wait               Wait for deletion to complete before exiting (default true)

 ```

```

### 🔍 `skupper_link_update.md`

**kubernetes** vs **local-systems**

```diff
--- docs/kubernetes/skupper_link_update.md
+++ docs/local-systems/skupper_link_update.md
@@ -11,5 +11,4 @@
   -h, --help                     help for update

       --timeout duration         raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 1m0s)

       --tls-credentials string   the name of a Kubernetes secret containing the generated or externally-supplied TLS credentials.

-      --wait string              Wait for the given status before exiting. Choices: configured, ready, none (default "ready")

 ```

```

### 🔍 `skupper_listener_create.md`

**kubernetes** vs **local-systems**

```diff
--- docs/kubernetes/skupper_listener_create.md
+++ docs/local-systems/skupper_listener_create.md
@@ -13,8 +13,6 @@
   -h, --help                     help for create

       --host string              The hostname or IP address of the local listener. Clients at this site use the listener host and port to establish connections to the remote service.

   -r, --routing-key string       The identifier used to route traffic from listeners to connectors

-      --timeout duration         raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 1m0s)

       --tls-credentials string   the name of a Kubernetes secret containing the generated or externally-supplied TLS credentials.

       --type string              The listener type. Choices: [tcp]. (default "tcp")

-      --wait string              Wait for the given status before exiting. Choices: configured, ready, none (default "configured")

 ```

```

### 🔍 `skupper_listener_delete.md`

**kubernetes** vs **local-systems**

```diff
--- docs/kubernetes/skupper_listener_delete.md
+++ docs/local-systems/skupper_listener_delete.md
@@ -10,7 +10,5 @@
 skupper listener delete database

 

 Flags:

-  -h, --help               help for delete

-  -t, --timeout duration   raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 1m0s)

-      --wait               Wait for deletion to complete before exiting (default true)

+  -h, --help   help for delete

 ```

```

### 🔍 `skupper_listener_update.md`

**kubernetes** vs **local-systems**

```diff
--- docs/kubernetes/skupper_listener_update.md
+++ docs/local-systems/skupper_listener_update.md
@@ -15,8 +15,6 @@
       --host string              The hostname or IP address of the local listener. Clients at this site use the listener host and port to establish connections to the remote service.

       --port int                 The port of the local listener

   -r, --routing-key string       The identifier used to route traffic from listeners to connectors

-      --timeout duration         raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 1m0s)

   -t, --tls-credentials string   the name of a Kubernetes secret containing the generated or externally-supplied TLS credentials.

       --type string              The listener type. Choices: [tcp]. (default "tcp")

-      --wait string              Wait for the given status before exiting. Choices: configured, ready, none (default "configured")

 ```

```

### 🔍 `skupper_site_create.md`

**kubernetes** vs **local-systems**

```diff
--- docs/kubernetes/skupper_site_create.md
+++ docs/local-systems/skupper_site_create.md
@@ -12,12 +12,12 @@
 skupper site create my-site --wait configured

 

 Flags:

-      --enable-link-access        allow access for incoming links from remote sites (default: false)

-  -h, --help                      help for create

-      --link-access-type string   configure external access for links from remote sites.

-                                  Choices: [route|loadbalancer]. Default: On OpenShift, route is the default; 

-                                  for other Kubernetes flavors, loadbalancer is the default.

-      --service-account string    the Kubernetes service account under which to run the Skupper controller

-      --timeout duration          raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 3m0s)

-      --wait string               Wait for the given status before exiting. Choices: configured, ready, none (default "ready")

+      --bind-host string                    A valid host or ip that can be used to bind a local port (default "0.0.0.0")

+      --enable-link-access                  allow access for incoming links from remote sites (default: false)

+  -h, --help                                help for create

+      --link-access-type string             configure external access for links from remote sites.

+                                            Choices: [route|loadbalancer]. Default: On OpenShift, route is the default; 

+                                            for other Kubernetes flavors, loadbalancer is the default.

+      --subject-alternative-names strings   Add subject alternative names for the router access in non kubernetes environments

+      --timeout duration                    raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 3m0s)

 ```

```

### 🔍 `skupper_site_delete.md`

**kubernetes** vs **local-systems**

```diff
--- docs/kubernetes/skupper_site_delete.md
+++ docs/local-systems/skupper_site_delete.md
@@ -15,5 +15,4 @@
       --all                delete all skupper resources associated with site in current namespace

   -h, --help               help for delete

       --timeout duration   raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 1m0s)

-      --wait               Wait for deletion to complete before exiting (default true)

 ```

```

### 🔍 `skupper_site_generate.md`

**kubernetes** vs **local-systems**

```diff
--- docs/kubernetes/skupper_site_generate.md
+++ docs/local-systems/skupper_site_generate.md
@@ -13,12 +13,11 @@
 skupper site generate my-site --enable-link-access

 

 Flags:

-      --bind-host string                    A valid host or ip that can be used to bind a local port (default "0.0.0.0")

-      --enable-link-access                  allow access for incoming links from remote sites (default: false)

-  -h, --help                                help for generate

-      --link-access-type string             configure external access for links from remote sites.

-                                            Choices: [route|loadbalancer]. Default: On OpenShift, route is the default; 

-                                            for other Kubernetes flavors, loadbalancer is the default.

-  -o, --output string                       print resources to the console instead of submitting them to the Skupper controller. Choices: json, yaml (default "yaml")

-      --subject-alternative-names strings   Add subject alternative names for the router access in non kubernetes environments

+      --enable-link-access        allow access for incoming links from remote sites (default: false)

+  -h, --help                      help for generate

+      --link-access-type string   configure external access for links from remote sites.

+                                  Choices: [route|loadbalancer]. Default: On OpenShift, route is the default; 

+                                  for other Kubernetes flavors, loadbalancer is the default.

+  -o, --output string             print resources to the console instead of submitting them to the Skupper controller. Choices: json, yaml (default "yaml")

+      --service-account string    the Kubernetes service account under which to run the Skupper controller

 ```

```

### 🔍 `skupper_site_update.md`

**kubernetes** vs **local-systems**

```diff
--- docs/kubernetes/skupper_site_update.md
+++ docs/local-systems/skupper_site_update.md
@@ -10,12 +10,12 @@
 skupper site update my-site --enable-link-access

 

 Flags:

-      --enable-link-access        allow access for incoming links from remote sites (default: false)

-  -h, --help                      help for update

-      --link-access-type string   configure external access for links from remote sites.

-                                  Choices: [route|loadbalancer]. Default: On OpenShift, route is the default; 

-                                  for other Kubernetes flavors, loadbalancer is the default.

-      --service-account string    the Kubernetes service account under which to run the Skupper controller

-      --timeout duration          raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 30s)

-      --wait string               Wait for the given status before exiting. Choices: configured, ready, none (default "ready")

+      --bind-host string                    A valid host or ip that can be used to bind a local port

+      --enable-link-access                  allow access for incoming links from remote sites (default: false)

+  -h, --help                                help for update

+      --link-access-type string             configure external access for links from remote sites.

+                                            Choices: [route|loadbalancer]. Default: On OpenShift, route is the default; 

+                                            for other Kubernetes flavors, loadbalancer is the default.

+      --subject-alternative-names strings   Add subject alternative names for the router access in non kubernetes environments

+      --timeout duration                    raise an error if the operation does not complete in the given period of time (expressed in seconds). (default 30s)

 ```

```

