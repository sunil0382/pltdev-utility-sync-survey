from sqlalchemy import Column, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from app.config.settings import SCHEMA
from app.database.base import Base


class MeterIssueDetail(Base):
    __tablename__ = "meter_issue_detail"
    __table_args__ = {"schema": SCHEMA}

    issue_detail_id = Column(BigInteger, primary_key=True, autoincrement=True)
    issue_type_id = Column(
        BigInteger,
        ForeignKey(f"{SCHEMA}.meter_issue_type.issue_type_id"),
        nullable=False,
    )

    issue_detail_description = Column(String(150), nullable=False)

    issue_type = relationship(
        "MeterIssueType",
        primaryjoin="MeterIssueDetail.issue_type_id == MeterIssueType.issue_type_id",
        back_populates="issue_details",
    )

    def __repr__(self):
        return (
            f"<MeterIssueDetail(issue_detail_id={self.issue_detail_id}, "
            f"issue_detail_description='{self.issue_detail_description}', "
            f"issue_type_id={self.issue_type_id})>"
        )
