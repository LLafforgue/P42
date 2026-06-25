import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--integration",
        action="store_true",
        default=False,
        help="Also run integration tests (requires a display and real asset files).",
    )


def pytest_collection_modifyitems(config, items):
    """Skip integration tests unless --integration flag is passed."""
    if config.getoption("--integration"):
        return  # run everything

    skip_integration = pytest.mark.skip(reason="Pass --integration to run these tests.")
    for item in items:
        if item.get_closest_marker("integration"):
            item.add_marker(skip_integration)
