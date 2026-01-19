"""Pytest configuration for Playwright tests"""
import pytest


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Force headless mode in CI by setting launch args"""
    return {
        **browser_type_launch_args,
        "headless": True,  # Always run headless
    }