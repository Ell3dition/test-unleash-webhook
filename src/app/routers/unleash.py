import json
from fastapi import APIRouter, HTTPException, Request
from app.schemas.unleash import WebhookSchema, FeatureEvent
from app.core.constants import (
    FEATURE_CREATED,
    FEATURE_ENABLED,
    FEATURE_DISABLED,
)
from app.utils.getClientsByName import get_client_by_name
from app.utils.data_views import change_status_data_view, create_data_view
from app.models.data_views import Data_view

router = APIRouter(
    prefix="/unleash",
    tags=["unleash"],
)


@router.post("/webhook")
async def handle_webhook(request: Request):
    try:
        request_json = await request.json()

        feature_event = FeatureEvent(**request_json)

        client = get_client_by_name(feature_event.client)

        if feature_event.event_type == FEATURE_CREATED:
            create_data_view(
                client.db_schema,
                data_view=Data_view(
                    **{
                        "name": feature_event.name,
                        "code": feature_event.name,
                        "description": feature_event.description,
                        "feature_key": feature_event.feature_name,
                        "path": feature_event.path,
                        "icon": feature_event.icon,
                        "feature_id": feature_event.feature_id,
                        "status": False,
                    }
                ),
            )
        elif feature_event.event_type == FEATURE_ENABLED:
            change_status_data_view(
                client.db_schema, feature_event.feature_id, status=True
            )
        elif feature_event.event_type == FEATURE_DISABLED:
            change_status_data_view(
                client.db_schema, feature_event.feature_id, status=False
            )
        return {"status": "success", "message": "Webhook procesado correctamente"}

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, detail=f"Error procesando el webhook: {str(e)}"
        )
