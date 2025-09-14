import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from app.config import get_settings
from app.database.core import get_db
from app.auth.repository import AuthRepository
from app.auth.models import Auth
from app.profile.repository import ProfileRepository
from app.profile.models import Profile
from app.petowner.models import PetOwner
from app.petowner.repository import create_petowner
from app.petcaretaker.models import PetCareTaker
from app.petcaretaker.repository import create_petcaretaker
from app.pet.models import Pet
from app.pet.repository import create_pet
from app.service.models import Service, OfferedService
from app.service.repository import (
    create_service,
    create_offered_service,
)
from app.location.models import Location
from app.location.repository import create_location
from datetime import datetime
from uuid import uuid4

settings = get_settings()


password = "P@ssw0rd123!"

session = next(get_db())
auth_repo = AuthRepository(db_session=session)
prof_repo = ProfileRepository(db_session=session)
# UUID generation
uuids = [uuid4() for i in range(2)]
# Auth + Profile + Pet Owner / Pet Care Taker
for i in range(2):
    auth = Auth(id=uuids[i], email=f"test{i}@gmail.com")
    auth.set_password(password)
    auth_repo.create_auth(auth_new=auth)
    profile = Profile(id=uuids[i], name=f"test{i}", dob=datetime.now(), gender="Male")
    prof_repo.create_profile(profile_new=profile)
owner = PetOwner(id=uuids[0])
create_petowner(db_session=session, petowner_new=owner)
caretaker = PetCareTaker(id=uuids[1], yoe=5)
create_petcaretaker(db_session=session, petcaretaker_new=caretaker)
pet = Pet(owner_id=uuids[0], name="Bob", age=10, species="Cat", breed="Munchkin")
create_pet(db_session=session, pet_new=pet)
# Services
services = [
    "Pet Walking",
    "Pet Grooming",
    "Pet Feeding",
    "Pet Training",
    "Pet Sitting",
    "Overnight Stay",
    "Dog Daycare",
]
for name in services:
    service = Service(name=name)
    create_service(db_session=session, service_new=service)
# Locations
locations = [
    "Dhoby Ghaut",
    "Outram Park",
    "Chinatown",
    "Clarke Quay",
    "Boat Quay",
    "City Hall",
    "Esplanade",
    "Raffles Place",
    "Bayfront",
    "Marina Bay",
    "Promontory",
    "Marina Bay Sands",
    "Bugis",
    "Lavender",
    "Kallang",
    "Geylang Bahru",
    "Potong Pasir",
    "Serangoon",
    "Dhoby Ghaut Interchange",
    "Toa Payoh",
    "Braddell",
    "Bishan",
    "Marymount",
    "Bartley",
    "Paya Lebar",
    "Eunos",
    "Bedok",
    "Tampines",
    "Pasir Ris",
    "Simei",
    "Expo",
    "Tanah Merah",
    "Changi Airport",
    "Bedok North",
    "Hougang",
    "Serangoon North",
    "Yishun",
    "Sembawang",
    "Woodlands",
    "Admiralty",
    "Marsiling",
    "Woodlands South",
    "Bukit Panjang",
    "Jelapang",
    "Chua Chu Kang",
    "Lot One",
    "Bukit Gombak",
    "Beauty World",
    "Little India",
    "Orchard",
    "Somerset",
    "Novena",
    "Toa Payoh North",
    "Novena North",
    "Bishan North",
    "Serangoon South",
    "Yishun North",
    "Sembawang North",
    "Bedok North East",
    "Jurong East",
    "Jurong West",
    "Bukit Batok",
    "Lot One North",
    "Woodlands West",
    "Thomson East Coast",
    "Tanjong Pagar",
    "Bencoolen",
    "King Albert Park",
    "Upper Bukit Timah",
    "Bukit Timah",
    "Joo Koon",
    "Jurong Lake",
    "Yishun East",
    "Kranji",
    "Bukit Gombak East",
    "Changi",
    "Puah Road",
    "Orchard Road",
]
locs = []
for loc in locations:
    location = Location(name=loc)
    locs.append(location)
    create_location(db_session=session, location_new=location)
for i in range(1, 4):
    offered_svc = OfferedService(service_id=i, caretaker_id=uuids[1], rate=50, day=["Monday", "Tuesday", "Wednesday"])
    for o in range(1, 4):
        offered_svc.locations.append(locs[o])
    create_offered_service(db_session=session, offered_service_new=offered_svc)

# Commit the transaction
print("Committing changes to the database...")  # Debugging print
session.commit()

# Close the session
session.close()
