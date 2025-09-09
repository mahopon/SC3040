from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.core import Base
from app.service.models import offered_service_location


class Location(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)

    offered_services: Mapped[list["OfferedService"]] = relationship(  # noqa
        secondary=offered_service_location, back_populates="locations"
    )
