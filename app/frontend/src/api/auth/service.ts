import { http } from "../client"
import { API } from "../endpoints"
import type { LoginProps, LoginResponse } from "./types"

export const login = async (data: LoginProps): Promise<LoginResponse> => {
  try {
    const res = await http.post<LoginResponse>(API.AUTH.LOGIN, data)
    return res.data
  } catch (err) {
    throw new Error("Invalid credentials")
  }
}
