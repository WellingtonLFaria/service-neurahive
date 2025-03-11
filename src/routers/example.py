from fastapi import APIRouter, Depends
from schemas.example import GetExampleResponse, PostExampleRequest
from schemas.basic_response import BasicResponse
from fastapi import status
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/example")


@router.get("/")
def get_examples(
    session: Session = Depends(get_db),
) -> BasicResponse[list[GetExampleResponse]]:
    return BasicResponse()


@router.post("/")
def post_example(
    example: PostExampleRequest,
    session: Session = Depends(get_db),
) -> BasicResponse[None]:
    return BasicResponse(
        message="Exemplo criado com sucesso", status_code=status.HTTP_201_CREATED
    )()
