import { BriefcaseBusiness, Cake, Mail, MapPin, PersonStanding, Phone } from "lucide-react"
import type { ReactNode } from "react"

type TAboutProps = {
  role: string
  address: string
  phoneNo: string
  email: string
  gender: string
  dateOfBirth: string
}

type TAboutItemProps = {
  icon: ReactNode
  label: string
}

const AboutItem = ({ icon, label }: TAboutItemProps) => {
  return (
    <div className="flex gap-5 items-center">
      <div className="w-6 h-6">{icon}</div>
      <div>{label}</div>
    </div>
  )
}

const About = ({ role, address, phoneNo, email, gender, dateOfBirth }: TAboutProps) => {
  return (
    <div className="mt-15">
      <div className="font-bold mb-3">About</div>
      <div className="border border-gray-300 rounded-md flex flex-col gap-5 px-5 py-7">
        <AboutItem icon={<BriefcaseBusiness />} label={role} />
        <AboutItem icon={<MapPin />} label={address} />
        <AboutItem icon={<Phone />} label={`+65 ${phoneNo}`} />
        <AboutItem icon={<Mail />} label={email} />
        <AboutItem icon={<PersonStanding />} label={gender} />
        <AboutItem icon={<Cake />} label={dateOfBirth} />
      </div>
    </div>
  )
}

export default About
