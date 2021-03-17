import json
import boto3
# from usda import UsdaClient
import noms
import requests
from requests.auth import HTTPBasicAuth

def handler(event, context):
    client = boto3.client("rekognition")
    s3 = boto3.client("s3")
    fileObj = s3.get_object(Bucket = "foodrecognition", Key="image 5.jpg")
    file_content = fileObj["Body"].read()
    # response = client.detect_labels(Image = {"S3Object": {"Bucket": "foodrecognition", "Name": "image 5.jpg"}}, MaxLabels=3, MinConfidence=70)
    response = client.detect_labels(Image = {"S3Object": {"Bucket": "fastfood153439-dev", "Name": "public/userUpload.png"}}, MaxLabels=5, MinConfidence=70)
    # print(response)
    return {
        'statusCode': 200,
        'body': json.dumps(response),
        'headers': {
            'Content-Type' : 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

# def nutrientHelper(foodName="Chedder Cheese"):
#
#     return ""
#
# if __name__ == "__main__":
#     print('testing')
#     response = handler("null", "null")
#     responseBody = json.loads(response['body'])
#     foodName = responseBody['Labels'][0]['Name']
#     foodName = "coffee"
#     try:
#         # usdaResult =  usda.search_foods("coffee", 1)
#         # print (json.dumps(usdaResult))
#         # nomsResult = nomsClient.search_query("Raw")
#         # print(nomsResult)
#         url = "https://api.nal.usda.gov/fdc/v1/foods/search?"+ "api_key="+API_KEY+"&query=Cheddar%20Cheese"
#         headers = {"Accept": "application/json"}
#         # auth = HTTPBasicAuth('api_key', API_KEY)
#         response = requests.get(url=url)
#         # response = json.dumps(response)
#         print(response)
#     except Exception as e:
#         print("error: {}", e)
#
#     # print(json.loads(nomsResult))
