
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
import os

from settings import configurations

INDEX_NAME=os.environ["INDEX_NAME"]

def main():
    es = Elasticsearch(
            "elasticsearch:9200",
            http_auth=["elastic", "changeme"],
        )

    client = IndicesClient(es)
    try:
        client.create(index=INDEX_NAME, body=configurations)
    except:
        pass


main()