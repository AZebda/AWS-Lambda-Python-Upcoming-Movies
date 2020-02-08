from botocore.vendored import requests
import os

def lambda_handler(event, context):
    upcompingMoviesList = requests.get(os.environ['MOVIES_ENDPOINT'])
    return upcompingMoviesList.json()