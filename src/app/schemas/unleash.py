from pydantic import BaseModel, HttpUrl


class FeatureEvent(BaseModel):
    feature_id: int
    environment: str
    client: str
    name: str
    feature_name: str
    event_type: str
    path: str
    icon: str
    description: str


class WebhookSchema(BaseModel):
    url: HttpUrl
    body: str
    contentType: str
