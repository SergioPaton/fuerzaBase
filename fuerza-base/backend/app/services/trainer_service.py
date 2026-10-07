"""
TrainerService — gestión de cartera de atletas y asignación de planes.
TODO: Migrar a caso de uso TrainerUseCase cuando se implemente.
"""
from typing import List

from app.schemas.user import UserResponse
from app.schemas.workout_plan import WorkoutPlanCreate, WorkoutPlanResponse


class TrainerService:
    @staticmethod
    def get_clients(trainer_id: int) -> List[UserResponse]:
        # TODO: implementar con repositorio
        return []

    @staticmethod
    def assign_plan(trainer_id: int, plan: WorkoutPlanCreate) -> WorkoutPlanResponse:
        # TODO: implementar con CreateWorkoutPlanUseCase
        raise NotImplementedError("Pendiente de implementación.")

