from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID, uuid4
from sqlalchemy import ForeignKey
from src.booking_app.enums import PaymentStatus
from src.core.models import Base
from src.core.models.base import (
    str_300,
    created_at,
    updated_at,
    datetime_column,
)


class Booking(Base):
    confirmation_id: Mapped[UUID] = mapped_column(default=uuid4, nullable=True)
    description: Mapped[str_300] = mapped_column(nullable=True)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    payment_status: Mapped[PaymentStatus] = mapped_column(nullable=True)
    payment_time: Mapped[datetime_column] = mapped_column(nullable=True)

    user_id = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    user: Mapped["User"] = relationship("User", back_populates="booking")
