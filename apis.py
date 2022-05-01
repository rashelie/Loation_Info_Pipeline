import pandas as pd
import requests
import json
from operator import itemgetter

# make a call to the API and parse to json file
link = "https://api.open-meteo.com/v1/forecast?latitude=50.57&longitude=-2.45&hourly=windgusts_10m&windspeed_unit=kn&timezone=Europe%2FBerlin"
r = requests.get(link)
data = r.json()


# Iterating through the json
# list
def nested_dict_pairs_iterator(dict_obj):
    ''' This function accepts a nested dictionary as argument
        and iterate over all values of nested dictionaries
    '''
    # Iterate over all key-value pairs of dict argument
    for key, value in dict_obj.items():
        # Check if value is of dict type
        if isinstance(value, dict):
            # If value is dict then iterate over all its values
            for pair in nested_dict_pairs_iterator(value):
                yield (key, *pair)
        else:
            # If value is not dict type then yield the value
            yield (key, value)


for pair in nested_dict_pairs_iterator(data):
    print(pair)

# Closing file
r.close()
