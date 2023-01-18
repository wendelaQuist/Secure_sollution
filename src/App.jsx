import { useState } from "react";
import axios from 'axios';
import apiUrl from "./constants";
import getResult from "./lib.js";
import './App.css';

const App = () => {
	const [pythonFile, setPythonFile] = useState();
	const [argsFile, setArgsFile] = useState();

	const uploadFile = (e) => {
		e.preventDefault();

		// callback hell!
		axios.post(`${apiUrl}/upload/${pythonFile.name}`, pythonFile).then(response => {
			if (response.status !== 200 ) {
				console.error("failed to load python file: " + response)
			}

			console.log("Python path: " + response.data);
			const taskName = response.data;

			axios.post(`${apiUrl}/upload/${taskName}/args`, argsFile).then(response => {
				if (response.status !== 200 ) {
					console.error("failed to load python file: " + response)
				}
	
				axios.post(`${apiUrl}/run/${taskName}`).then(response => {
					if (response.status !== 200 ) {
						console.error("failed to run task: " + response)
					}
		
					console.log("Result: " + response.data);
				})
			})
		})
	}

	const handlePythonFileChange = (e) => {
		setPythonFile(e.target.files[0]);
	}

	const handleArgsFileChange = (e) => {
		setArgsFile(e.target.files[0]);
	}

	return (
		<div className="App">
			<head>
			<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"/>
			</head>
			<div className="body">
				<div className="drag-area">
				<div class="icon"><i class="fas fa-cloud-upload-alt"></i></div>
			<header><h1>File Upload</h1></header>
			<form method="post" encType="multipart/form-data">
				<input type="file" name="python-file" onChange={handlePythonFileChange}/>
				<input type="file" name="args-file" onChange={handleArgsFileChange}/>
				<input type="submit" value="Upload" onClick={uploadFile} />
			</form>
				</div>
			</div>
		</div>
	);
}

export default App;
