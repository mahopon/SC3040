from app.database.core import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.service.enums import Day as DayEnum


class ServiceBooking(Base):
    """
    Represents a booking of an OfferedService for a Pet.

    Attributes:
        id (int): Primary key.
        offered_service_id (int): FK to OfferedService.id.
        pet_id (int): FK to Pet.id.
        pet (Pet): Relationship to the booked pet.
        offered_service (OfferedService): Relationship to the offered service.
        service_booking_days (list[ServiceBookingDay]): Days of booking.
        review (Review): Review associated with this booking.
        billing (Billing): Billing information for this booking.
    """

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    offered_service_id: Mapped[int] = mapped_column(
        ForeignKey("offered_service.id", ondelete="CASCADE"), nullable=False
    )
    pet_id: Mapped[int] = mapped_column(ForeignKey("pet.id", ondelete="CASCADE"), nullable=False)

    pet: Mapped["Pet"] = relationship(back_populates="service_bookings")  # noqa
    offered_service: Mapped["OfferedService"] = relationship(back_populates="service_bookings")  # noqa
    service_booking_days: Mapped[list["ServiceBookingDay"]] = relationship(back_populates="service_booking")
    review: Mapped["Review"] = relationship(back_populates="service_booking")  # noqa
    billing: Mapped["Billing"] = relationship(back_populates="service_booking")  # noqa


class ServiceBookingDay(Base):
    """
    Represents a specific day of a ServiceBooking.

    Attributes:
        id (int): Foreign key to ServiceBooking.id, primary key.
        day (DayEnum): The day of the booking.
        service_booking (ServiceBooking): Relationship to the booking.
    """

    id: Mapped[int] = mapped_column(ForeignKey("service_booking.id"), primary_key=True)
    day: Mapped[DayEnum] = mapped_column(primary_key=True)
    service_booking: Mapped["ServiceBooking"] = relationship(back_populates="service_booking_days")
