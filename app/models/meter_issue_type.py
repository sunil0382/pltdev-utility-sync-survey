from sqlalchemy import Column, String, BigInteger
from sqlalchemy.orm import relationship
from app.config.settings import SCHEMA
from app.database.base import Base


class MeterIssueType(Base):
    __tablename__ = "meter_issue_type"
    __table_args__ = {"schema": SCHEMA}

    issue_type_id = Column(BigInteger, primary_key=True, autoincrement=True)
    issue_type_name = Column(String(100), nullable=False, unique=True)

    issue_details = relationship(
        "MeterIssueDetail",
        primaryjoin="MeterIssueType.issue_type_id == MeterIssueDetail.issue_type_id",
        back_populates="issue_type",
    )

    def __repr__(self):
        return (
            f"<MeterIssueType(issue_type_id={self.issue_type_id}, "
            f"issue_type_name='{self.issue_type_name}')>"
        )
