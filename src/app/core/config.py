import os

from typing import Dict
from urllib.parse import quote

from pydantic import BaseSettings


# PROJECT ROOT 상대경로
PROJECT_ROOT: str = os.path.dirname(
    os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
LOG_DIR = os.path.join(PROJECT_ROOT, 'src', 'logs')

class Settings(BaseSettings):
    
    HOST: str = "0.0.0.0"
    PORT: int = 8080
    DEBUG: bool = True
    
    # PROJECT_NAME
    PROJECT_NAME: str = "FASTAPI_BASIC"
    API_ENTRYPOINT: str = "/domain"
    
    # DB INFO Settings
    DB_URI_TEMPLATE: Dict[str, str] = {
        'SQLITE': "sqlite:///{}{}{}{}{}./myapi.db" # main.py 동일 경로에 myapi.db 위치
    }
    DB_CONNECTION_INFO: Dict[str, Dict[str, str]] = {
        'SQLITE': {
            'user': ''
            ,'pwd': ''
            ,'host': ''
            ,'port': ''            
            ,'database': ''
        },
    }

    def get_db_uri(
        self
        , uri_type: str
        , user: str
        , pwd: str
        , host: str
        , port: str
        , database: str
    ) -> str:
        """
        DB URI by DB TYPE

        Args:
            uri_type (str): DB TYPE
            user (str): user
            pwd (str): pwd
            host (str): host
            port (str): port
            database (str): database

        Returns:
            str: DB URI
        """
        return self.DB_URI_TEMPLATE[uri_type].format(
            user
            , quote(pwd)
            , host
            , port
            , database
        )    
    
settings = Settings()