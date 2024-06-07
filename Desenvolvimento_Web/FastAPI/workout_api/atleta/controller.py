from fastapi import APIRouter, Body, satus
from workout_api.atleta.schemas import AtletaIn

from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.post(
    '/', 
    summary='Criar atleta',
    status_code=status.HTTP_201_CREATED
)
async def post(
    db_session: DatabaseDependency, 
    atleta_in: AtletaIn = Body(...)
):
    pass