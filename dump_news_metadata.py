import requests
import time
import json


documents_file_name = "documents-dump-{}.json".format(time.strftime("%Y-%m-%dT%H:%M:%S"))

with open(documents_file_name, 'w') as documents_file:
    next_url = "https://alephapi.public-people.techforgood.org.za/api/2/documents"
    while next_url:
        response = requests.get(next_url)
        response.raise_for_status()
        response_obj = response.json()
        documents = response_obj['results']
        for document in documents:
            documents_file.write(json.dumps(document) + "\n")
        next_url = response_obj['next']
