import { Link, useNavigate } from "react-router-dom"
import AppLogo from "./AppLogo"
import { useEffect, useState } from "react"
import { AuthAPI, ProfileAPI } from "@/api"
import { userPlaceholderUrl } from "@/assets"

const Navbar = () => {
  const navigate = useNavigate()
  const [profilePicture, setProfilePicture] = useState<string>("")

  const handleLogout = () => {
    AuthAPI.logout().then(() => navigate("/login", { replace: true }))
  }

  useEffect(() => {
    ProfileAPI.fetchProfilePicture()
      .then(({ profilePicture }) => setProfilePicture(profilePicture))
      .catch(() => navigate("/login", { replace: true }))
  }, [])

  return (
    <nav className="w-full shadow-md flex items-center justify-between px-8 py-5">
      <AppLogo />

      <div className="flex items-center gap-10">
        <Link to="/" className="font-medium hover:underline">
          Dashboard
        </Link>
        <Link to="/bookings" className="font-medium hover:underline">
          Bookings
        </Link>

        <div className="relative group">
          <button className="h-10 w-10 hover:cursor-pointer" aria-label="User profile">
            <img
              src={profilePicture || userPlaceholderUrl}
              alt="Profile"
              className="h-full w-full object-cover rounded-full"
            />
          </button>

          <div className="absolute right-0 z-10 hidden bg-grey-200 group-hover:block bg-white shadow-2xl min-w-[150px] rounded-md border border-gray-100">
            <ul>
              <li className="px-5 py-3 rounded-md hover:bg-gray-100 hover:cursor-pointer">
                <Link to="/profile">Profile</Link>
              </li>
              <li
                className="px-5 py-3 rounded-md hover:bg-gray-100 hover:cursor-pointer"
                onClick={() => handleLogout()}
              >
                <button className="hover:cursor-pointer">Logout</button>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </nav>
  )
}

export default Navbar
