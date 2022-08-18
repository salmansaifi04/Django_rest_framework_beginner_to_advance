# JWT (Json web token) Authorization - Simple JWT

## How to use Simple JWT

`pip install djangorestframework-simplejwt`

## GET Token

`http POST http://127.0.0.1:8000/gettoken/ username='user1' password='pass'`

## Verify Token

`http POST http://127.0.0.1:8000/verifytoken/ token="paste_Access_token_key"`

## Refresh Token

`http POST http://127.0.0.1:8000/refreshtoken/ token="paste_refresh_token_key"`

## How to install httpie

`pip install httpie`

## How to use Jwt through httpie

### GET Request

`http http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer paste_Access_tokon_key'`

### POST Request

`http -f POST http://127.0.0.1:8000/studentapi/ name=Salman roll=104 city=Noida 'Authorization:Bearer paste_Access_tokon_key'`


### PUT Request

`http PUT http://127.0.0.1:8000/studentapi/4/ name=Salman roll=105 city=Noida 'Authorization:Bearer paste_Access_tokon_key'`


### DELETE Request

`http DELETE http://127.0.0.1:8000/studentapi/4/ 'Authorization:Bearer paste_Access_tokon_key'`

