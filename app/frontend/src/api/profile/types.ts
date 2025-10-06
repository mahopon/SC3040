export type ProfileResponse = {
  first_name: string
  last_name: string
  contact_num: string
  dob: string
  address: string
  gender: string
  type: "caretaker" | "owner"
  profile_picture?: string
}

export type ProfilePictureResponse = {
  profilePicture: string
}
