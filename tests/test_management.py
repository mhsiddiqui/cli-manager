import unittest

from click.testing import CliRunner

from cli_manager import ManagementCommandSystem


class ManagementCommandSystemTestCases(unittest.TestCase):
    def test_management_command_system_registration(self):
        system = ManagementCommandSystem()
        system.register(package="tests.test_commands")
        self.assertEqual(len(system.commands), 1)

    def test_management_command_working(self):
        system = ManagementCommandSystem()
        system.register(package="tests.test_commands")
        runner = CliRunner()
        for command in system.commands:
            result = runner.invoke(command, ["a", "--n", 2])
            assert result.exit_code == 0
