import akeyless

import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_ID = os.getenv("AKEYLESS_ACCESS_ID")
ACCESS_KEY = os.getenv("AKEYLESS_ACCESS_KEY")

# using public API endpoint
configuration = akeyless.Configuration(
    host="https://api.akeyless.io"
)

api_client = akeyless.ApiClient(configuration)
api = akeyless.V2Api(api_client)

body = akeyless.Auth(access_id=ACCESS_ID, access_key=ACCESS_KEY)

res = api.auth(body)

token = res.token
print(token)

body = akeyless.GetSecretValue(names=['/SecretExtractor/static-secret-text-format'], token=token)
res = api.get_secret_value(body)
print("Static Secret: " + res['/SecretExtractor/static-secret-text-format'])

body = akeyless.GetDynamicSecretValue(name='/SecretExtractor/dynamic-secret-postgres', token=token)

res = api.dynamic_secret_get_value(body)
print(res['user'])
print("Dynamic Secret: " + (res['user']))
print("Dynamic Secret Password: " + (res['password']))
