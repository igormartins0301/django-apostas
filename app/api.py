from ninja import NinjaAPI
from lay0x1.api import router as events_router

api = NinjaAPI()

api.add_router("/predict/", events_router)
