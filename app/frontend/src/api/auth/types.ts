export type LoginProps = {
  email: string
  password: string
}

export type LoginResponse = {
  name: string
}

export type SignUpProps = {
  name: string
  email: string
  password: string
  dob: string // Will be filled with placeholder values for now
  gender: "male" | "female" | "others" // Will be filled with placeholder values for now
}

export type SignUpResponse = {
  // Backend returns 201 status with no body for register endpoint
}
