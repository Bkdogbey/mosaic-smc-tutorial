"""Record three scripted turns, not a human session: python labs/record.py."""
import json
from pathlib import Path

from play import make_env


if __name__ == "__main__":
    env = make_env()
    output = Path("recordings/demo.jsonl")
    output.parent.mkdir(exist_ok=True)
    try:
        with output.open("w", encoding="utf-8") as stream:
            for action in (env.actions.left, env.actions.right, env.actions.left):
                obs, reward, terminated, truncated, info = env.step(action)
                record = dict(obs, action=int(action), reward=float(reward),
                              terminated=bool(terminated), truncated=bool(truncated),
                              events=info.get("events", []))
                stream.write(json.dumps(record) + "\n")
                if terminated or truncated:
                    break
        print(f"Saved {output}. This is a scripted three-action trace.")
    finally:
        env.close()
