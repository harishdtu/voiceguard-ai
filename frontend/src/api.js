import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
});

export const login = (data) =>
  API.post("/auth/login", data);

export const detectMedia = (file, token) =>
  API.post("/detect/media", file, {
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "multipart/form-data",
    },
  });
