"""Compare camera views: python labs/tweak.py."""
from mosaic.core.camera import AgentConeCamera, AgentFOVCamera, CameraConfig
from mosaic.gui.main import SAREnvGUI
from mosaic.sar.actions import RescueAction, RescueRewards

from play import GUI_CONFIG, make_env

CAMERA = "room"  # Change to "cone", save and restart.
FAKE_VICTIM_REWARD = -1.0  # Observable only if your placer adds decoys.


def make_condition():
    """Use the same map settings with another camera and rescue component."""
    cameras = {"room": AgentFOVCamera, "cone": AgentConeCamera}
    camera = cameras[CAMERA](config=CameraConfig(tile_size=32))
    rescue = RescueAction(rewards=RescueRewards(
        real_victim_alive=1.0,
        fake_victim=FAKE_VICTIM_REWARD,
        real_victim_dead=-2.0,
    ))
    return make_env(camera_strategy=camera, action=rescue)


if __name__ == "__main__":
    env = make_condition()
    try:
        SAREnvGUI(env, config=GUI_CONFIG).run()
    finally:
        env.close()
