# Eye-Tracker Demo: Machine Setup

A checklist for getting any machine ready for the live eye-tracking demo
(slide 33). Do the steps in order; each ends with a check. Allow 30 minutes on
a new machine.

## What the machine needs

- **Python 3.10 exactly.** The Tobii SDK (`tobii-research` 2.1.0) is built only
  for Python 3.10, on Windows, macOS 14+, and Linux.
- The Tobii tracker on USB, mounted under the screen the game will run on.
- Internet for the installs. No API key.

## 1 · Tobii software (admin rights)

The tracker is a **Tobii Pro Spark**. It needs two installs, both for your
operating system:

1. **Tobii Pro Spark runtime** (the driver), from
   <https://connect.tobii.com/s/spark-downloads>. Without it the tracker shows
   on USB but no software can find it.
2. **Tobii Pro Eye Tracker Manager**, to set which screen the tracker is
   mounted under.

On Ubuntu 22.04, with the runtime `.deb` downloaded:

```bash
sudo apt install ./TobiiProSpark_2.2.3.0_x64.deb
wget https://s3-eu-west-1.amazonaws.com/tobiipro.eyetracker.manager/linux/TobiiProEyeTrackerManager-2.7.2.deb
sudo apt install ./TobiiProEyeTrackerManager-2.7.2.deb
```

Unplug and replug the tracker, then open Eye Tracker Manager and set the
screen.

✓ **Check:** the tracker appears in Eye Tracker Manager with its serial number.
If it does not, stop here: nothing below can work.

## 2 · Code and environment

MOSAIC and the lab's `ixp` package go side by side in one folder.

```bash
git clone https://github.com/iHuman-Lab/mosaic.git
git clone https://github.com/iHuman-Lab/ixp.git
conda create --name mosaic_demo python=3.10 -y
conda activate mosaic_demo
cd mosaic
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install tobii-research pylsl ray psychopy ujson beartype icontract pydantic
python -m pip install --no-deps --ignore-requires-python -e ../ixp
python -m pip uninstall -y pygame
python -m pip install --force-reinstall "pygame-ce>=2.5.2"
```

Two lines are deliberate:

- `--no-deps --ignore-requires-python` for `ixp`: it asks for Python 3.11, which
  the Tobii SDK cannot use, and it lists plain `pygame`, which breaks MOSAIC's
  window.
- The last two lines must come last. Run them again if any later install puts
  `pygame` back.

✓ **Check:**

```bash
python -c "import mosaic.gui.main, ixp.experiment, psychopy.visual; print('demo ready')"
```

## 3 · Can Python see the tracker?

```bash
python -c "import tobii_research as t; print(t.find_all_eyetrackers())"
```

✓ **Check:** the list is not empty. An empty list means step 1 is not finished.

## 4 · Two edits for the demo

**`src/experiment/experiment.py`** — in the `sar_experiment_test` block, change
`"skip"` to `"run"` and add the sensor calls (the same edit slide 33 shows).
Change `instruction_test` from `"run"` to `"skip"`.

```python
with skip_run("run", "sar_experiment_test") as check, check():
    ray.init(ignore_reinit_error=True, _system_config={"metrics_report_interval_ms": 0})
    experiment = Experiment(config)
    experiment.register_sensor(
        name="TobiiEyeTracker", sensor_cls=TobiiEyeTracker, sensor_config={"config": {}}
    )
    experiment.calibrate_sensor(
        "TobiiEyeTracker", screen=config["display"], fullscreen=config["fullscreen"]
    )

    experiment.add_task(
```

**`configs/experiment.yaml`** — set `display:` (top line) to the number of the
screen the tracker sits under (`0` is the first screen), and under `game:` set
`max_time: 2` so each trial is short.

## 5 · Run it

Start from the `mosaic` folder with `mosaic_demo` active.

```bash
PYTHONPATH=src python -m experiment.experiment
```

Windows PowerShell: `$env:PYTHONPATH = "src"`, then `python -m experiment.experiment`.

1. **Calibration:** five dots. Look at each. `Space` accepts, `R` redoes.
2. **Play:** three short trials in random order. `Esc` ends the current trial.
   No API key is used, so in two of the trials `Alt` shows an error in the chat
   instead of advice. That is expected; the game and the recording carry on.
3. **Show both streams:** in a second terminal (same environment), while a
   trial is running:

   ```bash
   python -c "import pylsl; [print(s.name(), '|', s.type(), '|', s.nominal_srate(), 'Hz') for s in pylsl.resolve_streams(2)]"
   ```

   ✓ **Check:** `TobiiEyeTracker | Gaze | 60.0 Hz` and the game stream. LabRecorder
   shows the same list if you prefer it on screen.

## If something fails

| Symptom | Fix |
| --- | --- |
| `find_all_eyetrackers()` prints `[]` | Step 1: the tracker must appear in Eye Tracker Manager first. Replug the USB cable. |
| `No eye trackers found` when the demo starts | Same as above. |
| `cannot import name 'DIRECTION_LTR'` | Rerun the last two install lines of step 2. |
| `No module named 'experiment'` | Run from the `mosaic` folder with `PYTHONPATH=src`. |
| `No module named 'ixp.experiment'` | `ixp` was cloned but not installed. Rerun its install line from step 2. |
| `Package 'ixp' requires a different Python` | The `--ignore-requires-python` flag is missing. |
| Calibration opens on the wrong screen | Change `display:` in `configs/experiment.yaml`. |
| The tracker fails on the day | Show the rehearsal screenshot of the stream list and move on. |

## Not yet tested

Step 2 was tested from scratch on Ubuntu 22.04 with Python 3.10 (fresh clones,
new environment, every demo import loads). Steps 1, 3, 4 and 5 were written
from the code and have not been run with a tracker while preparing this
checklist. Rehearse them on the actual demo machine.
