
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






