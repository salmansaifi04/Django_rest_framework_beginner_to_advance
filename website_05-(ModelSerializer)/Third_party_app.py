import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

## get the data
def get_data(id=None):
	data={}
	if id is not None:
		data = {'id':id}
	json_data = json.dumps(data)
	r = requests.get(url=URL, data=json_data)
	data = r.json()
	print(data)

# get_data(1)
get_data()

## post(create) the data
def post_data():
	# data={
	# 	'name':'Sanket',
	# 	'roll':199,
	# 	'city':'Delhi'
	# }

	# data={
	# 	'name':'Rohit',
	# 	'roll':199,
	# 	'city':'Ranchi'
	# }


	data={
		'name':'Rohan',
		'roll':199,
		'city':'Ranchi'
	}

	json_data = json.dumps(data)
	r = requests.post(url=URL, data=json_data)
	data = r.json()
	print(data)

# post_data()

## update(put/patch) the data
def update_data():
    ## partially update (patch)
	# data={
	# 	'id':4,
	# 	'name':'Shivam',
	# 	'city':'Delhi'
	# }

	## complete update (put)
	data={
		'id':4,
		'name':'Shivam',
		'roll':105,
		'city':'Delhi'
	}

	json_data = json.dumps(data)
	r = requests.put(url=URL, data=json_data)
	data = r.json()
	print(data)

# update_data()


## delete the data
def delete_data():
	data={'id':5}
	# data={'id':10}
	json_data = json.dumps(data)
	r = requests.delete(url=URL, data=json_data)
	data = r.json()
	print(data)

# delete_data()