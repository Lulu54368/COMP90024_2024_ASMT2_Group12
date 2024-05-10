
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


