import os
import shutil
import subprocess
import pytest

# Define test directory
TEST_DIR = "test_project"


@pytest.fixture(scope="function")
def clean_test_dir():
    """Fixture to clean up the test directory after each test."""
    yield
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)


def run_cli_command(command):
    """Helper to run CLI commands and return the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


def test_init_project(clean_test_dir):
    """Test the `init` command of the CLI."""
    returncode, stdout, stderr = run_cli_command(f"fastapi-blueprint init {TEST_DIR}")

    assert os.path.exists(TEST_DIR), "Project directory was not created."
    assert os.path.exists(os.path.join(TEST_DIR, "app")), "App directory was not created."
    assert os.path.exists(os.path.join(TEST_DIR, "requirements.txt")), "requirements.txt was not created."
    assert os.path.exists(os.path.join(TEST_DIR, "main.py")), "main.py was not created."


def test_add_router(clean_test_dir):
    """Test the `add` command for adding a router."""
    # First, initialize the project
    run_cli_command(f"fastapi-blueprint init {TEST_DIR}")

    # Then, add a router
    returncode, stdout, stderr = run_cli_command(f"fastapi-blueprint add routers users {TEST_DIR}")

    router_path = os.path.join(TEST_DIR, "app", "routers", "users.py")

    assert os.path.exists(router_path), "Router file was not created."


def test_add_nonexistent_component_type(clean_test_dir):
    """Test the `add` command with an invalid component type."""
    # First, initialize the project
    run_cli_command(f"fastapi-blueprint init {TEST_DIR}")

    # Try adding an invalid component type
    returncode, stdout, stderr = run_cli_command(f"fastapi-blueprint add invalid_component test  {TEST_DIR}")

    assert "error" in stderr, "Expected an error message for invalid component type."


def test_project_initialization_twice(clean_test_dir):
    """Test initializing a project twice to see if it handles existing files correctly."""
    # Initialize the project once
    run_cli_command(f"fastapi-blueprint init {TEST_DIR}")

    # Initialize the project again
    returncode, stdout, stderr = run_cli_command(f"fastapi-blueprint init {TEST_DIR}")
    assert "already exists" in stdout.lower(), "Expected a warning about existing files."
