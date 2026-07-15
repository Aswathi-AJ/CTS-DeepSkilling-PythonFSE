import axios from 'axios';

// Step 138: Configure single Axios instance with baseURL, headers, and timeout
const apiClient = axios.create({
  baseURL: 'https://jsonplaceholder.typicode.com',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
});

// Step 141: Request interceptor attaching Authorization mock token
apiClient.interceptors.request.use(
  (config) => {
    const mockAuthToken = 'Bearer mock_student_portal_jwt_token_2026';
    config.headers.Authorization = mockAuthToken;
    console.log(`[API Client Request] Outgoing ${config.method.toUpperCase()} to ${config.url}`);
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Step 140: Response interceptor unwrapping data & standardizing errors
apiClient.interceptors.response.use(
  (response) => {
    // (a) Returns response.data directly so callers don't need .data wrapper
    return response.data;
  },
  (error) => {
    // (b) Catches errors and throws standardised Error object with message and statusCode
    const statusCode = error.response ? error.response.status : 500;
    const message = error.response
      ? `API Request failed with status ${statusCode}`
      : 'Network Connection Error. Please check your network connection.';

    const customError = new Error(message);
    customError.statusCode = statusCode;
    customError.originalError = error;

    return Promise.reject(customError);
  }
);

export default apiClient;
