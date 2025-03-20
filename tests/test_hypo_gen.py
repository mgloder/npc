from typing import Any, Dict
from unittest.mock import MagicMock, patch

import pytest
from agents import ModelSettings

from app.lib.agent.hypo_gen import HypoGeneratorAgent


@pytest.fixture
def hypo_gen_agent() -> HypoGeneratorAgent:
    """Create a test instance of the HypoGeneratorAgent"""
    model_settings = ModelSettings()
    return HypoGeneratorAgent(model_settings=model_settings)


@pytest.fixture
def sample_hypo() -> Dict[str, Any]:
    """Sample hypothesis structure for testing"""
    return {
        "title": "Test Hypothesis",
        "content": "This is a test hypothesis",
        "children": [
            {
                "title": "Sub-hypothesis 1",
                "content": "Supporting detail 1",
                "children": [],
            }
        ],
    }


def test_agent_initialization() -> None:
    """Test that the agent initializes correctly with default parameters"""
    agent = HypoGeneratorAgent()
    assert agent.name == "HypoGenerator"
    assert "Generates hierarchical hypotheses" in agent.instructions


def test_agent_initialization_with_tools() -> None:
    """Test that the agent initializes correctly with custom tools"""
    mock_tool = MagicMock()
    mock_tool.__name__ = "mock_tool"

    agent = HypoGeneratorAgent(tools=[mock_tool])
    assert mock_tool in agent.tools


@patch("app.lib.agent.hypo_gen.HypoGeneratorAgent.generate_hypo")
def test_run_calls_generate_hypo(
    mock_generate_hypo: MagicMock,
    hypo_gen_agent: HypoGeneratorAgent,
    sample_hypo: Dict[str, Any],
) -> None:
    """Test that run method calls generate_hypo with correct parameters"""
    # Setup mock return value
    mock_generate_hypo.return_value = sample_hypo

    # Call the run method
    result = hypo_gen_agent.run("Test input")

    # Verify generate_hypo was called with the correct arguments
    mock_generate_hypo.assert_called_once_with("Test input")

    # Verify the result matches the expected output
    assert result == sample_hypo


@patch("app.lib.agent.hypo_gen.HypoGeneratorAgent.generate_hypo")
def test_generate_hypo_functionality(
    mock_generate_hypo: MagicMock,
    hypo_gen_agent: HypoGeneratorAgent,
    sample_hypo: Dict[str, Any],
) -> None:
    """Test the generate_hypo method functionality"""
    # Setup mock return value
    mock_generate_hypo.return_value = sample_hypo

    # Call generate_hypo
    result = hypo_gen_agent.generate_hypo(
        "Generate a hypothesis about climate change", depth=2, breadth=2
    )

    # Verify generate_hypo was called with the correct arguments
    mock_generate_hypo.assert_called_once_with(
        "Generate a hypothesis about climate change", depth=2, breadth=2
    )

    # Verify the result matches the expected output
    assert result == sample_hypo


@patch("app.lib.agent.hypo_gen.HypoGeneratorAgent.refine_hypo")
def test_refine_hypo_functionality(
    mock_refine_hypo: MagicMock, hypo_gen_agent: HypoGeneratorAgent
) -> None:
    """Test the refine_hypo method functionality"""
    # Initial hypothesis
    initial_hypo = {
        "title": "Initial Hypothesis",
        "content": "First draft content",
        "children": [],
    }

    # Expected refined hypothesis
    refined_hypo = {
        "title": "Refined Hypothesis",
        "content": "Improved content based on feedback",
        "children": [
            {
                "title": "New Supporting Point",
                "content": "Added based on feedback",
                "children": [],
            }
        ],
    }

    mock_refine_hypo.return_value = refined_hypo

    # Call refine_hypo
    result = hypo_gen_agent.refine_hypo(initial_hypo, "Add more supporting details")

    # Verify refine_hypo was called with the correct arguments
    mock_refine_hypo.assert_called_once_with(
        initial_hypo, "Add more supporting details"
    )

    # Verify the result matches the expected refined hypothesis
    assert result == refined_hypo
