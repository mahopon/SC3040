from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.core import Base
from uuid import UUID


class Pet(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    owner_id: Mapped[UUID] = mapped_column(ForeignKey("pet_owner.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    species: Mapped[str] = mapped_column(nullable=False)
    breed: Mapped[str] = mapped_column(nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    health: Mapped[str] = mapped_column(nullable=False, default="Healthy")
    preferences: Mapped[str] = mapped_column(nullable=False, default="NIL")

    owner: Mapped["PetOwner"] = relationship(back_populates="pets")  # noqa
    service_bookings: Mapped[list["ServiceBooking"]] = relationship(back_populates="pet")  # noqa
