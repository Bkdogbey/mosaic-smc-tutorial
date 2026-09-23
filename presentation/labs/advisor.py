"""Plug your own AI teammate into MOSAIC.

    python labs/advisor.py

A teammate is anything with `query(prompt) -> str`. That means the quality,
timing, and correctness of AI advice is an experimental variable you control
in ~10 lines of Python, with no changes to the environment.
"""
import random

from mosaic.llm.client import LLMClient, ask


class ScriptedAdvisor(LLMClient):
    """A rule-free teammate whose advice is CORRECT with probability p.

    Set p = 1.0 for a reliable teammate, p = 0.0 for an unreliable one,
    or vary p across trials to study trust repair / reliance calibration.
    """

    DIRECTIONS = ["north", "south", "east", "west"]

    def __init__(self, p_correct: float = 1.0, seed: int = 0):
        self.p_correct = p_correct
        self.rng = random.Random(seed)
        self.log = []          # every piece of advice, for post-hoc analysis

    def query(self, prompt: str) -> str:
        correct = self.rng.random() < self.p_correct
        heading = self.rng.choice(self.DIRECTIONS)
        advice = (
            f"Head {heading} — there's a survivor in the next room."
            if correct
            else f"Nothing {heading} of you. Hold position and search here."
        )
        self.log.append({"correct": correct, "advice": advice})
        return advice


if __name__ == "__main__":
    from mosaic.sar.env import build_sar_env
    from mosaic.sar.placers import VictimPlacer

    env = build_sar_env(screen_size=600, num_rows=2, num_cols=2, room_size=8,
                        victim_placer=VictimPlacer(num_real_victims=2))
    obs, _ = env.reset(seed=0)

    advisor = ScriptedAdvisor(p_correct=0.7, seed=42)
    for _ in range(5):
        obs, reward, terminated, truncated, info = env.step(2)   # 2 = move forward
        print(ask(obs, advisor, prompt_type="sparse"))

    n_ok = sum(a["correct"] for a in advisor.log)
    print(f"\n{n_ok}/{len(advisor.log)} pieces of advice were correct")

    # To use it in the live game instead:
    #   from mosaic.gui.main import SAREnvGUI
    #   SAREnvGUI(env, config={"fullscreen": False}, llm_client=advisor).run()
