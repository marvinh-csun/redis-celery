from __future__ import annotations
from sqlalchemy import BigInteger, Column, DECIMAL, Index, Integer, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from db import db
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship


Base = db.Model

metadata = Base.metadata


from sqlalchemy.orm import registry

mapper_registry = registry()




    
t_business = Table(
        'business', metadata,
        Column('business_id', String(1024, 'utf8mb4_unicode_ci'), nullable=False, primary_key=True),
        Column('name', String(1024, 'utf8mb4_unicode_ci'), nullable=False),
        Column('address', String(1024, 'utf8mb4_unicode_ci'), nullable=False),
        Column('city', String(1024, 'utf8mb4_unicode_ci'), nullable=False),
        Column('state', String(1024, 'utf8mb4_unicode_ci'), nullable=False),
        Column('postal_code', String(1024, 'utf8mb4_unicode_ci'), nullable=False),
        Column('stars', DECIMAL(8, 2), nullable=False),
        Column('review_count', Integer, nullable=False),
        Column('is_open', Integer, nullable=False),
        Column('categories', String(1024, 'utf8mb4_unicode_ci'), nullable=False)
)
class Business:
    pass

mapper_registry.map_imperatively(Business, t_business)


class FailedJob(Base):
    __tablename__ = 'failed_jobs'

    id = Column(BIGINT, primary_key=True)
    uuid = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False, unique=True)
    connection = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    queue = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    payload = Column(LONGTEXT, nullable=False)
    exception = Column(LONGTEXT, nullable=False)
    failed_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class Migration(Base):
    __tablename__ = 'migrations'

    id = Column(INTEGER, primary_key=True)
    migration = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    batch = Column(Integer, nullable=False)


class PasswordResetToken(Base):
    __tablename__ = 'password_reset_tokens'

    email = Column(String(255, 'utf8mb4_unicode_ci'), primary_key=True)
    token = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    created_at = Column(TIMESTAMP)


class PersonalAccessToken(Base):
    __tablename__ = 'personal_access_tokens'
    __table_args__ = (
        Index('personal_access_tokens_tokenable_type_tokenable_id_index', 'tokenable_type', 'tokenable_id'),
    )

    id = Column(BIGINT, primary_key=True)
    tokenable_type = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    tokenable_id = Column(BIGINT, nullable=False)
    name = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    token = Column(String(64, 'utf8mb4_unicode_ci'), nullable=False, unique=True)
    abilities = Column(Text(collation='utf8mb4_unicode_ci'))
    last_used_at = Column(TIMESTAMP)
    expires_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


t_user_favorites = Table(
    'user_favorites', metadata,
    Column('business_id', String(1024,'utf8mb4_unicode_ci'), primary_key=True),
    Column('user_id', BigInteger,primary_key=True)
)

class UserFavorite:
    pass

mapper_registry.map_imperatively(UserFavorite,t_user_favorites)




class User(Base):
    __tablename__ = 'users'

    id = Column(BIGINT, primary_key=True)
    name = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    email = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False, unique=True)
    email_verified_at = Column(TIMESTAMP)
    password = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    remember_token = Column(String(100, 'utf8mb4_unicode_ci'))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)