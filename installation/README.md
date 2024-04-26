
# Installation

## Step 1
Download following on your local machine
- OpenStack clients 6.3.x ([Installation instructions](https://docs.openstack.org/newton/user-guide/common/cli-install-openstack-command-line-clients.html)).
  > Note: Please ensure the following Openstack clients are installed: `python-cinderclient`, `python-keystoneclient`, `python-magnumclient`, `python-neutronclient`, `python-novaclient`, `python-octaviaclient`. See: [Install the OpenStack client](https://docs.openstack.org/newton/user-guide/common/cli-install-openstack-command-line-clients.html).
- JQ 1.6.x ([Installation instructions](https://jqlang.github.io/jq/download/)).
- Kubectl 1.26.8 ([Installation instructions](https://kubernetes.io/docs/tasks/tools/)).
- Helm 3.6.3 ([Installation instructions](https://helm.sh/docs/intro/install/)).
- MRC project with enough resources to create a Kubernetes cluster.
- Connect to [Campus network](https://studentit.unimelb.edu.au/wifi-vpn#uniwireless) if on-campus or [UniMelb Student VPN](https://studentit.unimelb.edu.au/wifi-vpn#vpn) if off-campus

## Step 2
Create key pairs on your MRC dashboard and share the public key. Once the public key been added to Bastion, you can access Bastion node by your own private key.

# Access kubernetes cluster 
## ssh tunnel
```shell
chmod 600 ./{your_private_key.pem}
```
```shell
ssh -i ~/{your_private_key.pem}  -L 6443:"192.168.10.12":6443 ubuntu@172.26.128.21
```

On your local machine, run following command:
First cd to our repository where you can see a [config](https://github.com/lollyluan/COMP90024_2024_ASMT2_Group12/blob/main/config) file. 

```shell
mkdir -p ~/.kube
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