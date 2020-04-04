import unittest

from ariadne_spike import query


class QueryTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_graphql_schema_of_query_is_valid(self):
        # Assign
        # Acts
        schema = query.type_def()
        # Assert
