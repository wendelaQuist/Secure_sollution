import axios from "axios";
import apiUrl from "./constants";

const getResult = (taskPath) => {
    const maxTries = 3;
    const msInterval = 15 * 1000;
    let counter = 0;
    let intervalId;

    intervalId = setInterval(() => {
        fetchData();
    }, 0);

    const fetchData = () => {
        axios.get(`${apiUrl}/result/${taskPath}`).then(response => {
            if (response.status === 200) {
                return response.data;
            } else {
                counter++;
                if (counter > maxTries) {
                    clearInterval(intervalId);
                    return;
                }
                setTimeout(getResult, msInterval);
            }
        }).catch(error => {
            console.error(error);
        });
    }
}

export default getResult