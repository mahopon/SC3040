import { createBrowserRouter } from "react-router-dom"

import Home from "@/pages/Home"
import Login from "@/pages/Login"
import SignUp from "@/pages/SignUp"
import Onboarding from "@/pages/Onboarding"

export const router = createBrowserRouter([
  { path: "/", element: <Home /> },
  { path: "/login", element: <Login /> },
  { path: "/signup", element: <SignUp /> },
  { path: "/onboarding", element: <Onboarding /> },
])
