import axios from 'axios';

// Set default base URL for Axios requests
axios.defaults.baseURL = 'http://127.0.0.1:5000';

// Add CORS headers to all Axios requests
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
axios.defaults.headers.common['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept';

export default axios;
