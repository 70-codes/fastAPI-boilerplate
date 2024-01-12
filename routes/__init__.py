from fastapi import APIRouter


def create_route(prefix, tags):
    return APIRouter(
        prefix=f"/api/v1/{prefix}",
        tags=[f"{tags}"],
    )
