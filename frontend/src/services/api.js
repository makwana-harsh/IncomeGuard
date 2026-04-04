import axios from "axios";

const API = axios.create({
    baseURL: "http://127.0.0.1:8000"
});

export const registerUser = (data) => API.post("/auth/register", data);
export const loginUser = (data) => API.post("/auth/login", data);
export const createPolicy = (data) => API.post("/policy/create-policy", data);
export const addSchedule = (data) => API.post("/schedule/add", data);
export const getClaims = (user_id) => API.get(`/claims/${user_id}`);
export const getPayments = (user_id) => API.get(`/payments/${user_id}`);

export default API;