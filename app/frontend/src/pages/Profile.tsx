import { ProfileAPI } from "@/api"
import type { ProfileResponse } from "@/api/profile/types"
import Navbar from "@/components/Navbar"
import About from "@/components/profile/About"
import ServiceCard from "@/components/profile/ServiceCard"
import { User } from "lucide-react"
import { useEffect, useState } from "react"

const Profile = () => {
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
            {user?.profile_picture ? (
              <img
                src={user.profile_picture || "/placeholder.svg"}
                alt="Profile"
                className="h-full w-full object-cover rounded-full"
              />
            ) : (
              <User className="h-full w-full" />
            )}
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

            <div className="mt-5 space-y-5">
              <div className="flex items-center justify-between">
                <h2 className="font-bold">Service(s) Provided</h2>
                <button className="bg-black text-white py-2 px-4 rounded-md  transition-colors font-medium disabled:opacity-60 enabled:hover:bg-gray-800 enabled:hover:cursor-pointer">
                  + Add Service
                </button>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <ServiceCard
                  service={{
                    id: 1,
                    serviceId: 1,
                    name: "Dog Grooming",
                    description:
                      "Full grooming service including bath, haircut, nail trimming, and ear cleaning for all dog breeds.",
                    rate: 80,
                    duration: 120,
                    days: [1, 2, 3, 4, 5],
                  }}
                  onEdit={(id: number) => console.log("Editing service: ", id)}
                  onDelete={(id: number) => console.log("Deleting service: ", id)}
                />
                <ServiceCard
                  service={{
                    id: 1,
                    serviceId: 1,
                    name: "Cat Grooming",
                    description:
                      "Gentle grooming for cats including bath, brushing, and nail trimming with specialized care.",
                    rate: 50,
                    duration: 60,
                    days: [1, 2, 3, 4, 5],
                  }}
                  onEdit={(id: number) => console.log("Editing service: ", id)}
                  onDelete={(id: number) => console.log("Deleting service: ", id)}
                />
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default Profile
