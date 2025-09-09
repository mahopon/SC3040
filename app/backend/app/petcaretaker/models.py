from app.database.core import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from uuid import UUID


class PetCareTaker(Base):
    id: Mapped[UUID] = mapped_column(ForeignKey("profile.id", ondelete="cascade"), primary_key=True)
    yoe: Mapped[int] = mapped_column(nullable=False, comment="Years of experience")

    profile: Mapped["Profile"] = relationship(back_populates="petcaretaker")  # noqa
    offered_services: Mapped[list["OfferedService"]] = relationship(back_populates="petcaretaker")  # noqa
    __mapper_args__ = {"polymorphic_identity": "caretaker"}
