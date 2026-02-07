from .handler import router as handler_router
from .start import router as start_router


routers = [start_router, handler_router]