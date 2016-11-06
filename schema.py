import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Department as DepartmentModel, Employee as EmployeeModel


class Department(graphene.ObjectType):
    class Meta:
        interfaces = (relay.Node, )
    name = graphene.String()

    @classmethod
    def get_node(cls, id, context, info):
        return db_session.query(DepartmentModel).first()

class Employee(graphene.ObjectType):
    class Meta:
        interfaces = (relay.Node, )
    name = graphene.String()
    departments = relay.ConnectionField(Department)
    def resolve_departments(slef, args, context, info):
        return []

    @classmethod
    def get_node(cls, id, context, info):
        return db_session.query(EmployeeModel).first()


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    employees = graphene.Field(Employee)

    def resolve_employees(self, args, context, info):
        return []


schema = graphene.Schema(query=Query)
