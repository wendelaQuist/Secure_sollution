import { initializeApp } from "firebase/app";
import { getStorage } from 'firebase/storage';

const firebaseConfig = {
  apiKey: "AIzaSyA2khZFeTYemDQNBfDjtEig0UOjzD3xH7A",
  authDomain: "file-upload-e2cb5.firebaseapp.com",
  projectId: "file-upload-e2cb5",
  storageBucket: "file-upload-e2cb5.appspot.com",
  messagingSenderId: "135572500800",
  appId: "1:135572500800:web:7f573a7daff23673894aa5"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const storage = getStorage(app);