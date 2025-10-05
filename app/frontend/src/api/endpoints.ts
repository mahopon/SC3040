export const API = {
  AUTH: {
    LOGIN: "/auth/login",
    SIGNUP: "/auth/register",
    GOOGLE_LOGIN: "/auth/login/google",
    CALLBACK: "/auth/callback",
    LOGOUT: "/auth/logout",
  },
  PROFILE: {
    GET: "/profile",
    UPDATE: "/profile/update",
    PICTURE: "/profile/picture",
  },
  ONBOARDING: {
    STATUS: "/onboarding/status",
    PROFILE: "/onboarding/profile",
    PET: "/onboarding/pet",
    SERVICE: "/onboarding/service",
    COMPLETE: "/onboarding/complete",
  },
  SERVICE: {
    GET: "/service",
  },
  LOCATION: {
    GET: "/location",
  },
}
