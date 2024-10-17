import click
from typing import Any


class Argument:
    """
    Represents an argument for a command. This class can handle positional,
    keyword arguments, and prompts.
    """

    def __init__(
        self,
        *param_decls: str,
        is_argument: bool = False,
        **attrs: Any
    ):
        """
        :param param_decls: Name of the argument.
        :param is_argument: Data type of the argument (default: str).
        :param attrs: Whether the argument is required (default: False).
        """
        self.param_decls = param_decls
        self.is_argument = is_argument
        self.attrs = attrs

    def apply(self, click_decorator):
        """
        Apply the argument or option to the Click decorator based on its configuration.
        """
        if self.is_argument:
            click_decorator = click.argument(*self.param_decls, **self.attrs)(click_decorator)
        else:
            click_decorator = click.option(*self.param_decls, **self.attrs)(click_decorator)
        return click_decorator
