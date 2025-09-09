from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.core import Base
from datetime import datetime


class Billing(Base):
    id: Mapped[int] = mapped_column(ForeignKey("service_booking.id"), primary_key=True)
    total_payable: Mapped[float] = mapped_column(nullable=False)
    paid_at: Mapped[datetime] = mapped_column(nullable=True)

    service_booking: Mapped["ServiceBooking"] = relationship(back_populates="billing")  # noqa
    payment: Mapped["Payment"] = relationship(back_populates="billing")  # noqa


class Payment(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    billing_id: Mapped[int] = mapped_column(ForeignKey("billing.id", ondelete="CASCADE"))
    amount_paid: Mapped[float] = mapped_column(nullable=False)

    billing: Mapped["Billing"] = relationship(back_populates="payment")
