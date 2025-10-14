import { useMemo, useState } from "react"
import { useNavigate } from "react-router-dom"
import { ArrowLeft, Bell, CalendarDays, Clock, Settings, Sparkles, Tag, User } from "lucide-react"

import "./NewBooking.css"

type ServiceId = "basic-grooming" | "full-grooming" | "walk-30" | "walk-60" | "drop-in"

type ServiceOption = {
  id: ServiceId
  name: string
  description: string
  durationLabel: string
  price: number
}

const SERVICE_OPTIONS: ServiceOption[] = [
  {
    id: "basic-grooming",
    name: "Basic Grooming",
    description: "Bath, blow-dry, nail trim.",
    durationLabel: "45 min",
    price: 40,
  },
  {
    id: "full-grooming",
    name: "Full Grooming",
    description: "Complete groom incl. styling.",
    durationLabel: "90 min",
    price: 75,
  },
  {
    id: "walk-30",
    name: "Dog Walking (30m)",
    description: "Neighbourhood walk.",
    durationLabel: "30 min",
    price: 20,
  },
  {
    id: "walk-60",
    name: "Dog Walking (60m)",
    description: "Park & playtime walk.",
    durationLabel: "60 min",
    price: 35,
  },
  {
    id: "drop-in",
    name: "Drop-in Visit",
    description: "Water, feed, quick clean.",
    durationLabel: "30 min",
    price: 28,
  },
]

const TIME_SLOTS = [
  "09:00",
  "09:30",
  "10:00",
  "10:30",
  "11:00",
  "11:30",
  "13:00",
  "13:30",
  "14:00",
  "14:30",
  "15:00",
  "15:30",
  "16:00",
]

const formatCurrency = (value: number) =>
  new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    minimumFractionDigits: 2,
  }).format(value)

