from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from models.base import Base


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    owner = Column(ForeignKey("users.id"), nullable=False, index=True)
