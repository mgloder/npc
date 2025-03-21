import os

# Get the base directory for the agent module
AGENT_DIR = os.path.dirname(os.path.abspath(__file__))
# Define paths relative to the agent directory
CONFIG_DIR = os.path.join(AGENT_DIR, "..", "..", "config")


def get_config_path(filename: str) -> str:
    """
    Get the absolute path to a config file.

    Args:
        filename: Name of the config file

    Returns:
        Absolute path to the config file
    """
    return os.path.join(CONFIG_DIR, filename)
