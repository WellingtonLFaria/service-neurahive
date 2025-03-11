from fastapi import APIRouter, Depends, Query
from schemas.example import GetExampleResponse, PostExampleRequest, DeleteExampleRequest
from schemas.basic_response import BasicResponse
from database import get_db
from sqlalchemy.orm import Session
from modules.example import CreateExample, GetExample, DeleteExample

router = APIRouter(prefix="/example")


@router.get("/")
def get_examples(
    session: Session = Depends(get_db),
) -> BasicResponse[list[GetExampleResponse]]:
    return GetExample(session).execute()


@router.post("/")
def post_example(
    example: PostExampleRequest,
    session: Session = Depends(get_db),
) -> BasicResponse[None]:
    return CreateExample(session, example).execute()


@router.delete("/")
def delete_example(
    example: DeleteExampleRequest = Query(), session: Session = Depends(get_db)
) -> BasicResponse[None]:
    return DeleteExample(session, example).execute()
