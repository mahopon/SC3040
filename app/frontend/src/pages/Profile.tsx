import { ProfileAPI } from "@/api"
import type { ProfileResponse } from "@/api/profile/types"
import Navbar from "@/components/Navbar"
import About from "@/components/profile/About"
import ContentLayout from "@/components/profile/ContentLayout"
import PetCard from "@/components/profile/PetCard"
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

            {user.type === "caretaker" && (
              <ContentLayout
                title="Service(s) Provided"
                action={{
                  label: "+ Add Service",
                  onClick: () => console.log("Add service"),
                }}
                children={
                  <>
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
                  </>
                }
              />
            )}

            {user.type === "owner" && (
              <ContentLayout
                title="Pet(s) Owned"
                action={{
                  label: "+ Add Pet",
                  onClick: () => console.log("Add pet"),
                }}
                children={
                  <>
                    <PetCard
                      pet={{
                        id: 0,
                        name: "Happy",
                        species: "Dog",
                        breed: "Labrador Retriever",
                        age: 2,
                        health: "Healthy",
                        preferences:
                          "Prefers beef over anything else, does not like medicine, does not like needles, very scared of the vet",
                      }}
                      onEdit={(id: number) => console.log("Editing pet: ", id)}
                      onDelete={(id: number) => console.log("Deleting pet: ", id)}
                    />
                    <PetCard
                      pet={{
                        id: 0,
                        name: "Milk",
                        species: "Cat",
                        breed: "Persian",
                        age: 5,
                        health: "Healthy",
                        preferences:
                          "Very friendly, does not mind being touches, bla bla bla bla bla",
                      }}
                      onEdit={(id: number) => console.log("Editing pet: ", id)}
                      onDelete={(id: number) => console.log("Deleting pet: ", id)}
                    />
                  </>
                }
              />
            )}
          </div>
        </div>
      )}
    </div>
  )
}

export default Profile
