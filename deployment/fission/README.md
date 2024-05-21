
# Elasticsearch request
## Twitter
### Total number
```
GET twitter/_count/
```

### The total number of instances (sentiment < 0)
```
GET twitter/_search
{
   "query": {
    "bool": {
      "filter": {
        "range": {
          "sentiment": {
            "lt": 0
          }
        }
      }
    }
  },
  "_source": "topic",
  "aggs": {
    "topics_count": {
      "terms": {
        "field": "topic",
        "size": 1000 
      }
    }
  }
}
```
### The total number of instances (sentiment > 0)
```
GET twitter/_search
{
   "query": {
    "bool": {
      "filter": {
        "range": {
          "sentiment": {
            "gt": 0
          }
        }
      }
    }
  },
  "_source": "topic",
  "aggs": {
    "topics_count": {
      "terms": {
        "field": "topic",
        "size": 1000  // Specify the number of top topics you want to retrieve
      }
    }
  }
}
```

## mastadon
### total number
```
GET mastodon/_count/
```

### The total number of instances (sentiment < 0)
```
GET mastodon/_search
{
   "query": {
    "bool": {
      "filter": {
        "range": {
          "sentiment_score": {
            "lt": 0
          }
        }
      }
    }
  },
  "_source": "topics",
  "aggs": {
    "topics_count": {
      "terms": {
        "field": "topics",
        "size": 1000 
      }
    }
  }
}
```

### The total number of instances (sentiment > 0)
```
GET mastodon/_search
{
   "query": {
    "bool": {
      "filter": {
        "range": {
          "sentiment_score": {
            "gt": 0
          }
        }
      }
    }
  },
  "_source": "topics",
  "aggs": {
    "topics_count": {
      "terms": {
        "field": "topics",
        "size": 1000 
      }
    }
  }
}
```

### The population density in Victoria
```
GET sudo/_search
{
  "query": {
       "term": { " state_name_2016.keyword": "Victoria"}
        },
        "_source": [
            "sa2_name_2016",
            " area_km2",
            " sa2_maincode_2016",
            " pop_density_2020_people_per_km2"
        ],
        "size": 1000
    }
```

### The total stations during 2021-01 to 2022-12 at different region in VIC
```
GET bom/_search
{
  "size": 0,
  "query": {
    "bool": {
      "must": [
        {
          "range": {"Start": {"lte": "2021-01"}}
        },
        {
          "range": {"End": {"gte": "2022-12"}}
        },
        {
          "match": {
            "state": "Victoria"
          }
        }
      ]
    }
  },
  "aggs": {
    "by_SA2_NAME21": {
      "terms": {"field": "SA2_NAME21"},
      "aggs": {
        "unique_names_count": {
          "cardinality": {"field": "Name"}
        }
      }
    }
  }
}
```

### The site coordinates in VIC
```
GET bom/_search
{
  "query": {
         "bool": {
             "must": [
             {"range": {"Start": {"lte": "2021-01"}}},
             {
              "range": {"End": {"gte": "2022-12"}}},
             {
               "match": {"state": "Victoria"}
             }
            ]
         }
        },
    "_source": ["Site",  "Start", "End", "Location.lat", "Location.lon"],
    "size": 1000
    }
```

### Query region name by site in VIC
```
GET bom/_search
{
  "query": {"match_all": {}},
     "_source": ["Name", "SA2_NAME21"],
     "size": 10000 
      }
```


### Caculate average rate of asthma
GET asthma/_search
{
  "size": 0,
  "aggs": {
    "by_suburb": {
      "terms": {
        "field": "suburb.keyword","size": 1000},
      "aggs": {
        "average_asthma_rate": {
          "avg": {"field": "asthma_me_2_rate_3_11_7_13" }
          },
        "average_respiratory_rate": {
          "avg": {"field": "respirtry_me_2_rate_3_11_7_13"  }
        }
      }
    }
  }
}


# Fission function

