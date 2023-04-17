"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("directory", [{"path": "/var/cyhy/admiral", "mode": "0o755"}])
def test_packages(host, directory):
    """Assert that the correct directory was created."""
    assert host.file(directory["path"]).exists
    assert host.file(directory["path"]).is_directory
    assert oct(host.file(directory["path"]).mode) == directory["mode"]


@pytest.mark.parametrize(
    "file",
    [
        {"path": "/var/cyhy/admiral/docker-compose.yml", "mode": "0o644"},
        {"path": "/var/cyhy/admiral/docker-compose-dev.yml", "mode": "0o644"},
    ],
)
def test_command(host, file):
    """Assert that the correct files exist."""
    assert host.file(file["path"]).exists
    assert host.file(file["path"]).is_file
    assert oct(host.file(file["path"]).mode) == file["mode"]
