import json
from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status
from starlette.responses import JSONResponse

from models.api_service import ApiService
from models.probes import HealthStatus
from operations.probes import check_health, check_readiness


router = APIRouter()


@router.get("/_/ready", response_model=None)
async def readiness() -> JSONResponse:
    """
    This function serves as readiness probe.

    Returns:
        JSONResponse: a response.
    """
    headers = {
        "content-type": "application/json",
    }

    health = check_readiness()

    if health.status == HealthStatus.HEALTHY:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=json.loads(health.model_dump_json()),
            headers=headers,
        )

    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content=json.loads(health.model_dump_json()),
        headers=headers,
    )


@router.get("/_/health", response_model=None)
async def liveness() -> JSONResponse:
    """This function serves as readiness probe.

    Returns:
        JSONResponse: a response.
    """
    headers = {
        "content-type": "application/json",
    }

    health = check_health()

    if health.status == HealthStatus.HEALTHY:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=json.loads(health.model_dump_json()),
            headers=headers,
        )

    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content=json.loads(health.model_dump_json()),
        headers=headers,
    )
