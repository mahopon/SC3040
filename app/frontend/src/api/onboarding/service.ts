import { http } from "../client"
import { API } from "../endpoints"
import type {
  OnboardingStatus,
  PetOnboardRequest,
  ProfileOnboardRequest,
  ServiceOnboardRequest,
} from "./types"

export const fetchOnboardingStatus = async (): Promise<OnboardingStatus> => {
  try {
    const res = await http.get<OnboardingStatus>(API.ONBOARDING.STATUS)
    console.log("GET onboarding status: ", res)
    return res.data
  } catch (err) {
    console.log(`GET onboarding status: ${err}`)
    throw new Error("Failed to fetch onboarding status")
  }
}

export const onboardProfile = async (data: ProfileOnboardRequest): Promise<void> => {
  try {
    const res = await http.post<void>(API.ONBOARDING.PROFILE, {
      first_name: data.firstName,
      last_name: data.lastName,
      dob: data.dateOfBirth,
      gender: data.gender,
      contact_num: data.phone,
      address: data.address,
      type: data.type,
      yoe: data.yearsOfExperience ?? 0,
    })
    console.log("POST profile onboard: ", res)
    return res.data
  } catch (err) {
    console.log(`POST profile onboard: ${err}`)
    throw new Error("Failed to onboard profile")
  }
}

export const onboardPet = async (data: PetOnboardRequest): Promise<void> => {
  try {
    const res = await http.post<void>(API.ONBOARDING.PET, data)
    console.log("POST pet onboard: ", res)
    return res.data
  } catch (err) {
    console.log(`POST pet onboard: ${err}`)
    throw new Error("Failed to onboard pet")
  }
}

export const onboardService = async (data: ServiceOnboardRequest): Promise<void> => {
  try {
    const res = await http.post<void>(
      API.ONBOARDING.SERVICE,
      data.map(({ serviceId, rate, day }) => ({
        service_id: serviceId,
        rate,
        day: day.map((day) => Number(day)),
      })),
    )
    console.log("POST service onboard: ", res)
    return res.data
  } catch (err) {
    console.log(`POST service onboard: ${err}`)
    throw new Error("Failed to onboard service")
  }
}

export const onboardComplete = async (): Promise<void> => {
  try {
    const res = await http.post<void>(API.ONBOARDING.COMPLETE)
    console.log("POST complete onboard: ", res)
    return res.data
  } catch (err) {
    console.log("POST complete onboard: ", err)
    throw new Error("Failed to complete onboarding")
  }
}
