from app.database.core import Base
from sqlalchemy import ForeignKey
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
    name: Mapped[str] = mapped_column(nullable=False)
    dob: Mapped[datetime] = mapped_column(nullable=True)
    gender: Mapped[Gender] = mapped_column(nullable=True)

    petowner: Mapped["PetOwner"] = relationship(back_populates="profile")  # noqa
    petcaretaker: Mapped["PetCareTaker"] = relationship(back_populates="profile")  # noqa

    __mapper_args__ = {"polymorphic_identity": "user"}
