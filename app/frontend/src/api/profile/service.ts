import { http } from "../client"
import { API } from "../endpoints"
import type { ProfilePictureResponse, ProfileResponse } from "./types"

export const fetchProfile = async (): Promise<ProfileResponse> => {
  try {
    const res = await http.get<ProfileResponse>(API.PROFILE.GET)
    console.log("GET profile: ", res)
    return res.data
  } catch (err) {
    console.log(`GET profile: ${err}`)
    throw new Error("Failed to fetch profile")
  }
}

export const fetchProfilePicture = async (): Promise<ProfilePictureResponse> => {
  try {
    const res = await http.get<ProfileResponse>(API.PROFILE.GET)
    console.log("GET profile: ", res)
    return { profilePicture: res.data.profile_picture ?? "" }
  } catch (err) {
    console.log(`GET profile: ${err}`)
    throw new Error("Failed to fetch profile")
  }
}

export const fetchProfileById = async (userId: string) => {
  try {
    const res = await http.get(`/profile/${userId}`)
    console.log("GET profile by ID: ", res)
    return res.data
  } catch (err) {
    console.log(`GET profile by ID: ${err}`)
    throw new Error("Failed to fetch profile by ID")
  }
}
