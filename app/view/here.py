import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

URL = "https://geocode.search.hereapi.com/v1/geocode"
location = input("Enter the location here: ") #taking user input
api_key = 'ao5DPDJ3gGJCMBY8-Rwg_7FJBqRo4iAlKRtHAGl1hxY' # Acquire from developer.here.com
PARAMS = {'apikey':api_key,'q':location} 

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
data = r.json()

position = data['items'][0]['position']

print(position)