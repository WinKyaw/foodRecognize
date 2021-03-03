
import React, { Component, useState } from 'react';
import { Button } from 'react-bootstrap';
import { useCookie } from 'react-cookie';


const ImageThumb = ({ image }) => {
  let [uploadFile, setUploadFile] = useState("");
  var reader = new FileReader();
  var url = reader.readAsDataURL(image);
  reader.onloadend = function (e) {
      setUploadFile(reader.result);
    }.bind(this);

  return <img src={uploadFile} alt={image.name} />;
};

export default function Uploads() {
    let [file, setFile] = useState("");



  let handleFileUpload = (event) => {
    let fileUpload = event.target.files[0];
    setFile(fileUpload);

  }

  let onUploadCompleted = () => {
    var reader = new FileReader();
    var url = reader.readAsDataURL(file);
  }


    return(
      <div>
        <input type="file" onChange={handleFileUpload}/>
        <p>Filename: {file.name}</p>
        <p>File type: {file.type}</p>
        <p>File size: {file.size} bytes</p>
        {file && <ImageThumb image={file} />}

      </div>
    )

};
