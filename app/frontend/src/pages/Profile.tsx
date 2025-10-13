import { ProfileAPI } from "@/api"
import type { ProfileResponse } from "@/api/profile/types"
import Navbar from "@/components/Navbar"
import About from "@/components/profile/About"
import { useEffect, useRef, useState } from "react"
import { userPlaceholderUrl } from "@/assets"
import Modal, { type TModalHandle } from "@/components/ui/Modal"
import ServiceContent from "@/components/profile/ServiceContent"
import PetContent from "@/components/profile/PetContent"

const Profile = () => {
  const petModalRef = useRef<TModalHandle>(null)
  const [user, setUser] = useState<ProfileResponse>()

  useEffect(() => {
    ProfileAPI.fetchProfile().then((data) => setUser(data))
  }, [])

  return (
    <div className="min-h-screen">
      <Navbar />

      <div className="relative h-50 bg-gradient-to-r from-purple-400 via-green-300 to-yellow-300">
        <div className="absolute -bottom-10 left-[5%] lg:left-[20%] md:left-[12.5%] flex items-center gap-5">
          <div className="h-36 w-36 ">
            <img
              src={user?.profile_picture || userPlaceholderUrl}
              alt="Profile"
              className="h-full w-full object-cover rounded-full"
            />
          </div>
          <div className="text-4xl font-bold">{user?.first_name}</div>
        </div>
      </div>

      {user && (
        <div className="container mx-auto w-[90%] lg:w-[60%] md:w-[75%]">
          <div className="grid grid-cols-1 lg:grid-cols-[250px_1fr] gap-8">
            <About
              role={user.type}
              address={user.address}
              phoneNo={user.contact_num}
              email=""
              gender={user.gender}
              dateOfBirth={user.dob}
            />

            {user.type === "caretaker" && <ServiceContent />}
            {user.type === "owner" && <PetContent />}
          </div>
        </div>
      )}

      <Modal
        ref={petModalRef}
        header="Add Pet"
        actionButtons={[
          {
            label: "Cancel",
            onClick: () => petModalRef.current?.closeModal(),
          },
          {
            label: "Add",
            onClick: () => {
              petModalRef.current?.closeModal()
              console.log("Adding pet...")
            },
            style: "bg-blue-500 text-white hover:bg-blue-600",
          },
        ]}
      >
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="petName">
            Pet Name
          </label>
          <input id="petName" />
        </div>
      </Modal>
    </div>
  )
}

export default Profile
