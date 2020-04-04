# pylint: disable=invalid-name,unused-argument
from typing import Any

from ariadne import gql, make_executable_schema, QueryType, ObjectType
from graphql import GraphQLSchema, GraphQLResolveInfo

from ariadne_spike.domain.user import User

query = QueryType()
user = ObjectType("User")


def type_def() -> str:
    return gql("""
        type Query {
            user(name: String, age: Int): User
        }
        
        type User {
            name: String
            age: Int
        }
    """)


class UserResolver:
    def __call__(self, obj: Any, info: GraphQLResolveInfo, name=None, age=None):
        return User(name, age)

query.create_register_resolver('user')(UserResolver())



@user.field("name")
def resolve_name(obj, info):
    return f'My name is {obj.name} !'


@user.field("age")
def resolve_age(obj, info):
    return obj.age


def schema() -> GraphQLSchema:
    return make_executable_schema(type_def(), [query, user])
