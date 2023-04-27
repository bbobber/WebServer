import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


association_table = sqlalchemy.Table(
    'association_goods',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('goods', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('goods.id')),
    sqlalchemy.Column('categorygoods', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('categorygoods.id'))
)


class Categorygoods(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'categorygoods'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)