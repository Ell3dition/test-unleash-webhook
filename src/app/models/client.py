from sqlmodel import Field, SQLModel


class Client(SQLModel, table=True):
    __tablename__ = "clients"
    id_client: int = Field(default=None, primary_key=True, nullable=False)
    name: str = Field(nullable=False)
    db_schema: str = Field(nullable=False)
    envs_prefix: str = Field(nullable=False)
    deleted_at: str = Field(nullable=True)
