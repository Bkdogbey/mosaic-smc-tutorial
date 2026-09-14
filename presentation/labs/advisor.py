"""Offline advisor integration: python labs/advisor.py.

A fixed controls reminder, not a tactical planner or correctness experiment.
"""
from mosaic.gui.main import SAREnvGUI
from mosaic.llm.client import LLMClient

from play import GUI_CONFIG, make_env


class ControlsAdvisor(LLMClient):
    """Return a controls reminder without a provider or network connection."""

    def query(self, prompt: str) -> str:
        return "Face a victim and press Tab to rescue. Use Space to open a door."


if __name__ == "__main__":
    env = make_env()
    try:
        SAREnvGUI(env, config=GUI_CONFIG, llm_client=ControlsAdvisor()).run()
    finally:
        env.close()
