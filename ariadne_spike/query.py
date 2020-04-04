# pylint: disable=invalid-name,unused-argument

from ariadne import gql, make_executable_schema, QueryType
from graphql import GraphQLSchema

query = QueryType()


def type_def() -> str:
    return gql("""
        type Query {
            hello: String!
        }
    """)


@query.field("hello")
def resolve_hello(_, info):
    return "Hello stranger"


def schema() -> GraphQLSchema:
    return make_executable_schema(type_def(), query)
