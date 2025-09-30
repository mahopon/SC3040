import pytest
from uuid import uuid4
from unittest.mock import MagicMock
from app.service.service import ServiceService
from app.service.models import OfferedService, Service
from app.service.schemas import OfferedService as OfferedServiceDTO, OfferedServiceCreate, Service as ServiceDTO
from app.service.enums import Day


@pytest.fixture
def repo_mock():
    return MagicMock()


@pytest.fixture
def service(repo_mock):
    return ServiceService(repo=repo_mock)


def test_create_offered_service(service, repo_mock):
    profile_id = uuid4()
    offered_service_req = OfferedServiceCreate(service_id=1, rate=50, day=[1, 2, 3])
    service.create_offered_service(profile_id=profile_id, offered_service_req=offered_service_req)

    created_obj = repo_mock.create_offered_service.call_args[1]["offered_service_new"]

    service.repo.create_offered_service.assert_called_once()
    assert created_obj.service_id == 1
    assert created_obj.rate == 50
    assert created_obj.day == [Day.Monday, Day.Tuesday, Day.Wednesday]


def test_get_offered_services_by_profile_id(service, repo_mock):
    profile_id = uuid4()
    fake_services = [
        OfferedService(id=1, caretaker_id=profile_id, service_id=1, rate=5, service=Service(id=1, name="Walking")),
        OfferedService(id=2, caretaker_id=profile_id, service_id=2, rate=10, service=Service(id=2, name="Grooming")),
    ]
    repo_mock.get_offered_services_by_profile_id.return_value = fake_services

    result = service.get_offered_services_by_profile_id(profile_id=profile_id)

    service.repo.get_offered_services_by_profile_id.assert_called_once_with(profile_id=profile_id)
    assert len(result) == 2
    assert all(isinstance(svc, OfferedServiceDTO) for svc in result)
    assert result[0].id == 1
    assert result[1].id == 2


def test_get_services(service, repo_mock):
    fake_services = [Service(id=1, name="Grooming"), Service(id=2, name="Walking")]
    repo_mock.get_services.return_value = fake_services

    result = service.get_services()

    service.repo.get_services.assert_called_once()
    assert len(result) == 2
    assert all(isinstance(svc, ServiceDTO) for svc in result)
    assert result[0].name == "Grooming"
    assert result[1].name == "Walking"
