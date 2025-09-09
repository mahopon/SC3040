import { EyeOff, Eye } from "lucide-react"
import { useState } from "react"

const Login = () => {
  const [email, setEmail] = useState("johndoe@example.com")
  const [password, setPassword] = useState("")
  const [showPassword, setShowPassword] = useState(false)
  const [rememberMe, setRememberMe] = useState(false)

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    console.log("Login attempt:", { email, password, rememberMe })
  }

  return (
    <>
      <div className="auth-bg fixed inset-0 z-[-1] bg-gradient-to-br from-purple-400 via-blue-400 via-teal-400 to-yellow-300"></div>
      <div className="min-h-screen flex flex-col px-12">
        <header className="flex justify-between items-center py-9">
          <div className="flex items-center gap-3">
            <div className="w-12 h-12 bg-black rounded-full flex items-center justify-center">
              <span className="text-white font-bold text-xl">PM</span>
            </div>
            <span className="text-gray-800 font-medium text-xl">PawfectMatch</span>
          </div>
          <button className="px-6 py-2 border-2 border-black text-black font-bold text-sm hover:bg-black hover:text-white hover:cursor-pointer transition-colors">
            SIGN UP
          </button>
        </header>

        {/* Main Content */}
        <div className="flex-1 flex items-center justify-center p-6">
          <div className="bg-white rounded-lg shadow-xl p-8 w-full max-w-md">
            <div className="text-center mb-8">
              <h1 className="text-2xl font-bold text-gray-900 mb-2">Log In to Petcare</h1>
              <p className="text-gray-600 text-sm">A simple way to take care for your pet</p>
            </div>

            <form onSubmit={handleSubmit} className="space-y-6">
              <div>
                <label
                  htmlFor="email"
                  className="block text-xs font-medium text-gray-700 mb-2 uppercase tracking-wide"
                >
                  Email Address
                </label>
                <input
                  type="email"
                  id="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="w-full px-3 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
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
                    type={showPassword ? "text" : "password"}
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="••••••••••"
                    className="w-full px-3 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent pr-10"
                    required
                  />
                  <button
                    type="button"
                    onClick={() => setShowPassword(!showPassword)}
                    className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-gray-600"
                  >
                    {showPassword ? <EyeOff size={20} /> : <Eye size={20} />}
                  </button>
                </div>
              </div>

              <div className="flex items-center justify-between">
                <label className="flex items-center">
                  <input
                    type="checkbox"
                    checked={rememberMe}
                    onChange={(e) => setRememberMe(e.target.checked)}
                    className="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                  />
                  <span className="ml-2 text-sm text-gray-600">Remember Me</span>
                </label>
                <a href="#" className="text-sm text-gray-600 hover:text-gray-800">
                  Forgot Password?
                </a>
              </div>

              <button
                type="submit"
                className="w-full bg-gray-900 text-white py-3 px-4 rounded-md hover:bg-gray-800 transition-colors font-medium"
              >
                PROCEED
              </button>
            </form>

            <div className="mt-8">
              <div className="text-center text-sm text-gray-500 mb-4">OR USE</div>
              <div className="flex justify-center space-x-4">
                <button className="w-10 h-10 bg-red-500 rounded-full flex items-center justify-center text-white hover:bg-red-600 transition-colors">
                  G
                </button>
                <button className="w-10 h-10 bg-gray-900 rounded-full flex items-center justify-center text-white hover:bg-gray-800 transition-colors"></button>
                <button className="w-10 h-10 bg-blue-600 rounded-full flex items-center justify-center text-white hover:bg-blue-700 transition-colors">
                  f
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default Login
