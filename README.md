# COMP90024_2024_ASMT2_Group12
```
Team12 		  	
Meilun Yao   1076213
Yingyi Luan 1179002
Yuntao Lu 1166487
Jiayi Xu 1165986
Zheyuan Wu 1166034
```
# introduction

The structure of this project follows the chronological progression. It began by searching and processing various sources from social and data platforms, focusing on finding data with high availability. Particular emphasis was placed on the SUDO and Maston scenarios. Next, we conducted a thorough evaluation of the tools utilized in our project. It also includes a detailed presentation of the system's main features, alongside an overview of its basic design and architecture. 


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

## Step 3 build ssh tunnel
```shell
chmod 600 ./{your_private_key.pem}
```
```shell
ssh -i ~/{your_private_key.pem}  -L 6443:"192.168.10.12":6443 ubuntu@172.26.128.21
```

## Step 4
Download OpenRC Stack file from MRC dashboard. Instructions in Workshop week4-2 Page15. Once you download the file, run following command on your **local machine**, **not on Bastion node**:

```shell
source ./{<your project name>-openrc.sh}
```

Then cd to our GitHub repository where you can see a [config](https://github.com/lollyluan/COMP90024_2024_ASMT2_Group12/blob/main/config) file. 

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

# How client can run 
navigate to frontend to run the client

-- mastodon_vs_twitter.ipynb Scenario 1/2

-- station_vs_twitter.ipynb Scenario 3/4

Run the block from the first to last after starting all the local service





## sturcture 
```
├── README.md
├── config
├── data
│   ├── BOM-Station
│   │   ├── BOM-Station-Origin.csv
│   │   ├── convert.py
│   │   ├── pre-station.ipynb
│   │   └── suburb_centre_bom.json
│   ├── Mastodon
│   │   ├── mastadonau.ipynb
│   │   └── mastodon_data.py
│   ├── README.md
│   ├── SA2-Map
│   │   ├── SA2_2021_AUST_GDA2020.dbf
│   │   ├── SA2_2021_AUST_GDA2020.prj
│   │   ├── SA2_2021_AUST_GDA2020.shp
│   │   ├── SA2_2021_AUST_GDA2020.shx
│   │   ├── SA2_2021_AUST_GDA2020.xml
│   │   └── convert.py
│   ├── SUDO-ABS-PopulationDensity
│   │   ├── abs_regional_population_sa2_2001_2020-4826266136351011880.csv
│   │   ├── abs_regional_population_sa2_2001_2020-4826266136351011880.json
│   │   ├── abs_regional_population_sa2_2001_2020-metadata-5317016466857159348.json
│   │   ├── climateStation.py
│   │   ├── convert.py
│   │   ├── sudo.ipynb
│   │   └── sudo_region.json
│   ├── asthma
│   │   ├── asthma.ipynb
│   │   ├── asthma_edit.json
│   │   ├── fetch_epa.py
│   │   └── victoria_data.json
│   └── twitter
│       ├── byte_split.py
│       ├── filtered_tweets.json
│       ├── final.json
│       ├── merge_topics.py
│       ├── suburb_centre.json
│       ├── tweet.json
│       └── tweet_process.ipynb
├── database
│   ├── README.md
│   └── elastic.py
├── deployment
│   ├── fission
│   │   ├── README.md
│   │   ├── function
│   │   │   ├── coordinate-list.py
│   │   │   ├── get-asthma-avg.py
│   │   │   ├── get-bom-list.py
│   │   │   ├── get-bom-name.py
│   │   │   ├── get-epa-list.py
│   │   │   ├── get-map-region-info.py
│   │   │   ├── get-population-list.py
│   │   │   ├── mastodon_count.py
│   │   │   ├── mastodon_gt.py
│   │   │   ├── mastodon_lt.py
│   │   │   ├── twitter_count.py
│   │   │   ├── twitter_gt.py
│   │   │   ├── twitter_lt.py
│   │   │   └── twitter_sentiment.py
│   │   ├── specs
│   │   │   ├── README
│   │   │   ├── env-nodejs.yaml
│   │   │   ├── env-python.yaml
│   │   │   ├── epa-data.yaml
│   │   │   ├── fission-deployment-config.yaml
│   │   │   ├── function-coordinate-list.yaml
│   │   │   ├── function-get-asthma-avg.yaml
│   │   │   ├── function-get-bom-list.yaml
│   │   │   ├── function-get-bom-name.yaml
│   │   │   ├── function-get-map-region-info.yaml
│   │   │   ├── function-get-population-list.yaml
│   │   │   ├── function-mastodon-count.yaml
│   │   │   ├── mastodon-data.yaml
│   │   │   ├── shared-data.yaml
│   │   │   └── twitter-data.yaml
│   │   ├── test.py
│   │   └── utils.py
│   └── kubenetes
│       └── flask-app.yaml
├── docs
│   └── README.md
├── frontend
│   ├── README.md
│   ├── epa.ipynb
│   ├── mastodon_vs_twitter.ipynb
│   ├── station_vs_twitter.ipynb
│   ├── topic_percentage_comparison.png
│   └── topic_percentage_for_different_sentiment.png
├── installation
│   └── README.md
└── test
    ├── README.md
    └── end-to-end.py
```
