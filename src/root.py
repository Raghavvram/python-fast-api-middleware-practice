from fastapi import APIRouter

# Initialize the router
router = APIRouter()

@router.get("/")
def return_root():
    return {"Message": "Backend is Running ...."}
