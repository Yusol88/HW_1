# app/api/rest/endpoints/tasks.py
router = APIRouter()

@router.post("/predict")
async def create_prediction(
    task_data: PredictionRequest,
    current_user: User = Depends(get_current_user)
):
    # Обработка запроса на предсказание