# Simple Integration for Hubspot API

Created by [@chelo154](www.github.com/chelo154)

## Features

- Oauth Flow for Hubspot
- Deal API call from Husbpot
- Store user data and Deals in MongoDB Atlas

## Tech Stack

This project was developed using

- Flask
- Mongoengine (ORM for Mongosql)
- Python 3.8.5

## Considerations

### Install

To run the project you have to use pip

`pip install -r requirements.txt`

### Ngrok

For complete OAUTH authentication flow , use [ngrok](https://ngrok.com/) for https tunneling 
from localhost.

Also you have to change the `adapters/oauth/oauth_hubspot_adapter` with the redirect_url
given by ngrok

```python
    def __init__(self):
        self.url = ''
        self.tokens_url = ''
        self.client_id = ''
        self.scope = ''
        self.redirect_uri = 'PUT HERE THE NGROK LINK'
        self.client_secret = ''
```

### MongoDB

The data is stored in a personal database in mongoDBAtlas

## API

- `/api/oauth/authorization: GET`
This will redirect to Hubspot OAUTH

- `/api/oauth/callback : GET`
This is the redirect URI called by Hubspot

    Response in this case will be:
    
    ```json      
      {
        "code": The user code returned by Hubspot,
        "username": The username returned by Hubspot,
         "access_token": The access token,
        "refresh_token": The refresh token
       } 
    ```

- `api/deals : GET`

This is the endpoint for get the Deals from the user

Request Body 
```json
{
  "username" : Your Hubspot username
}
```
Response 
```json
  [
    {
        "id": 4712527724,
        "name": "Example Deal",
        "stage": "closedwon",
        "close_date": "1617218939799",
        "amount": 250.0,
        "deal_type": "newbusiness",
        "user": "chelo154@gmail.com"
    },
    {
        "id": 4719692685,
        "name": "TestDeal",
        "stage": "qualifiedtobuy",
        "close_date": "1617210385982",
        "amount": 500.0,
        "deal_type": "existingbusiness",
        "user": "chelo154@gmail.com"
    }
]
```