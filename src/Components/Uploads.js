
import React, { Component, useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';
import { useCookie } from 'react-cookie';
import FoodInfo from './FoodInfo';
import {
S3Client
} from "@aws-sdk/client-s3";
import { CognitoIdentityClient } from "@aws-sdk/client-cognito-identity";
import * as AmazonCognitoIdentity from 'amazon-cognito-identity-js';
import { fromCognitoIdentityPool } from "@aws-sdk/credential-provider-cognito-identity";

import { API, Storage  } from 'aws-amplify';
import { AWS } from 'aws-sdk';

const UserFileUpload = ({ image }) => {
  let [uploadFile, setUploadFile] = useState("");

  var reader = new FileReader();

  reader.readAsDataURL(image);

  reader.onloadend = function (e) {
      setUploadFile(reader.result);
    }.bind(this);
  return (
    <div><img src={uploadFile} alt={image.name} /></div>);
};

const FoodName = ({foodName}) => {
  return (
    <div>
      <p>
        FoodName: {foodName}
      </p>
    </div>
  )
}

export default function Uploads() {
  let [file, setFile] = useState("");
  let [foodName, setFoodName] = useState("");
  const [recognize, setRecognize] = useState(null);
  const fetchRecognize = async () => {
    const apiData = await API.get('fastFoodRecognize', '/recognize');
    console.log(apiData);
    setRecognize(apiData.Labels[0].Name);
    setFoodName(apiData.Labels[0].Name);
  }
  useEffect(() => {
    // fetchRecognize();
  }, []);



  let handleFileUpload = async (event) => {
    let fileUpload = event.target.files[0];
    setFile(fileUpload);

    try {

      await Storage.put("userUpload.png", fileUpload, {
        contentType: 'image/png' // contentType is optional

      });
      await fetchRecognize();

    } catch (err) {
      console.log('Error uploading file: ', err);
    }

  }


  let onUploadCompleted = () => {
  var reader = new FileReader();
  var url = reader.readAsDataURL(file);
  }


  return(
    <div>
      <input type="file" onChange={handleFileUpload}/>
      {file && <UserFileUpload image={file} />}
      {foodName && <FoodName foodName={foodName} /> }

    </div>
  )

};
