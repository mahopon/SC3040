import { http } from "../client"
import { API } from "../endpoints"
import type { ServiceListResponse } from "./types"

export const fetchServiceList = async (): Promise<ServiceListResponse> => {
  try {
    const res = await http.get<ServiceListResponse>(API.SERVICE.GET)
    console.log("GET service list: ", res)
    return res.data
  } catch (err) {
    console.log(`GET service list: ${err}`)
    throw new Error("Failed to fetch list of services")
  }
}
