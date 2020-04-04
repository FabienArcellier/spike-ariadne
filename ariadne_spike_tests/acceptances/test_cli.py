# coding=utf-8

import unittest

from click.testing import CliRunner

from ariadne_spike.cli import cli



class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_main_exit_with_1_as_error_code_if_action_fails(self):
        # Assign
        runner = CliRunner()

        # Acts
        result = runner.invoke(cli, ['command1', '--name', 'fabien'])

        # Assert
        self.assertEqual(result.exit_code, 0)
        self.assertEqual('fabien\n', result.output)
