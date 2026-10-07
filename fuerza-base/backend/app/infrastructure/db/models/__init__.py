"""
Modelos ORM SQLAlchemy — capa de infraestructura.
Estos modelos son detalles de implementación: sólo la infraestructura los conoce.
"""
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Importar todos los modelos para que Alembic y create_all los detecte
from app.infrastructure.db.models.user import UserORM              # noqa: F401, E402
from app.infrastructure.db.models.workout_plan import WorkoutPlanORM  # noqa: F401, E402
from app.infrastructure.db.models.feedback import FeedbackORM      # noqa: F401, E402
from app.infrastructure.db.models.regulation_log import RegulationLogORM  # noqa: F401, E402
