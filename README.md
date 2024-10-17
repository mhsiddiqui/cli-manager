# FastAPI Commands Package

A FastAPI package that enables you to create and manage custom management commands, similar to Django's management system. This package uses Python's `click` to define, register, and execute commands for your FastAPI application dynamically.

## Features

- **Dynamic Command Registration:** Automatically discover and register commands located in specific directories.
- **Class-Based Commands:** Easily define reusable commands by subclassing `BaseCommand`.
- **Custom Arguments:** Commands can specify their own arguments and options, which will be automatically handled by the command-line interface.
- **Pluggable and Extendable:** Easily integrate this package with any FastAPI app or third-party package.

## Installation

Install the package via `pip`:

```bash
pip install fastapi-commands
```

## Usage

### 1. Define Your Command

To create a custom command, define a Python script in your project and subclass `BaseCommand`. Implement the `run` method to include your logic, and use `get_arguments` to specify any arguments the command will accept.

```python
# src/scripts/mycommand.py

from fastapi_commands import BaseCommand, Argument

class Command(BaseCommand):
    def get_arguments(self):
        return [
            Argument(name='arg1', type=str, required=True, is_positional=True),
            Argument(name='arg2', type=int, required=False, is_positional=False, prompt="Enter value for arg2"),
        ]

    def run(self, *args, **kwargs):
        print(f"Running command with args: {args}, kwargs: {kwargs}")
```

In this example, we define a command that requires one argument (`arg1`) and accepts an optional second argument (`arg2`). These arguments are passed to the `run` method for further processing.

### 2. Register Commands

In your main CLI runner file, use the `ManagementCommandSystem` to register and organize all your commands dynamically. This method discovers all commands within a specified package (like `src.scripts`) and registers them.

```python
# cli_runner.py

from fastapi_commands import ManagementCommandSystem
from fastapi import FastAPI

app = FastAPI()

# Initialize the management command system
management_system = ManagementCommandSystem(app=app)

# Register all commands in the 'src.scripts' package
management_system.register(package='src.scripts')

# Create the Click CLI group
cli = management_system.create_cli()

if __name__ == '__main__':
    cli()
```

This code sets up the command system and links the command logic to a FastAPI instance. All commands from the specified package (`src.scripts`) will automatically become available as CLI commands.

### 3. Run Commands

Once your commands are registered, you can run them using the CLI:

```bash
python cli_runner.py mycommand arg1_value --arg2 123
```

In this case, `mycommand` is the command name, and `arg1_value` and `--arg2 123` are the arguments passed to the command.

### 4. Using Management Commands from External Packages

If you have installed another FastAPI package with its own set of management commands, you can also register those commands in your CLI by specifying the package name.

```python
management_system.register(package='external_package.scripts')
```

To avoid command name conflicts between multiple packages, you can apply a prefix:

```python
management_system.register(prefix='ext-', package='external_package.scripts')
```

This way, all commands from `external_package` will be prefixed with `ext-`, avoiding any conflicts with similarly named commands in your project.

### 5. Adding Arguments Dynamically

The `get_arguments` method in `BaseCommand` allows each command to dynamically specify its own arguments. These are automatically added to the CLI when you register the command.

Each argument is defined as a dictionary with the following keys:

- `name`: The name of the argument.
- `type`: The data type of the argument (e.g., `str`, `int`, etc.).
- `required`: A boolean that indicates whether the argument is mandatory.

### Example Command

Here’s another example where you define a simple `greet` command:

```python
# src/scripts/greet.py

from fastapi_commands import BaseCommand

class Command(BaseCommand):
    def get_arguments(self):
        return [
            {'name': 'name', 'type': str, 'required': True},  # Required argument
        ]

    def run(self, name):
        print(f"Hello, {name}!")
```

Run the command using:

```bash
python cli_runner.py greet Alice
```

This will output:

```bash
Hello, Alice!
```

## Testing

To ensure the package works as expected, you can run tests using `pytest` or `tox` for multiple versions of Python and FastAPI.

### Setup Testing with `tox`

Install `tox` if you haven't already:

```bash
pip install tox
```

Run the tests:

```bash
tox
```

### Example Test Case

Here’s a sample test for command registration:

```python
# tests/test_management.py

from fastapi_commands import BaseCommand, ManagementCommandSystem
from fastapi import FastAPI

def test_command_registration():
    app = FastAPI()
    system = ManagementCommandSystem(app)

    class TestCommand(BaseCommand):
        def get_arguments(self):
            return [{'name': 'arg', 'type': str, 'required': True}]

        def run(self, *args, **kwargs):
            return "success"

    system.register_command("test_command", TestCommand)
    cli = system.create_cli()

    result = cli.invoke(["test_command", "example"])
    assert result.exit_code == 0
    assert "success" in result.output
```

## Continuous Integration with GitHub Actions

This package includes a GitHub Actions workflow to run tests automatically on multiple Python and FastAPI versions. The configuration can be found in `.github/workflows/ci.yml`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This version includes a more structured flow and better formatting to provide a clearer understanding of how to use the FastAPI commands package. Let me know if you need further modifications!