from sqlalchemy.orm import declarative_base

Base = declarative_base()

from backend.app.models.user import User
from backend.app.models.workout_plan import WorkoutPlan
from backend.app.models.feedback import Feedback
from backend.app.models.regulation_log import RegulationLog
