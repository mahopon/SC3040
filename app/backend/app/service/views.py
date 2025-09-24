from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .dependency import InternalServiceSvc as ServiceSvc

service_router = APIRouter()


@service_router.get("")
def get_services(service_service: ServiceSvc) -> JSONResponse:
    all_services = service_service.get_services()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(all_services))
