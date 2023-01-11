import './App.css';
import { useState } from "react";
import { storage } from "./firebase";
import { ref, uploadBytes } from "firebase/storage";
import { v4 } from "uuid";

function App() {
  const [fileUpload, setFileUpload] = useState(null);
  const uploadFile = () => {
    if (fileUpload == null) return;
    const fileRef = ref(storage, `uploads/${fileUpload.name + v4()}`);
    uploadBytes(fileRef, fileUpload).then(() => {
      alert("File good to go");
    })//return sollution???

  };

  return <div className="App">
    <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"/>
    <link rel="stylesheet" href="./index.css" />
    </head>
    <body>
    <div class="drag-area">
    <div class="icon"><i class="fas fa-cloud-upload-alt"></i></div>
    <header><h1>File Upload</h1></header>
    <input type="file" onChange={(event) => {
      setFileUpload(event.target.files[0])
    }}
    />
    <button onClick={uploadFile}> Upload File </button>
    </div>
    </body>
    </div>
}

export default App;