import { useMemo, useState } from "react"
import type { ChangeEvent, FormEvent } from "react"
import { useLocation, useNavigate } from "react-router-dom"
import {
  ArrowLeft,
  BadgeCheck,
  CalendarDays,
  CreditCard,
  ShieldCheck,
  Tag,
  User,
} from "lucide-react"

import "./Payment.css"

type PaymentLocationState = {
  serviceId: string
  serviceName: string
  serviceDuration: string
  servicePrice: number
  date: string
  time: string
  promoCode: string | null
  total: number
}

const formatCurrency = (value: number) =>
  new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    minimumFractionDigits: 2,
  }).format(value)

type CardForm = {
  name: string
  number: string
  expiry: string
  cvc: string
}

const Payment = () => {
  const navigate = useNavigate()
  const location = useLocation()
  const details = location.state as PaymentLocationState | undefined

  const [cardForm, setCardForm] = useState<CardForm>({ name: "", number: "", expiry: "", cvc: "" })
  const [showSuccess, setShowSuccess] = useState(false)

  const formattedDate = useMemo(() => {
    if (!details?.date) {
      return "No date selected"
    }

    return new Intl.DateTimeFormat("en-US", {
      month: "short",
      day: "numeric",
      weekday: "short",
    }).format(new Date(details.date))
  }, [details?.date])

  const formattedTime = details?.time || "No timeslot selected"
  const formattedTotal = details ? formatCurrency(details.total) : formatCurrency(0)

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    setShowSuccess(true)
  }

  const handleCardFieldChange =
    (field: keyof CardForm) => (event: ChangeEvent<HTMLInputElement>) => {
      setCardForm((previous) => ({ ...previous, [field]: event.target.value }))
      setShowSuccess(false)
    }

  if (!details) {
    return (
      <main className="paymentPage paymentPage--empty">
        <section className="paymentCard">
          <h1>Ready to confirm a booking?</h1>
          <p>
            We couldn&apos;t find any booking details. Start a new booking to reach the payment
            step.
          </p>
          <button type="button" className="paymentButton" onClick={() => navigate("/booking/new")}>
            Start a booking
          </button>
        </section>
      </main>
    )
  }

  return (
    <main className="paymentPage">
      <header className="paymentHeader" aria-label="Payment header">
        <button
          type="button"
          className="backButton"
          onClick={() => navigate("/booking/new")}
          aria-label="Back to booking"
        >
          <ArrowLeft aria-hidden="true" strokeWidth={1.8} />
        </button>

        <span className="paymentBadge">
          <ShieldCheck aria-hidden="true" strokeWidth={1.8} />
          Protected checkout
        </span>
      </header>

      <div className="paymentLayout">
        <section className="paymentCard summaryCard" aria-label="Booking summary">
          <header className="cardHeader">
            <h2>Review &amp; confirm</h2>
            <p>Make sure the details look right before you pay.</p>
          </header>

          <div className="summaryList">
            <div className="summaryItem">
              <CalendarDays aria-hidden="true" strokeWidth={1.6} />
              <div>
                <span>{formattedDate}</span>
                <span className="summarySub">{formattedTime}</span>
              </div>
            </div>

            <div className="summaryItem">
              <BadgeCheck aria-hidden="true" strokeWidth={1.6} />
              <div>
                <span>{details.serviceName}</span>
                <span className="summarySub">{details.serviceDuration}</span>
              </div>
            </div>
          </div>

          <dl className="summaryTotals">
            <div>
              <dt>Service price</dt>
              <dd>{formatCurrency(details.servicePrice)}</dd>
            </div>
            <div>
              <dt>Promo code</dt>
              <dd>{details.promoCode ?? "None applied"}</dd>
            </div>
            <div className="summaryTotalRow">
              <dt>Total due today</dt>
              <dd>{formattedTotal}</dd>
            </div>
          </dl>

          <div className="paymentSupport">
            <User aria-hidden="true" strokeWidth={1.6} />
            <div>
              <span>Need a hand?</span>
              <span className="summarySub">Our support team is just a message away.</span>
            </div>
          </div>
        </section>

        <section className="paymentCard formCard" aria-label="Payment form">
          <header className="cardHeader">
            <h2>Payment details</h2>
            <p>Enter your card information to complete the booking.</p>
          </header>

          <div className="methodHighlight">
            <CreditCard aria-hidden="true" strokeWidth={1.6} />
            <div>
              <span>Card payment</span>
              <span className="summarySub">Visa, Mastercard, and Amex accepted</span>
            </div>
          </div>

          <form className="paymentForm" onSubmit={handleSubmit} aria-live="polite">
            <label className="formField" htmlFor="card-name">
              <span>Cardholder name</span>
              <input
                id="card-name"
                type="text"
                value={cardForm.name}
                onChange={handleCardFieldChange("name")}
                placeholder="Jordan Smith"
                required
              />
            </label>

            <label className="formField" htmlFor="card-number">
              <span>Card number</span>
              <input
                id="card-number"
                type="text"
                inputMode="numeric"
                value={cardForm.number}
                onChange={handleCardFieldChange("number")}
                placeholder="4242 4242 4242 4242"
                required
              />
            </label>

            <div className="formRow">
              <label className="formField" htmlFor="card-expiry">
                <span>Expiry</span>
                <input
                  id="card-expiry"
                  type="text"
                  inputMode="numeric"
                  value={cardForm.expiry}
                  onChange={handleCardFieldChange("expiry")}
                  placeholder="MM/YY"
                  required
                />
              </label>

              <label className="formField" htmlFor="card-cvc">
                <span>CVC</span>
                <input
                  id="card-cvc"
                  type="password"
                  inputMode="numeric"
                  value={cardForm.cvc}
                  onChange={handleCardFieldChange("cvc")}
                  placeholder="123"
                  required
                />
              </label>
            </div>

            {details.promoCode ? (
              <div className="appliedPromo">
                <Tag aria-hidden="true" strokeWidth={1.6} />
                <span>
                  Promo <strong>{details.promoCode}</strong> will be applied at confirmation.
                </span>
              </div>
            ) : null}

            <button type="submit" className="paymentButton">
              Complete payment ({formattedTotal})
            </button>
          </form>

          {showSuccess ? (
            <div className="successBanner" role="status">
              <ShieldCheck aria-hidden="true" strokeWidth={1.6} />
              <div>
                <strong>Payment confirmed</strong>
                <span className="summarySub">
                  You&apos;ll receive a confirmation email shortly.
                </span>
              </div>
            </div>
          ) : null}
        </section>
      </div>
    </main>
  )
}

export default Payment
