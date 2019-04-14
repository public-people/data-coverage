import requests
import time
import csv


documents_file_name = "documents-dump-{}.csv".format(time.strftime("%Y-%m-%dT%H%M%S"))

with open(documents_file_name, 'w') as documents_file:
    fieldnames = ['collection_id', 'collection_name', 'document_id', 'source_url', 'publication_date']
    writer = csv.DictWriter(documents_file, fieldnames=fieldnames)
    writer.writeheader()

    next_url = "https://alephapi.public-people.techforgood.org.za/api/2/documents"
    while next_url:
        print(next_url)
        response = requests.get(next_url)
        response.raise_for_status()
        response_obj = response.json()
        documents = response_obj['results']
        for document in documents:
            row_dict = {
                'collection_id': document['collection']['id'],
                'collection_name': document['collection']['label'],
                'document_id': document['id'],
                'source_url': document['source_url'],
                'publication_date': document['published_at'][:10]
            }
            writer.writerow(row_dict)
        documents_file.flush()
        next_url = response_obj['next']
