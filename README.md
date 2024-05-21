# COMP90024_2024_ASMT2_Group12

#TODO
Find data sets



├── README.md
├── config
├── data
│   ├── BOM-Station
│   │   ├── BOM-Station-Origin.csv
│   │   ├── BOM-Station.json
│   │   ├── BOM.json
│   │   ├── convert.py
│   │   ├── filtered_suburb.json
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
│   │   ├── asthma.json
│   │   ├── asthma_with_coordinates.json
│   │   ├── asthma_with_coordinates_filtered.json
│   │   └── asthma_with_sa2.json
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
│   │   │   ├── get-bom-list.py
│   │   │   ├── get-bom-name.py
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
│   │   │   ├── fission-deployment-config.yaml
│   │   │   ├── function-coordinate-list.yaml
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
├── docker-compose.yml
├── docs
│   └── README.md
├── frontend
│   ├── README.md
│   ├── api.json
│   ├── epa.ipynb
│   ├── mastodon_gt.json
│   ├── mastodon_lt.json
│   ├── mastodon_vs_twitter.ipynb
│   ├── station_vs_twitter.ipynb
│   ├── topic_percentage_comparison.png
│   ├── topic_percentage_for_different_sentiment.png
│   ├── twitter_gt.json
│   └── twitter_lt.json
├── installation
│   └── README.md
└── test
    └── README.md
