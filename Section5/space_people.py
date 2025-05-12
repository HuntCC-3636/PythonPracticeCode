# to run requests module u need to run 'pip install requests'
import requests
                            #Site we are requesting from data
people = requests.get('http://api.open-notify.org/astros.json')
json = people.json()

#default print of entire json
print(json)

#header
print('The people currently in space are:')
#list for names from source but only people
for person in json['people']:
    print(person['name']) # -name is the key inside of people 



