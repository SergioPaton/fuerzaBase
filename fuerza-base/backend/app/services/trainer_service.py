from typing import List
from backend.app.models import User, WorkoutPlan
from backend.app.schemas import UserResponse, WorkoutPlanResponse

class TrainerService:
    @staticmethod
    def get_clients(trainer_id: int) -> List[UserResponse]:
        # placeholder logic
        return []

    @staticmethod
    def assign_plan(trainer_id: int, plan: WorkoutPlanCreate) -> WorkoutPlanResponse:
        # placeholder logic
        return WorkoutPlanResponse()
