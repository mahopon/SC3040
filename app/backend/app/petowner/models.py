from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.core import Base
from uuid import UUID


class PetOwner(Base):
    id: Mapped[UUID] = mapped_column(ForeignKey("profile.id", ondelete="CASCADE"), primary_key=True)

    # TODO Add relationships for Location, Payment
    profile: Mapped["Profile"] = relationship(back_populates="petowner")  # noqa
    pets: Mapped[list["Pet"]] = relationship(back_populates="owner")  # noqa

    __mapper_args__ = {"polymorphic_identity": "owner"}
