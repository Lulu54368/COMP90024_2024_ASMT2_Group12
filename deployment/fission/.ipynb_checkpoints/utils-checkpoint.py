# Team 12
# Meilun Yao   1076213
# Yingyi Luan 1179002
# Yuntao Lu 1166487
# Jiayi Xu 1165986
# Zheyuan Wu 1166034
HEALTH_URL="'https://elasticsearch-master.elastic.svc.cluster.local/_cluster/health'"
MASTODON_URL = "'https://elasticsearch-master.elastic.svc.cluster.local:9200/mastodon/_search'"
MASTODON_COUNT_URL="'https://elasticsearch-master.elastic.svc.cluster.local:9200/mastodon/_count'"
HEADERS = {
    "kbn-xsrf": "reporting",
    "Content-Type": "application/json",
    "Authorization": "Basic ZWxhc3RpYzplbGFzdGlj"
}
AUTH = ('elastic', 'elastic')

MASTODON_REQ_BODY_GT = {
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