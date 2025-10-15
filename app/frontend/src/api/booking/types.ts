import type { TService } from "../service/types"

type TBookingOfferedService = {
  id: number
  caretaker_id: string
  service: TService
}

type TBookingPet = {
  id: number
  name: string
  species: string
  breed: string
  age: number
  health: string
  preferences: string
  owner_id: string
}

export type TBooking = {
  id: number
  status: string
  date: string
  offered_service: TBookingOfferedService
  pet: TBookingPet
}

export type TBookings = TBooking[]

export type TAddBookingRequest = {
  date: string
  offered_service_id: number
  pet_id: number
}
