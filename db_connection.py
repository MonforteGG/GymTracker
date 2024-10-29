import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Conexión a la base de datos
TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL")
TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN")

# Crear el motor de SQLAlchemy
dbUrl = f"sqlite+{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true"


# Crear una sesión
engine = create_engine(dbUrl, connect_args={'check_same_thread': False}, echo=True)
Session = sessionmaker(bind=engine)
session = Session()