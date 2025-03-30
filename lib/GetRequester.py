import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        return json.loads(self.get_response_body())
   
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

# Create an instance of GetRequester
requester = GetRequester(url)

# Fetch and print the parsed JSON data
print("\nParsed JSON:")
data = requester.load_json()
for person in data:
    print(f"Name: {person['name']}, Occupation: {person['occupation']}")
