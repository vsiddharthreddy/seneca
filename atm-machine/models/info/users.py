from sqlalchemy import Column
from sqlalchemy import String, Index

from models import BaseModel, CreatedMixin, ModifiedMixin


class User(BaseModel, CreatedMixin, ModifiedMixin):
    """ Table to store the user information """

    __tablename__ = "user"
    __table_args__ = (
        Index("idx_email_user", "email"),
        {"schema": "info"},
    )

    email = Column(String(256), nullable=False)
    phone_number = Column(String(256), nullable=False)
    full_name = Column(String(256), nullable=False)
