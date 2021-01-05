from unittest.mock import Mock

from click.testing import CliRunner
import pytest
from pytest_mock import MockFixture
import requests

from test_poetry import console


@pytest.fixture
def runner() -> CliRunner:
    """ Fixture for invoking cli """
    return CliRunner()


@pytest.fixture
def mock_wikipedia_random_page(mocker: MockFixture) -> Mock:
    """Fixture for mocking wikipedia.random_page"""
    return mocker.patch("test_poetry.wikipedia.random_page")


def test_main_uses_specified_language(runner, mock_wikipedia_random_page):
    runner.invoke(console.main, ["--language=pl"])
    mock_wikipedia_random_page.assert_called_with(language="pl")


@pytest.mark.e2e
def test_main_succeeds_in_production_env(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0
