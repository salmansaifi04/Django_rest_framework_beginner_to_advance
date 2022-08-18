# Generate Token using Signal and How to use this token
1. **You need to create a user using admin pannel then Token automatically create**
2. **Then use cmd**


## How to install httpie

`pip install httpie`

## How to use generate token through httpie

### GET Request

`http http://127.0.0.1:8000/studentapi/ 'Authorization:Token key_name'`

### POST Request

`http -f POST http://127.0.0.1:8000/studentapi/ name=Salman roll=104 city=Noida 'Authorization:Token key_name'`


### PUT Request

`http PUT http://127.0.0.1:8000/studentapi/4/ name=Salman roll=105 city=Noida 'Authorization:Token key_name'`


### DELETE Request

`http DELETE http://127.0.0.1:8000/studentapi/4/ 'Authorization:Token key_name'`

