"""Minimal MOSAIC search-and-rescue mission used in Part Three.

Run from an active environment that has MOSAIC installed:

    python first_mission.py
"""

from mosaic.gui.main import SAREnvGUI
from mosaic.sar.env import build_sar_env
from mosaic.sar.placers import LavaPlacer, LockedRoomPlacer, VictimPlacer


env = build_sar_env(
    screen_size=720,
    num_rows=2,
    num_cols=2,
    room_size=8,
    victim_placer=VictimPlacer(num_real_victims=1),
    lava_placer=LavaPlacer(lava_per_room=1),
    locked_room_placer=LockedRoomPlacer(locked_room_prob=0.25),
)

gui = SAREnvGUI(
    env,
    config={"fullscreen": False, "max_time": 3},
)
gui.run()
