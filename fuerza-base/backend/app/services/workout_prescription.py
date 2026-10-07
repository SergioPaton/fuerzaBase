"""
WorkoutPrescription — creación, edición y calendarización de entrenamientos.
TODO: Migrar a caso de uso CreateWorkoutPlanUseCase.
"""
from app.schemas.workout_plan import WorkoutPlanCreate, WorkoutPlanResponse


class WorkoutPrescription:
    @staticmethod
    def create_plan(data: WorkoutPlanCreate) -> WorkoutPlanResponse:
        # TODO: implementar con repositorio
        raise NotImplementedError("Pendiente de implementación.")

