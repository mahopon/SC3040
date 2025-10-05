export type OnboardingStatus = {
  onboarded: boolean
}

export type ProfileOnboardRequest = {
  firstName: string
  lastName: string
  dateOfBirth: string
  gender: string
  phone: string
  address: string
  type: "owner" | "caretaker"
  yearsOfExperience?: number
}

export type ProfileOnboardResponse = {}

export type PetOnboardRequest = {
  name: string
  species: string
  breed: string
  age: number
  health: string
  preferences: string
}

export type PetOnboardResponse = {}

export type ServiceOnboardRequest = {
  serviceId: number
  rate: number
  day: number[]
}[]

export type ServiceOnboardResponse = {}

export type CompleteOnboardResponse = {}
