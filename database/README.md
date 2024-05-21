# Database
This folder store the mapping of each index:
- sudo
- bom
- mastodon
- twitter
- epa
- asthma

The data are store in data folder as json format. Using json format will be easier for batch indexing.

With the tunneling connecting and port-forward to  9200:9200, run following command can create the index mapping:
```
python elastic.py
```