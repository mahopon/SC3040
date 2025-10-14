import { Link, useNavigate } from "react-router-dom"
import AppLogo from "./AppLogo"
import { userPlaceholderUrl } from "@/assets"
import { useUser } from "@/context/UserContext"

const Navbar = () => {
  const navigate = useNavigate()
  const {
    user: { profile_picture },
  } = useUser()

  return (
    <nav className="w-full shadow-md flex items-center justify-between px-8 py-5">
      <AppLogo />

      <div className="flex items-center gap-10">
        <Link to="/" className="font-medium hover:underline">
          Dashboard
        </Link>
        <Link to="/services" className="font-medium hover:underline">
          Browse Services
        </Link>
        <Link to="/bookings" className="font-medium hover:underline">
          Bookings
        </Link>

        <button 
          className="h-10 w-10 hover:cursor-pointer" 
          aria-label="User profile"
          onClick={() => navigate("/profile")}
        >
          <img
            src={profile_picture || userPlaceholderUrl}
            alt="Profile"
            className="h-full w-full object-cover rounded-full"
          />
        </button>
      </div>
    </nav>
  )
}

export default Navbar
