from sqlalchemy.orm import Session
from schemas.example import GetExampleResponse
from schemas.basic_response import BasicResponse


class GetExample:
    def __init__(self, session: Session):
        self._session = session

    def execute(self) -> BasicResponse[list[GetExampleResponse]]:
        return self._session()


class CreateExample:
    def __init__(self):
        pass
