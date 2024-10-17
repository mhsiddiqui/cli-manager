from typing import List

import click

from cli import Argument, BaseCommand


class Command(BaseCommand):
    def get_arguments(self) -> List[Argument]:
        return [Argument("--name", is_argument=False, prompt="Your name please")]

    def run(self, *args, **kwargs):
        click.echo(f'My Name is {kwargs.get("name")}')
