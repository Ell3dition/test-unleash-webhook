from sqlmodel import Field, SQLModel
from datetime import datetime


class Data_view(SQLModel, table=True):
    __tablename__ = "data_views"
    id_data_view: int = Field(default=None, primary_key=True, nullable=False)
    name: str = Field(nullable=False)
    code: str = Field(nullable=False)
    description: str = Field(nullable=False)
    feature_key: str = Field(nullable=False)
    path: str = Field(nullable=False)
    icon: str = Field(nullable=True)
    created_at: str = Field(nullable=False, default=datetime.now())
    updated_at: str = Field(nullable=True)
    deleted_at: str = Field(nullable=True)
    status: bool = Field(default=False, nullable=False)
    feature_id: int = Field(nullable=True)


# ALTER TABLE don_pollo.data_views ADD feature_key varchar(50) NULL;
# ALTER TABLE don_pollo.data_views ADD "path" varchar(50) NULL;
# ALTER TABLE don_pollo.data_views ADD icon varchar(100) NULL;
# ALTER TABLE don_pollo.data_views ADD status boolean DEFAULT false NOT NULL;
# ALTER TABLE don_pollo.data_views ADD feature_id numeric NULL;

# ENVDATA01
# FOODDATA01
