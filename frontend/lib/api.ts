import axios from "axios";

const api = axios.create({
  baseURL: "https://supreme-spork-wrx7p7vx56qvfv5-8000.app.github.dev/"
});

export default api;