from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


# Definir el modelo de usuario
class Usuario(Base):
    __tablename__ = 'usuarios'

    chat_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    entreno_findes = Column(Boolean, nullable=False)
    dias_entreno_por_semana = Column(Integer, nullable=False)
    registered_at = Column(Date, nullable=False)

# Definir el modelo de entrenamientos
class Entrenamiento(Base):
    __tablename__ = 'entrenamientos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer)
    fecha = Column(Date)