```
cd fission
kubectl apply -f ./specs/shared-data.yaml
kubectl apply -f ./specs/mastodon-data.yaml
kubectl apply -f ./specs/twitter-data.yaml

fission function create --name mastodon-count --env python --code ./function/mastodon_count.py --configmap shared-data --configmap mastodon-data
fission function create --name mastodon-gt --env python --code ./function/mastodon_gt.py --configmap shared-data --configmap mastodon-data
fission function create --name mastodon-lt --env python --code ./function/mastodon_lt.py --configmap shared-data --configmap mastodon-data

fission function create --name twitter-count --env python --code ./function/twitter_count.py --configmap shared-data --configmap twitter-data
fission function create --name twitter-gt --env python --code ./function/twitter_gt.py --configmap shared-data --configmap twitter-data
fission function create --name twitter-lt --env python --code ./function/twitter_lt.py --configmap shared-data --configmap twitter-data
fission function create --name twitter-sentiment --env python --code ./function/twitter_sentiment.py --configmap shared-data --configmap twitter-data


fission function create --name get-population-list --env python --code ./function/get-population-list.py --configmap shared-data
fission function create --name get-bom-list --env python --code ./function/get-bom-list.py --configmap shared-data
fission function create --name get-bom-name --env python --code ./function/get-bom-name.py --configmap shared-data
fission function create --name get-map-region-info --env python --code ./function/get-map-region-info.py --configmap shared-data

fission function create --name get-asthma-avg --env python --code ./function/get-asthma-avg.py --configmap shared-data


fission route create  --url /mastodon/gt --function mastodon-gt --name mastodon-gt --createingress
fission route create  --url /mastodon/lt --function mastodon-lt --name mastodon-lt --createingress
fission route create  --url /mastodon/count --function mastodon-count --name mastodon-count --createingress

fission route create  --url /twitter/count --function twitter-count --name twitter-count --createingress
fission route create  --url /twitter/lt --function twitter-lt --name twitter-lt --createingress
fission route create  --url /twitter/gt --function twitter-gt --name twitter-gt --createingress
fission route create  --url /twitter/sentiment --function twitter-sentiment --name twitter-sentiment --createingress


fission route create  --url /get-population-list --function get-population-list --name get-population-list --createingress
fission route create  --url /get-bom-list --function get-bom-list --name get-bom-list --createingress
fission route create  --url /get-bom-name --function get-bom-name --name get-bom-name --createingress
fission route create  --url /get-map-region-info --function get-map-region-info --name get-map-region-info --createingress

fission fn create --name fetch-epa --code fetch_epa.py --env python --configmap shared-data
fission timer create --name fetch-epa --function fetch-epa --cron "@every 5m" 
fission fn create --name get-epa --env python --code get-epa-list.py --configmap shared-data
fission route create --url epa --env python --function get-epa 

fission route create  --url /get-asthma-avg --function get-asthma-avg --name get-asthma-avg --createingress

kubectl port-forward service/router -n fission 9090:80



```

# timer
```
fission timer update --name fetch-epa --cron
 "@every 1h"
trigger 'fetch-epa' updated
Current Server Time:    2024-05-21T22:38:42Z
Next 1 invocation:      2024-05-21T23:38:42Z


fission timer list  
NAME      CRON      FUNCTION_NAME
fetch-epa @every 6h fetch-epa

fission timer showschedule --cron "@every 1h"
Current Server Time:    2024-05-21T22:40:19Z
Next 1 invocation:      2024-05-21T23:40:19Z
```





# API for frontend
1. create a tunnel
```
ssh -i ./<private_key>  -L 6443:"192.168.10.12":6443  ubuntu@172.26.128.21
```
2. set up elasticsearch
```
kubectl port-forward service/elasticsearch-master -n elastic 9200:9200
kubectl port-forward service/kibana-kibana -n elastic 5601:5601
```
3. connect to fission router
```
kubectl port-forward service/router -n fission 9090:80
```
4. get api request 
```
http://127.0.0.1:9090/twitter/count //count tweet number
http://127.0.0.1:9090/twitter/gt //aggregate the topic for the sentiment number > 0
http://127.0.0.1:9090/twitter/lt  //aggregate the topic for the sentiment number < 0
http://127.0.0.1:9090/twitter/sentiment //get the sentiment average score by area

http://127.0.0.1:9090/mastodon/count //count the mastodon number
http://127.0.0.1:9090/mastodon/gt //aggregate the topic for the sentiment number > 0
http://127.0.0.1:9090/mastodon/lt //aggregate the topic for the sentiment number <> 0

http://127.0.0.1:9090/get-population-list //list site and coordinates
http://127.0.0.1:9090/get-bom-list// aggregate the station in victoria ar different regions
http://127.0.0.1:9090/get-bom-name // query region name by site
http://127.0.0.1:9090/get-map-region-info // list regions

http://127.0.0.1:9090/get-asthma-avg // caculate asthma avg rate

```









