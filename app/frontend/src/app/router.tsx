import { Booking, Bookings, Home, Login, Onboarding, Profile, ServiceBrowsing, ServiceDetail, SignUp } from "@/pages"
import { createBrowserRouter } from "react-router-dom"

export const router = createBrowserRouter([
  { path: "/", element: <Home /> },
  { path: "/login", element: <Login /> },
  { path: "/signup", element: <SignUp /> },
  { path: "/onboarding", element: <Onboarding /> },
  { path: "/profile", element: <Profile /> },
  { path: "/services", element: <ServiceBrowsing /> },
  { path: "/service/:id", element: <ServiceDetail /> },
  { path: "/booking/:id", element: <Booking /> },
  { path: "/bookings", element: <Bookings /> },
])
