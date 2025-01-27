from sqlmodel import select
from app.core.database import get_db_session
from app.models.client import Client


def get_client_by_name(client_name: str) -> Client:

    with get_db_session("common") as session:
        statement = select(Client).where(Client.name == client_name)
        results = session.exec(statement)
        client = results.one()
        return client
