from cli import ManagementCommandSystem

system = ManagementCommandSystem()
system.register(package="example.scripts")
cli = system.create_cli()


if __name__ == "__main__":
    cli()
