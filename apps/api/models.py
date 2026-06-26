from datetime import datetime, timezone
from sqlalchemy import String, DateTime, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Tle(Base):
    """
    SQLAlchemy model for the tle table
    Stores TLE data ingested from Celestrak
    """
    __tablename__ = "tle"

    id: Mapped[int] = mapped_column(primary_key=True)
    satellite_id: Mapped[str] = mapped_column(String(20))
    name: Mapped[str] = mapped_column(String(100))
    line1: Mapped[str] = mapped_column(String(69))
    line2: Mapped[str] = mapped_column(String(69))
    source_group: Mapped[str] = mapped_column(String(50))
    ingested_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)  # updated on every upsert, not the date of the first insertion
    )

    # a satellite can appear in multiple groups, uniqueness is defined for each pair (satellite, group)
    __table_args__ = (
        UniqueConstraint("satellite_id", "source_group"),
    )
