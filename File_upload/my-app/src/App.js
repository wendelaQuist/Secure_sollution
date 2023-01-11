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
    })

  };

  return <div className="App">
    <input type="file" onChange={(event) => {
      setFileUpload(event.target.files[0])
    }}
    />
    <button onClick={uploadFile}> Upload File </button>
    </div>
}

export default App;
