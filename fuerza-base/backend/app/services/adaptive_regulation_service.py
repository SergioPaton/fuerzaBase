"""
AdaptiveRegulationService — regulación dinámica de cargas según feedback.
TODO: Migrar a caso de uso con motor de reglas cuando se implemente.
"""
from app.schemas.regulation_log import RegulationLogCreate, RegulationLogResponse


class AdaptiveRegulationService:
    @staticmethod
    def adjust_plan(plan_id: int, adjustment: RegulationLogCreate) -> RegulationLogResponse:
        # TODO: implementar motor de reglas
        raise NotImplementedError("Pendiente de implementación.")

