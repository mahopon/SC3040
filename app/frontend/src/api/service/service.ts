import { http } from "../client"
import { API } from "../endpoints"
import type { TServiceListResponse } from "./types"

export const fetchServiceList = async (): Promise<TServiceListResponse> => {
  try {
    const res = await http.get<TServiceListResponse>(API.SERVICE.GET)
    console.log("GET service list: ", res)
    return res.data
  } catch (err) {
    console.log(`GET service list: ${err}`)
    throw new Error("Failed to fetch list of services")
  }
}
