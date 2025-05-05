# to run requests module u need to run 'pip install requests'
import requests
                            #Site we are requesting from data
response = requests.get('http://api.open-notify.porg/astros.json')
json = response.json()

#header
print('The people currently in space are:')
#list for names from source but only people
for person in json['person']:
    print(person['name'])



