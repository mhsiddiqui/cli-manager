[![Build](https://github.com/mhsiddiqui/cli-manager/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/mhsiddiqui/cli-manager/actions/workflows/build.yml)

# Cli Manager

A Python package that enables you to create and manage custom management commands, similar to Django's management system for FastAPI, Flask and other similar frameworks. This package uses Python's `click` to define, register, and execute commands for your application dynamically.

## Features

- **Dynamic Command Registration:** Automatically discover and register commands located in specific directories.
- **Class-Based Commands:** Easily define reusable commands by subclassing `BaseCommand`.
- **Custom Arguments:** Commands can specify their own arguments and options, which will be automatically handled by the command-line interface.
- **Pluggable and Extendable:** Easily integrate this package with any FastAPI app or third-party package.

## Installation

Install the package via `pip`:

```bash
pip install cli-manager
```

## Usage

### 1. Define Your Command

To create a custom command, define a Python script in your project and subclass `BaseCommand`. Implement the `run` method to include your logic, and use `get_arguments` to specify any arguments the command will accept.

```python
# src/scripts/mycommand.py

from cli import BaseCommand, Argument

class Command(BaseCommand):
    def get_arguments(self):
        return [
            Argument('arg1', is_argument=True),
            Argument('--n', is_argument=False, type=int),
        ]

    def run(self, *args, **kwargs):
        print(f"Running command with args: {args}, kwargs: {kwargs}")
```

To Argument class accept all the parameters which `click.Argument` and `click.Option` accept. By using `is_argument=True/False`, both type of argument can be differentiated.


### 2. Register Commands

In your main CLI runner file, use the `ManagementCommandSystem` to register and organize all your commands dynamically. This method discovers all commands within a specified package (like `src.scripts`) and registers them.

```python
# cli_runner.py

from fastapi_commands import ManagementCommandSystem
from fastapi import FastAPI

# Initialize the management command system
management_system = ManagementCommandSystem()

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

Here’s another example where you define a simple `greet` command:

### Example

Example can be seen in example folder. This example can be run by running following command

```bash
python example_runner.py whats_my_name
```

## Authors
[@mhsiddiqui](https://github.com/mhsiddiqui)

## Contributing
Contributions are always welcome!

Please read contributing.md to get familiar how to get started.

Please adhere to the project's code of conduct.

Feedback And Support
Please open an issue and follow the template, so the community can help you.
