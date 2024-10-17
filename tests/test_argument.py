import unittest
import click
from click.testing import CliRunner
from cli import Argument

class ArgumentTestCases(unittest.TestCase):

    def setUp(self):
        @click.command()
        def dummy_command(*args, **kwargs):
            click.echo('Dummy Command')

        self.command = dummy_command

    def test_argument_as_argument_with_one_option(self):


        # Testing Argument as a Click option
        arg = Argument('a', is_argument=True, nargs=1)
        command = arg.apply(self.command)

        assert isinstance(command, click.Command)
        runner = CliRunner()
        result = runner.invoke(command, ['John'])
        assert result.exit_code == 0

    def test_argument_as_argument_with_invalid_option(self):
        # Testing Argument as a Click option
        arg = Argument('a', is_argument=True, nargs=1)
        command = arg.apply(self.command)

        assert isinstance(command, click.Command)
        runner = CliRunner()
        result = runner.invoke(command, ['a', 'John', 'Smith'])
        assert result.exit_code == 2

    def test_argument_as_argument_with_n_options(self):
        # Testing Argument as a Click option
        arg = Argument('a', is_argument=True, nargs=-1)
        command = arg.apply(self.command)

        assert isinstance(command, click.Command)
        runner = CliRunner()
        result = runner.invoke(command, ['a'] * 5)
        assert result.exit_code == 0


    def test_argument_as_option(self):
        # Testing Argument as a Click positional argument
        arg = Argument('--n', is_argument=False, type=int)
        command = arg.apply(self.command)

        assert isinstance(command, click.Command)
        runner = CliRunner()
        result = runner.invoke(command, ['--n', 2])
        assert result.exit_code == 0


    def test_argument_prompt(self):
        # Testing prompt feature of Argument
        arg = Argument('--name', is_argument=False, prompt='Your name please')
        command = arg.apply(self.command)

        runner = CliRunner()
        result = runner.invoke(command, input='John\n')
        assert result.exit_code == 0
