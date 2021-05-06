from fastapi import APIRouter, Body, HTTPException, status
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from services.errors import EntityDoesNotExist

router = APIRouter()


