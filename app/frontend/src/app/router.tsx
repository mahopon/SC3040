import { Home, Login, Onboarding, Profile, SignUp } from "@/pages"
import { createBrowserRouter } from "react-router-dom"

export const router = createBrowserRouter([
  { path: "/", element: <Home /> },
  { path: "/login", element: <Login /> },
  { path: "/signup", element: <SignUp /> },
  { path: "/onboarding", element: <Onboarding /> },
  { path: "/profile", element: <Profile /> },
])
