
import { EyeOff, Eye } from "lucide-react"
import { useState } from "react"
import { useNavigate, Link } from "react-router-dom"
import Loading from "@/components/Loading"

export default function SignUp() {

  const [firstName, setFirstName] = useState("")
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [showPassword, setShowPassword] = useState(false)
  const [agree, setAgree] = useState(false)
  const [isSubmitting, setIsSubmitting] = useState(false)
  const navigate = useNavigate()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsSubmitting(true)
    // TODO: handle sign up logic here
    setTimeout(() => {
      setIsSubmitting(false)
      navigate("/", { replace: true })
    }, 1000)
  }

  return (
    <>
      <div className="auth-bg fixed inset-0 z-[-1] bg-gradient-to-br from-indigo-400 from-5% via-teal-300 via-25% to-orange-300 to-80%"></div>
      <div className="min-h-screen flex flex-col px-12">
        <header className="flex justify-between items-center pt-9">
          <div className="flex items-center gap-3">
            <div className="w-12 h-12 bg-black rounded-full flex items-center justify-center">
              <span className="text-white font-bold text-xl">PM</span>
            </div>
            <span className="text-gray-800 font-medium text-xl">PawfectMatch</span>
          </div>
          <Link
            to="/login"
            className="px-6 py-2 border-2 border-black text-black font-bold text-sm hover:bg-black hover:text-white transition-colors"
          >
            SIGN IN
          </Link>
        </header>

        <div className="flex-1 flex items-center justify-center">
          <div className="bg-white rounded-lg shadow-xl px-16 pt-14 pb-20 w-full max-w-lg">
            <div className="text-center mb-8">
              <h1 className="text-3xl font-bold text-gray-900 mb-2">Sign up to PawfectMatch</h1>
              <p className="text-gray-600 text-sm">A simple way to take care for your pet</p>
            </div>

            <form onSubmit={handleSubmit} className="space-y-6" noValidate>
              <div>
                <label
                  htmlFor="firstName"
                  className="block text-xs font-medium text-gray-700 mb-2 uppercase tracking-wide"
                >
                  First Name
                </label>
                <input
                  id="firstName"
                  type="text"
                  className="w-full px-3 py-3 border rounded-md focus:outline-none focus:border-black border-gray-300"
                  value={firstName}
                  onChange={e => setFirstName(e.target.value)}
                  required
                />
              </div>
              <div>
                <label
                  htmlFor="email"
                  className="block text-xs font-medium text-gray-700 mb-2 uppercase tracking-wide"
                >
                  Email Address
                </label>
                <input
                  id="email"
                  type="email"
                  className="w-full px-3 py-3 border rounded-md focus:outline-none focus:border-black border-gray-300"
                  value={email}
                  onChange={e => setEmail(e.target.value)}
                  required
                />
              </div>
              <div>
                <label
                  htmlFor="password"
                  className="block text-xs font-medium text-gray-700 mb-2 uppercase tracking-wide"
                >
                  Password
                </label>
                <div className="relative">
                  <input
                    id="password"
                    type={showPassword ? "text" : "password"}
                    className="w-full px-3 py-3 border rounded-md focus:outline-none focus:border-black border-gray-300"
                    value={password}
                    onChange={e => setPassword(e.target.value)}
                    required
                  />
                  <button
                    type="button"
                    onClick={() => setShowPassword((s) => !s)}
                    className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600"
                    aria-label={showPassword ? "Hide password" : "Show password"}
                  >
                    {showPassword ? <EyeOff size={20} /> : <Eye size={20} />}
                  </button>
                </div>
              </div>
              <div className="flex items-center">
                <label className="flex items-center">
                  <input
                    type="checkbox"
                    className="w-4 h-4 border-gray-300 rounded"
                    checked={agree}
                    onChange={e => setAgree(e.target.checked)}
                    required
                  />
                  <span className="ml-2 text-sm text-gray-600">I agree to the Terms of Service and Privacy Policy.</span>
                </label>
              </div>
              <button
                type="submit"
                disabled={!agree || isSubmitting}
                className="w-full bg-black text-white py-3 px-4 rounded-md hover:bg-gray-800 transition-colors font-medium disabled:opacity-60"
              >
                {isSubmitting ? <Loading /> : "CREATE ACCOUNT"}
              </button>
            </form>
          </div>
        </div>
      </div>
    </>
  )
}
