"""
AutoGenerationEngine — generación automática de rutinas iniciales desde cuestionario.
TODO: Migrar a caso de uso con lógica de generación real.
"""
from app.schemas.workout_plan import WorkoutPlanCreate, WorkoutPlanResponse


class AutoGenerationEngine:
    @staticmethod
    def generate_from_profile(profile_data: dict) -> WorkoutPlanResponse:
        # TODO: implementar generación desde perfil del atleta
        raise NotImplementedError("Pendiente de implementación.")

