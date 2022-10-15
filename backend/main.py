from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from apis.general_pages.route_homepage import general_pages_router



def include_router(app: FastAPI):
    #add the imported router to app
    app.include_router(general_pages_router)


def configure_static(app):
    #add support for static files
    app.mount("/static", StaticFiles(directory="static"), name="static")


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    return app

app = start_application()

