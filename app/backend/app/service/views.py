from fastapi import APIRouter, status, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .dependency import InternalServiceSvc as ServiceSvc
from .schemas import OfferedServiceCreate
from uuid import UUID
from app.auth.dependency import CurrentId

service_router = APIRouter()
offered_service_router = APIRouter()


@service_router.get("/")
def get_services(service_service: ServiceSvc) -> JSONResponse:
    all_services = service_service.get_services()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(all_services))


@offered_service_router.get("/")
def get_offered_services(service_service: ServiceSvc):
    pass


@offered_service_router.get("/{user_id}")
def get_offered_services_by_id(service_service: ServiceSvc, user_id: UUID = Path(...)):
    pass


@offered_service_router.post("/create")
def create_offered_service(id: CurrentId, service_service: ServiceSvc, new_offered_svc_req: OfferedServiceCreate):
    pass


@offered_service_router.put("/{offered_svc_id}")
def update_offered_service(
    id: CurrentId, service_service: ServiceSvc, offered_svc_update_req: OfferedServiceCreate, offered_svc_id=Path(...)
):  # TODO: Temp schema
    pass


@offered_service_router.delete("/{offered_svc_id}")
def delete_offered_service(id: CurrentId, service_service: ServiceSvc, offered_svc_id=Path(...)):
    pass
