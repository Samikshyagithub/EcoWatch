import { useState } from "react";
import axios from 'axios';
import LoadingBar from "./loading";
import { BiCctv } from "react-icons/bi";

function FileWindow2() {
    const [url, setURL] = useState("");
    const [path, setPath] = useState("");
    const [success, setSuccess] = useState(0);
    const [processing, setProcessing] = useState(0);

    function handleUrlChange(event) {
        setURL(event.target.value);
    }

    function handleURLSubmit(event) {
        event.preventDefault();
        setSuccess(0);
        setProcessing(1);
        // Extract filename from the URL
        const filename = url.substring(url.lastIndexOf('/') + 1);
        axios.get(`http://127.0.0.1:5000/firetest/${filename}`)
            .then(response => {
                console.log(response.data);
                setProcessing(0);
                setSuccess(1);
                setPath(url); // Setting the path as the input URL
            })
            .catch(error => {
                console.error('Error:', error);
                setProcessing(0);
                setSuccess(0);
            });
    }

    return (
        <div className="flex-row items-center justify-start">
            <h1 className="w-full my-4 text-3xl font-bold text-center">Fire Detection Tool</h1>
            <div className="w-full px-10 my-10">
                <form className="flex justify-center">
                    <input type="text" id="small-input" className="p-4 w-[50rem] text-gray-900 outline-none rounded-full border-2 border-gray-300" placeholder="Enter video stream" onChange={handleUrlChange}></input>
                    <button onClick={handleURLSubmit} className="p-4 mx-5 text-white rounded-full bg-primary dark:bg-primary-dark"><BiCctv size={25} /></button>
                </form>
            </div>
            {success === 1 ? <p>Video successfully processed!</p> : null}
            {processing === 1 ? <LoadingBar /> : null}
        </div>
    );
}

export default FileWindow2;
