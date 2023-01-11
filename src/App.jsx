import './App.css';
import { useState } from "react";
import axios from 'axios';
import { apiUrl } from './constants';

const App = () => {
	const [file, setFile] = useState();

	const uploadFile = (e) => {
		e.preventDefault();

		let formData = new FormData();
		formData.append('file', file);

		axios.post(apiUrl + "/" + file.name, formData).then(response => {
			console.log(response.data);
		})
	}

	const handleFileChange = (e) => {
		setFile(e.target.files[0]);
	}

	return (
		<div className="App">
			{/* <!-- File upload form --> */}
			<div class="icon"><i class="fas fa-cloud-upload-alt"></i></div>
			<header><h1>File Upload</h1></header>
			<form method="post" encType="multipart/form-data">
				<input type="file" name="file" onChange={handleFileChange}/>
				<input type="submit" value="Upload" onClick={uploadFile} />
			</form>
		</div>
	);
}

export default App;