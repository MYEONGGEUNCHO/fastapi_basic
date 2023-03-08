from typing import List, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from domain.basic import basic_crud, basic_schema

router = APIRouter(
    prefix="/api/basic"
)

@router.get('/')
def basic_root():
    return {
        "message": "Hello World"
    }