from cli import Argument, BaseCommand


class Command(BaseCommand):
    def get_arguments(self):
        return [
            Argument("a", is_argument=True),
            Argument("--n", is_argument=False, type=int),
        ]

    def run(self, *args, **kwargs):
        print("Command executed")
