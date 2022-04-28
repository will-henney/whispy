"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Whispy."""


if __name__ == "__main__":
    main(prog_name="whispy")  # pragma: no cover
