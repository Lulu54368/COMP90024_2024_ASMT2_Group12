
# Installation
- OpenStack clients 6.3.x ([Installation instructions](https://docs.openstack.org/newton/user-guide/common/cli-install-openstack-command-line-clients.html)).
  > Note: Please ensure the following Openstack clients are installed: `python-cinderclient`, `python-keystoneclient`, `python-magnumclient`, `python-neutronclient`, `python-novaclient`, `python-octaviaclient`. See: [Install the OpenStack client](https://docs.openstack.org/newton/user-guide/common/cli-install-openstack-command-line-clients.html).
- JQ 1.6.x ([Installation instructions](https://jqlang.github.io/jq/download/)).
- Kubectl 1.26.8 ([Installation instructions](https://kubernetes.io/docs/tasks/tools/)).
- Helm 3.6.3 ([Installation instructions](https://helm.sh/docs/intro/install/)).
- MRC project with enough resources to create a Kubernetes cluster.
- Connect to [Campus network](https://studentit.unimelb.edu.au/wifi-vpn#uniwireless) if on-campus or [UniMelb Student VPN](https://studentit.unimelb.edu.au/wifi-vpn#vpn) if off-campus

# Access kubernetes cluster 
## ssh tunnel
chmod 600 <path-to-private-key> (e.g. ~/Downloads/mykeypair.pem)
ssh -i ~/test_key.pem  -L 6443:"192.168.10.12":6443 ubuntu@172.26.128.21
openstack coe cluster config elastic
```shell
openstack coe cluster config elastic
```

```shell
awk '
    /^    server:/ { sub(/https:\/\/[^:]+/, "https://127.0.0.1") }
    { print }
' config > temp && mv temp config
```
```shell
mv config ~/.kube/config
chmod 600 ~/.kube/config
```

```shell
kubectl get nodes
```
## Access elasticsearch
1. Watch all containers come up.
  $ kubectl get pods --namespace=elastic -l release=kibana -w
2. Retrieve the elastic user's password.
  $ kubectl get secrets --namespace=elastic elasticsearch-master-credentials -ojsonpath='{.data.password}' | base64 -d
3. Retrieve the kibana service account token.
  $ kubectl get secrets --namespace=elastic kibana-kibana-es-token -ojsonpath='{.data.token}' | base64 -d

## Access Fission
 You can create fission resources in the namespace "default"

  $ fission env create --name nodejs --image fission/node-env --namespace default

  $ curl https://raw.githubusercontent.com/fission/examples/master/nodejs/hello.js > hello.js

  $ fission function create --name hello --env nodejs --code hello.js --namespace default

  $ fission function test --name hello --namespace default
  Hello, world!