import { baseURL, http } from "../client"
import { API } from "../endpoints"
import type {
  AuthenticatedResponse,
  LoginProps,
  LoginResponse,
  LogoutResponse,
  SignUpProps,
  SignUpResponse,
} from "./types"

export const isAuthenticated = async (): Promise<AuthenticatedResponse> => {
  const res = await http.get(API.PROFILE.GET)
  if (res.status === 200) {
    return { authenticated: true }
  } else {
    return { authenticated: false }
  }
}

export const login = async (data: LoginProps): Promise<LoginResponse> => {
  try {
    const res = await http.post<LoginResponse>(API.AUTH.LOGIN, data)
    console.log("POST login: ", res)
    return res.data
  } catch (err) {
    console.log(`POST login: ${err}`)
    throw new Error("Invalid credentials")
  }
}

export const signup = async (data: SignUpProps): Promise<SignUpResponse> => {
  try {
    const res = await http.post<SignUpResponse>(API.AUTH.SIGNUP, data)
    return res.data
  } catch (err: any) {
    console.log(`signup: ${err}`)
    console.log("Full error:", err.response?.data) // Better debugging

    // Handle different types of signup errors
    if (err.response?.status === 409) {
      throw new Error("An account with this email already exists")
    }
    if (err.response?.status === 400) {
      // Extract specific validation errors from backend
      const errorMessage =
        err.response?.data?.detail || "Invalid input data. Please check your information."
      throw new Error(errorMessage)
    }
    if (err.response?.status === 422) {
      // Validation errors from Pydantic
      const errors = err.response?.data?.detail
      if (Array.isArray(errors) && errors.length > 0) {
        const firstError = errors[0]
        throw new Error(`${firstError.loc?.[1] || "Field"}: ${firstError.msg}`)
      }
      throw new Error("Validation error. Please check your input.")
    }

    // Network connection errors
    if (!err.response) {
      throw new Error("Cannot connect to server. Please check if the backend is running.")
    }

    throw new Error("Failed to create account. Please try again.")
  }
}

export const loginGoogle = () => {
  const url = `${baseURL}${API.AUTH.GOOGLE_LOGIN}`
  window.location.href = url
}

export const logout = async (): Promise<LogoutResponse> => {
  try {
    const res = await http.post(API.AUTH.LOGOUT)
    console.log("POST logout: ", res)
    return res.data
  } catch (err) {
    console.log(`POST logout: ${err}`)
    throw new Error("Logout failed")
  }
}
