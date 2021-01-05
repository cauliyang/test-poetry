from test_poetry import __version__
import click.testing
import pytest
from test_poetry import console


def test_version():
    assert __version__ == "0.1.0"


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0
