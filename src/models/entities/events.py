from src.models.settings.base import Base
from sqlalchemy import Column

class Events(Base):
    __tablename__ = "events"