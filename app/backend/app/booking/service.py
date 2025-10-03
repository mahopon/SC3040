from .protocols import InternalBookingService
from .repository import BookingRepository


class BookingService(InternalBookingService):
    def __init__(self, repo: BookingRepository):
        self.repo = repo
