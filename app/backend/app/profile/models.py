from app.database.core import Base
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID
from datetime import datetime
from .enums import Gender


class Profile(Base):
    """
    Represents a user's profile details

    Attributes:
        id (UUID): Primary key, Foreign key (Auth)
        name (str): Name of user
        dob (datetime): Date of Birth of user
        gender (enum): Gender of user (male, female, others)
    """

    id: Mapped[UUID] = mapped_column(ForeignKey("auth.id", ondelete="CASCADE"), primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=True)
    dob: Mapped[datetime] = mapped_column(nullable=True)
    gender: Mapped[Gender] = mapped_column(nullable=True)
    contact_num: Mapped[str] = mapped_column(nullable=True)
    address: Mapped[str] = mapped_column(nullable=True)
    setup: Mapped[bool] = mapped_column(default=False, server_default=text("false"))
    type: Mapped[str] = mapped_column(nullable=False, default="profile")
    profile_picture: Mapped[str] = mapped_column(nullable=True)

    petowner: Mapped["PetOwner"] = relationship(back_populates="profile", lazy="joined")  # noqa
    petcaretaker: Mapped["PetCareTaker"] = relationship(back_populates="profile", lazy="joined")  # noqa
