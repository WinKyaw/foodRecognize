import json
import boto3
import io
from PIL import Image


def lambda_handler(event, context):
    client = boto3.client("rekognition")
    s3 = boto3.client("s3")
    # fileObj = s3.get_object(Bucket = "fastfood153439-dev", Key="image 5.jpg")
    # file_content = fileObj["Body"].read()
    response = client.detect_labels(Image = {"S3Object": {"Bucket": "fastfood153439-dev", "Name": "public/userUpload.png"}}, MaxLabels=3, MinConfidence=70)
    # response = client.detect_labels(Image = {"S3Object": {"Bucket": "foodrecognition", "Name": "image 5.jpg"}}, MaxLabels=3, MinConfidence=70)
    # response = client.detect_labels(Image)
    #
    # image = Image.open(image_path)
    #
    # stream = io.BytesIO()
    # image.save(stream,format="JPEG")
    # image_binary = stream.getvalue()
    #
    # response = client.detect_labels(Image={'Bytes':image_binary})
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps(response),
        'headers': {
            'Content-Type' : 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
    }

if __name__ == "__main__":
    print('testing')
    lambda_handler("null", "null")
