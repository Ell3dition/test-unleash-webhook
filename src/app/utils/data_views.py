from sqlmodel import select
from sqlalchemy import update
from typing import Optional

from app.core.database import get_db_session
from app.models.data_views import Data_view


def get_data_view(schema: str) -> list[Data_view]:

    with get_db_session(schema) as session:
        statement = select(Data_view)
        results = session.exec(statement)
        data_views = results.all()
        return data_views


def create_data_view(schema: str, data_view: Data_view) -> Data_view:

    with get_db_session(schema) as session:
        session.add(data_view)
        session.commit()
        session.refresh(data_view)
        return data_view


def change_status_data_view(
    schema: str, feature_id: int, status: bool
) -> Optional[Data_view]:
    with get_db_session(schema) as session:
        statement = (
            update(Data_view)
            .where(Data_view.feature_id == feature_id)
            .values(status=status)
        )
        session.exec(statement)
        session.commit()

        select_statement = select(Data_view).where(Data_view.feature_id == feature_id)
        data_view = session.exec(select_statement).first()

        if not data_view:
            raise ValueError(f"No se encontró un Data_view con feature_id={feature_id}")

        return data_view
