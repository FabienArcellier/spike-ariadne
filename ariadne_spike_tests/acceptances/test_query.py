import unittest

from ariadne import graphql_sync

from ariadne_spike import query


class QueryTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_graphql_schema_of_query_is_valid(self):
        # Assign
        # Acts
        schema = query.type_def()
        # Assert

    def test_user_should_work_without_argument(self):
        schema = query.schema()

        # Acts
        success, result = graphql_sync(schema, {"query": '{ user { name, age } }'})

        # Assert
        self.assertTrue(success)
        self.assertEqual(result['data']['user']['name'], 'My name is stranger !')

    def test_user_should_accept_name_argument(self):
        # Assign
        schema = query.schema()

        # Acts
        success, result = graphql_sync(schema, {"query": '{ user(name:"Fabien") { name, age } }'})

        # Assert
        self.assertTrue(success)
        self.assertEqual(result['data']['user']['name'], f'My name is Fabien !')

    def test_user_should_accept_age_argument(self):
        # Assign
        schema = query.schema()

        # Acts
        success, result = graphql_sync(schema, {"query": '{ user(age:24) { name, age } }'})

        # Assert
        self.assertTrue(success)
        self.assertEqual(result['data']['user']['age'], 24)
