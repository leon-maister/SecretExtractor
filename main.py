#  Note: the apy-key is kept in .env file, but this file is not uploaded to github and not part docker file
#  for this purpose, the .env file should be uploaded to the machine where docker will run and please run the
#  command below:
# docker run --rm --env-file .env leonmaister/secret-extractor:1.0.0
# to build: docker docker build . -t leonmaister/secret-extractor:1.0.0
# #to push docker:
# docker push leonmaister/secret-extractor:1.0.0

import akeyless

import os
# from dotenv import load_dotenv
from dotenv import load_dotenv, find_dotenv

if os.path.isfile(".env"):
    path = find_dotenv()
    load_dotenv(".env")


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

print("Dynamic Secret Name: " + (res['user']))
print("Dynamic Secret Password: " + (res['password']))

