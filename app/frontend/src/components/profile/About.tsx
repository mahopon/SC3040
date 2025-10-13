import type { TUserGender, TUserRole } from "@/api/profile/types"
import { USER_GENDER, USER_ROLE } from "@/constants/user"
import { formatDate } from "@/utils/formatDateTime"
import { BriefcaseBusiness, Cake, MapPin, PersonStanding, Phone, Star } from "lucide-react"
import type { ReactNode } from "react"

type TAboutProps = {
  role: TUserRole
  address: string
  phoneNo: string
  gender: TUserGender
  dateOfBirth: string
  yearsOfExperience?: number
}

type TAboutItemProps = {
  icon: ReactNode
  label: string
}

const AboutItem = ({ icon, label }: TAboutItemProps) => {
  return (
    <div className="flex gap-5 items-center">
      <div className="w-6 h-6">{icon}</div>
      <div>{label || "-"}</div>
    </div>
  )
}

const About = ({ role, address, phoneNo, gender, dateOfBirth, yearsOfExperience }: TAboutProps) => {
  console.log(role)
  return (
    <div className="mt-15">
      <div className="font-bold mb-3">About</div>
      <div className="border border-gray-300 rounded-md flex flex-col gap-5 px-5 py-7">
        <AboutItem icon={<BriefcaseBusiness />} label={USER_ROLE[role]} />
        <AboutItem icon={<MapPin />} label={address} />
        <AboutItem icon={<Phone />} label={`+65 ${phoneNo}`} />
        <AboutItem icon={<PersonStanding />} label={USER_GENDER[gender]} />
        <AboutItem icon={<Cake />} label={formatDate(dateOfBirth)} />
        {role === "caretaker" && yearsOfExperience && (
          <AboutItem icon={<Star />} label={`${yearsOfExperience} Years of Experience`} />
        )}
      </div>
    </div>
  )
}

export default About