const NewBooking = () => {
  const navigate = useNavigate()
  const [selectedService, setSelectedService] = useState<ServiceId>("basic-grooming")
  const [date, setDate] = useState("")
  const [time, setTime] = useState("")
  const [promoCode, setPromoCode] = useState("")

  const selectedServiceDetails = useMemo(
    () => SERVICE_OPTIONS.find((option) => option.id === selectedService) ?? SERVICE_OPTIONS[0],
    [selectedService],
  )

  const subtotal = selectedServiceDetails.price
  const total = subtotal
  const hasSelections = Boolean(date && time)
  const formattedDate = date
    ? new Intl.DateTimeFormat("en-US", {
        month: "short",
        day: "numeric",
        weekday: "short",
      }).format(new Date(date))
    : "No date"

  const handleConfirm = () => {
    if (!hasSelections) return

    navigate("/booking/payment", {
      state: {
        serviceId: selectedServiceDetails.id,
        serviceName: selectedServiceDetails.name,
        serviceDuration: selectedServiceDetails.durationLabel,
        servicePrice: selectedServiceDetails.price,
        date,
        time,
        promoCode: promoCode.trim() || null,
        total,
      },
    })
  }

  return (
    <main className="bookingPage">
      <header className="bookingHeader" aria-label="Page header">
        <div className="brand">
          <button
            type="button"
            className="iconCircle backButton"
            onClick={() => navigate(-1)}
            aria-label="Go back"
          >
            <ArrowLeft aria-hidden="true" strokeWidth={1.8} />
          </button>
          <div className="brandText">
            <span className="brandTitle">Book a Service</span>
            <span className="brandSubtitle">
              Choose a service, pick a time, and you&apos;re set.
            </span>
          </div>
        </div>
        <div className="navIcons" role="group" aria-label="Quick links">
          <span className="badge badgeVersion">
            <Sparkles className="badgeIcon" aria-hidden="true" strokeWidth={1.6} />
            <span className="badgeLabel">v0.1 Mock</span>
          </span>
          <button type="button" className="iconButton" aria-label="View notifications">
            <Bell aria-hidden="true" strokeWidth={1.8} />
          </button>
          <button type="button" className="iconButton" aria-label="Open settings">
            <Settings aria-hidden="true" strokeWidth={1.8} />
          </button>
          <button type="button" className="iconButton profileButton" aria-label="Open profile">
            <User aria-hidden="true" strokeWidth={1.8} />
          </button>
        </div>
      </header>

      <div className="bookingLayout" role="presentation">
        <section className="mainColumn">
          <article className="panel">
            <header className="panelHeader">
              <h2>
                <Sparkles aria-hidden="true" strokeWidth={1.6} /> Select Service
              </h2>
              <p>Pick what you need. Prices shown are base rates.</p>
            </header>

            <div className="serviceOptions" role="list">
              {SERVICE_OPTIONS.map((option) => {
                const isActive = option.id === selectedService
                return (
                  <button
                    key={option.id}
                    type="button"
                    role="listitem"
                    className={`serviceOption ${isActive ? "isActive" : ""}`}
                    onClick={() => setSelectedService(option.id)}
                    aria-pressed={isActive}
                  >
                    <div className="serviceOptionHeader">
                      <span className="serviceName">{option.name}</span>
                      <span className="servicePrice">{formatCurrency(option.price)}</span>
                    </div>
                    <p className="serviceDescription">{option.description}</p>
                    <span className="serviceDuration">
                      <Clock aria-hidden="true" strokeWidth={1.5} /> {option.durationLabel}
                    </span>
                  </button>
                )
              })}
            </div>
          </article>

          <article className="panel">
            <header className="panelHeader">
              <h2>
                <CalendarDays aria-hidden="true" strokeWidth={1.6} /> Date &amp; Time
              </h2>
              <p>Select a date and a convenient timeslot.</p>
            </header>

            <div className="scheduleSection">
              <label className="dateField" htmlFor="booking-date">
                <span>Date</span>
                <input
                  id="booking-date"
                  type="date"
                  value={date}
                  onChange={(event) => setDate(event.target.value)}
                />
              </label>

              <div className="timeField">
                <span>Timeslot</span>
                <div className="timeGrid" role="radiogroup" aria-label="Choose a timeslot">
                  {TIME_SLOTS.map((slot) => {
                    const isSelected = slot === time
                    return (
                      <button
                        key={slot}
                        type="button"
                        className={`timeCell ${isSelected ? "isSelected" : ""}`}
                        onClick={() => setTime(slot)}
                        aria-pressed={isSelected}
                      >
                        {slot}
                      </button>
                    )
                  })}
                </div>
              </div>
            </div>
          </article>
        </section>

        <aside className="summaryColumn" aria-label="Booking summary">
          <div className="summaryCard">
            <header className="panelHeader">
              <h2>Summary</h2>
              <p>Review your selection before confirming.</p>
            </header>

            <div className="summaryBlock">
              <div className="summaryLine">
                <CalendarDays aria-hidden="true" strokeWidth={1.6} />
                <div>
                  <span>{formattedDate}</span>
                  <span className="summarySub">{time || "No timeslot selected"}</span>
                </div>
              </div>
              <div className="summaryLine">
                <Sparkles aria-hidden="true" strokeWidth={1.6} />
                <div>
                  <span>{selectedServiceDetails.name}</span>
                  <span className="summarySub">{selectedServiceDetails.durationLabel}</span>
                </div>
              </div>
            </div>

            <dl className="totals">
              <div>
                <dt>Base price</dt>
                <dd>{formatCurrency(subtotal)}</dd>
              </div>
              <div>
                <dt>Add-ons</dt>
                <dd>None</dd>
              </div>
              <div className="promoRow">
                <dt>Subtotal</dt>
                <dd>{formatCurrency(subtotal)}</dd>
              </div>
              <div className="promoInput">
                <Tag aria-hidden="true" strokeWidth={1.6} />
                <input
                  type="text"
                  placeholder="Promo code"
                  value={promoCode}
                  onChange={(event) => setPromoCode(event.target.value)}
                />
              </div>
              <div>
                <dt>Total</dt>
                <dd>{formatCurrency(total)}</dd>
              </div>
            </dl>

            <button
              type="button"
              className="summaryButton"
              disabled={!hasSelections}
              onClick={handleConfirm}
            >
              Confirm booking
            </button>
          </div>
        </aside>
      </div>
    </main>
  )
}

export default NewBooking
