import uvicorn

from server_updater.infrastructure.fastapi.endpoints.endpoints import app


def run_fastapi() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)
