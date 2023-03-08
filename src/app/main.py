import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core.config import settings

# Domain Router
from domain.basic import basic_router

app = FastAPI(
    title=settings.PROJECT_NAME
    , openapi_url=f'{settings.API_ENTRYPOINT}/openapi.json'
)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(basic_router.router, tags=['Basic'])

if __name__ == '__main__':
    uvicorn.run(
        "main:app"
        , host=settings.HOST
        , port=settings.PORT
        
        # , debug=settings.DEBUG
        , reload=settings.DEBUG
    )