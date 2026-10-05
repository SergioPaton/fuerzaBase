from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check_v2():
    return {"status": "ok", "version": "v2"}
