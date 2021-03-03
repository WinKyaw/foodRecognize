from flask import Flask,request,redirect,url_for
from bson import ObjectId
from pymongo import MongoClient
import os
import json
import boto3
import io
from botocore.utils import fix_s3_host
from PIL import Image

app = Flask(__name__)
title = "TODO sample application with Flask and MongoDB"
heading = "TODO Reminder with Flask and MongoDB"
sess= boto3.session(region_name="us-west-1")

client = MongoClient("mongodb://localhost:27017") #host uri
db = client.foods
users = db.users


def redirect_url():
    return request.args.get('next') or \
           request.referrer or \
           url_for('index')

@app.route("/users", methods=['GET'])
def users ():
    # users = users.find()
    return "string"

@app.route("/recognize", methods=['GET'])
def recognize():
    boto3_client = sess.client('rekognition')
    image = Image.open('ls.jpg')
    stream = io.BytesIO()
    image.save(stream,format="JPEG")
    image_binary = stream.getvalue()
    response = boto3_client.detect_text(
        Image={'Bytes':image_binary}
        )
    print(response)
    # client = boto3.client('rekognition')
    #
    # {
    #   "Image": {
    #     "Bytes": blob,
    #     "S3Object": {
    #       "Bucket": "string",
    #        "Name": "string",
    #        "Version": "string"
    #      }
    #   }
    # }
    #
    # image = Image.open(local)
    #
    # stream = io.BytesIO()
    # image.save(stream,format="JPEG")
    # image_binary = stream.getvalue()
    #
    # response = client.detect_labels(
    #     Image={'Bytes':image_binary}
    #     )


    # client = boto3.client("rekognition")
    # s3 = boto3.client("s3")
    # fileObj = s3.get_object(Bucket = "foodrecognition", Key="ls.jpg")
    # file_content = fileObj["Body"].read()
    # response = client.detect_labels(Image = {"S3Object": {"Bucket": "foodrecognition", "Name": "download.jpg"}}, MaxLabels=3, MinConfidence=70)
    # print(response)
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps(response)
    # }
    return "TEST"

@app.route("/completed")
def completed ():
    #Display the Completed Tasks
    todos_l = todos.find({"done":"yes"})
    a3="active"
    return render_template('index.html',a3=a3,todos=todos_l,t=title,h=heading)

@app.route("/done")
def done ():
    #Done-or-not ICON
    id=request.values.get("_id")
    task=todos.find({"_id":ObjectId(id)})
    if(task[0]["done"]=="yes"):
        todos.update({"_id":ObjectId(id)}, {"$set": {"done":"no"}})
    else:
        todos.update({"_id":ObjectId(id)}, {"$set": {"done":"yes"}})
    redir=redirect_url()

    return redirect(redir)

@app.route("/action", methods=['POST'])
def action ():
    #Adding a Task
    name=request.values.get("name")
    desc=request.values.get("desc")
    date=request.values.get("date")
    pr=request.values.get("pr")
    todos.insert({ "name":name, "desc":desc, "date":date, "pr":pr, "done":"no"})
    return redirect("/list")

@app.route("/remove")
def remove ():
    #Deleting a Task with various references
    key=request.values.get("_id")
    todos.remove({"_id":ObjectId(key)})
    return redirect("/")

@app.route("/update")
def update ():
    id=request.values.get("_id")
    task=todos.find({"_id":ObjectId(id)})
    return render_template('update.html',tasks=task,h=heading,t=title)

@app.route("/action3", methods=['POST'])
def action3 ():
    #Updating a Task with various references
    name=request.values.get("name")
    desc=request.values.get("desc")
    date=request.values.get("date")
    pr=request.values.get("pr")
    id=request.values.get("_id")
    todos.update({"_id":ObjectId(id)}, {'$set':{ "name":name, "desc":desc, "date":date, "pr":pr }})
    return redirect("/")

@app.route("/search", methods=['GET'])
def search():
    #Searching a Task with various references

    key=request.values.get("key")
    refer=request.values.get("refer")
    if(key=="_id"):
        todos_l = todos.find({refer:ObjectId(key)})
    else:
        todos_l = todos.find({refer:key})
    return render_template('searchlist.html',todos=todos_l,t=title,h=heading)

if __name__ == "__main__":

    app.run()
