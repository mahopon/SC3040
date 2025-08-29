import axios from "axios"

const baseURL = import.meta.env.VITE_API_URL

export const userAPI = axios.create({
  baseURL: `${baseURL}/users`,
})
