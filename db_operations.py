from datetime import datetime

from db_connection import session
from model import Usuario

def guardar_usuario(username, password, entreno_findes, dias_entreno_por_semana, chat_id):

    registered_at = datetime.now().date()

    nuevo_usuario = Usuario(
        chat_id=chat_id,
        username=username,
        password=password,
        entreno_findes=entreno_findes,
        dias_entreno_por_semana=dias_entreno_por_semana,
        registered_at=registered_at
    )

    session.add(nuevo_usuario)
    session.commit()
    session.close()
    print("Usuario guardado en la base de datos.")