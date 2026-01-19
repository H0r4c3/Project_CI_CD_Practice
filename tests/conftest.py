"""Pytest configuration for Playwright tests"""
import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Force headless mode for all tests"""
    return {
        **browser_context_args,
    }


def pytest_addoption(parser):
    """Add custom command line options"""
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run tests in headed mode (with visible browser)"
    )