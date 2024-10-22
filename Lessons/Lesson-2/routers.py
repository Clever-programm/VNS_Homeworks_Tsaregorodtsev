from fastapi import APIRouter, status

from schemas import StatusResponse, AccountRegisterSchema, AccountSchema, Role

status_router = APIRouter(prefix="/status")
accounts_router = APIRouter(prefix="/accounts", tags=["Аккаунты"])
USER: AccountSchema

@status_router.get('', summary="Получить статус сервера", tags=["Статус"])
def get_status() -> StatusResponse:
    return StatusResponse(status="ok")


@accounts_router.post('/register', summary="Регистрация нового аккаунта",
                      status_code=status.HTTP_201_CREATED)
def register(body: AccountRegisterSchema) -> AccountSchema:
    return AccountSchema(
        id=1,
        login=body.login,
        name=body.name,
        role=Role.USER
    )


@accounts_router.get('/my', summary="Получение данных своего аккаунта")
def register() -> AccountSchema:
    return AccountSchema(
        id=1,
        login="user1",
        name="Пася Вупкин",
        role=Role.USER
    )