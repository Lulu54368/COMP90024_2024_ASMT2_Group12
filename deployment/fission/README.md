
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


# Fission function

```
cd fission
kubectl apply -f ./specs/shared-data.yaml
kubectl apply -f ./specs/mastodon-data.yaml
kubectl apply -f ./specs/twitter-data.yaml

fission function create --name mastodon-count --env python --code ./function/mastodon_count.py --configmap shared-data --configmap 
mastodon-data
fission function create --name twitter-count --env python --code ./function/twitter_count.py --configmap shared-data --configmap twitter-data
fission function create --name twitter-gt --env python --code ./function/twitter_gt.py --configmap shared-data --configmap twitter-data
fission function create --name twitter-lt --env python --code ./function/twitter_lt.py --configmap shared-data --configmap twitter-data

fission route create  --url /mastodon/gt --function mastodon-gt --name mastodon-gt --createingress
fission route create  --url /mastodon/lt --function mastodon-lt --name mastodon-lt --createingress
fission route create  --url /mastodon/count --function mastodon-count --name mastodon-count --createingress
fission route create  --url /twitter/count --function twitter-count --name twitter-count --createingress
fission route create  --url /twitter/lt --function twitter-lt --name twitter-lt --createingress
fission route create  --url /twitter/gt --function twitter-gt --name twitter-gt --createingress
kubectl port-forward service/router -n fission 9090:80
```






