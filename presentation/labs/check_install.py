"""Verify imports, an environment step, RGB rendering and an advisor prompt."""
import platform
import sys
from importlib.metadata import version

from mosaic.llm.client import ask

from advisor import ControlsAdvisor
from play import make_env


def main():
    print("Python:", platform.python_version())
    print("Interpreter:", sys.executable)
    for package in ("mosaic", "minigrid", "pygame-ce", "pygame_gui", "tabulate"):
        print(f"{package}: {version(package)}")
    env = make_env()
    try:
        obs, reward, terminated, truncated, info = env.step(env.actions.left)
        frame = env.render()
        assert frame.ndim == 3 and frame.shape[2] == 3, "Expected an RGB frame"
        assert obs["remaining_victims"] > 0, "Expected real victims"
        print("Mission:", env.get_mission_status())
        print("Frame:", frame.shape)
        print("Advisor:", ask(obs, ControlsAdvisor(), prompt_type="sparse"))
        print("MOSAIC CHECK PASSED")
    finally:
        env.close()


if __name__ == "__main__":
    main()
