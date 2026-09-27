import click


@click.group()
def cli():
    """A simple calculator CLI."""


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def add(a, b):
    """Add two numbers."""
    click.echo(a + b)


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def sub(a, b):
    """Subtract b from a."""
    click.echo(a - b)


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def mul(a, b):
    """Multiply two numbers."""
    click.echo(a * b)


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def div(a, b):
    """Divide a by b."""
    if b == 0:
        raise click.ClickException("Cannot divide by zero")
    click.echo(a / b)