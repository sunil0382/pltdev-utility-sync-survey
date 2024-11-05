import json
from fastapi import FastAPI
from fastapi.routing import APIRouter
from routes.utility_request_router import router as utility_request_router


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    with open("swagger/utility_request.swagger.json", "r") as f:
        app.openapi_schema = json.load(f)
    return app.openapi_schema


app = FastAPI(
    title="Utility API",
    description="API for managing utility requests",
    version="1.0.0",
    docs_url="/survey/docs",
    redoc_url="/redoc",
)
# Register API version 1 routers
v1_router = APIRouter(prefix="/survey/api/v1")
# v1_router.include_router(customer_router, prefix="/customers")
v1_router.include_router(utility_request_router)  # Register Utility Request Router
app.openapi = custom_openapi  # type: ignore[method-assign]

# Register all version routers to the main app
app.include_router(v1_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)
