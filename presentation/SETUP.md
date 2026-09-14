# MOSAIC tutorial setup and exercises

Use a laptop with a desktop display, terminal and text editor. The exercises need no API key, GPU or sensor hardware. Complete installation before the session if possible.

This guide targets **Python 3.12** and MOSAIC commit **a409222534dcd234dd2925a5adab8da9db17e6b2**. Earlier checks of the exercise behavior used Linux with Python 3.12.14. Rehearse on Windows and macOS before conference delivery.

## 1. Python and Git

### Windows

Install [Python 3.12](https://www.python.org/downloads/release/python-31210/) and [Git for Windows](https://git-scm.com/downloads/win). Include the Python launcher and PATH option if offered. Reopen PowerShell.

~~~powershell
py -3.12 --version
git --version
~~~

If typing python opens the Microsoft Store, use py -3.12 until the environment is active. If py is missing, add the launcher through the installer.

### macOS

Install [Python 3.12](https://www.python.org/downloads/release/python-31210/) and follow the [Git installation options](https://git-scm.com/downloads/mac). Apple's Command Line Tools are one route: run xcode-select --install, complete installation, and reopen Terminal.

~~~bash
python3.12 --version
git --version
~~~

### Ubuntu 24.04

~~~bash
sudo apt update
sudo apt install python3 python3-venv python3-pip git
python3 --version
git --version
~~~

Ubuntu 24.04 uses Python 3.12. On an older release, use a separately installed Python 3.12 interpreter with matching venv support, or a prepared Ubuntu 24.04 machine. Do not replace the system Python. Other distributions need their own package-manager commands.

**Checkpoint:** Python and Git both print version numbers.

## 2. Download both repositories

Run in a folder where you keep projects. Use a fresh workshop folder if an existing clone has local changes.

~~~bash
git clone https://github.com/Bkdogbey/mosaic.git
git clone https://github.com/Bkdogbey/mosaic-smc-tutorial.git
git -C mosaic-smc-tutorial switch tutorial/task-focused-redesign
cd mosaic
git checkout a409222534dcd234dd2925a5adab8da9db17e6b2
~~~

Detached HEAD is expected: the workshop selects a fixed software revision. Public clones do not need a GitHub account.

The folders must be siblings for the relative paths below:
- mosaic contains the software and its .venv environment.
- mosaic-smc-tutorial/presentation contains the slides and labs.

If using GitHub's Download ZIP instead, select the correct revision/branch and rename the extracted folders to these names.

## 3. Create and select a virtual environment

Run inside **mosaic**.

### Windows PowerShell

~~~powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
~~~

### Windows Command Prompt

~~~bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
~~~

### macOS

~~~bash
python3.12 -m venv .venv
source .venv/bin/activate
~~~

### Ubuntu 24.04

~~~bash
python3 -m venv .venv
source .venv/bin/activate
~~~

Check the selected interpreter:

~~~bash
python -c "import sys; print(sys.executable)"
~~~

**Checkpoint:** the path contains mosaic and .venv. Use python -m pip so installation targets this interpreter.

### PowerShell activation is blocked

Activation is optional. Use the venv Python directly for every command. This route covers installation, repair and first launch without changing execution policy:

~~~powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m pip install tabulate
.\.venv\Scripts\python.exe -m pip uninstall -y pygame
.\.venv\Scripts\python.exe -m pip install --force-reinstall pygame-ce==2.5.8
.\.venv\Scripts\python.exe -c "from mosaic.gui.main import SAREnvGUI; print('GUI imports OK')"
cd ../mosaic-smc-tutorial/presentation
..\..\mosaic\.venv\Scripts\python.exe labs/check_install.py
..\..\mosaic\.venv\Scripts\python.exe labs/play.py
~~~

Alternatively, use CMD activation.

## 4. Install the base package

Inside **mosaic**, with the venv selected:

~~~bash
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install tabulate
~~~

The editable install points to this source folder. tabulate supports the custom advisor's prompt builder. The base install does not include the full study framework.

### Graphics dependency repair

For this pinned revision:

~~~bash
python -m pip uninstall -y pygame
python -m pip install --force-reinstall pygame-ce==2.5.8
~~~

MOSAIC declares pygame, while MiniGrid and pygame_gui use pygame-ce. Both occupy the pygame import namespace. Removing pygame can delete shared files, so **keep --force-reinstall**.

The specific warning that mosaic requires pygame remains as a package-metadata conflict after this repair. Other dependency or installation failures need investigation. Installing MOSAIC dependencies again may restore plain pygame and require the repair again.

~~~bash
python -c "from mosaic.gui.main import SAREnvGUI; print('GUI imports OK')"
~~~

**Checkpoint:** GUI imports OK appears.

## 5. Verify the exercises

Keep the same terminal and environment:

~~~bash
cd ../mosaic-smc-tutorial/presentation
python labs/check_install.py
~~~

The checker prints versions, constructs a world, takes an action, renders an RGB frame and exercises the offline advisor. Expected final line:

~~~text
MOSAIC CHECK PASSED
~~~

Default requested victims: 2 × 2 × 2 = 8. The actual count can be lower in crowded configurations or after spawn-cell clearing. Inspect the actual mission output.

## 6. Play

From **mosaic-smc-tutorial/presentation**:

~~~bash
python labs/play.py
~~~

Click the window, press Left and confirm the agent turns. F11 toggles fullscreen; Esc closes.

| Key | Action |
| --- | --- |
| Up | Move forward |
| Left / Right | Turn in place |
| Space | Open or close the door in front; unlock using a matching key |
| Tab / Page Up | Rescue a victim or pick up a key in front |
| Left Shift / Page Down | Drop a key on a free tile in front |
| Alt | Request advice |
| Backspace | Generate another mission |
| F11 | Toggle fullscreen |
| Esc | Quit |

W is not mapped. Face objects before interacting. The default client in play.py returns “Currently, no commands are available.”

The basic GUI resets immediately after termination, including a lava collision. Its countdown is displayed but not enforced. Health depletion and experimental timing need additional study logic.

## Returning in a new terminal

From the common parent folder, select the existing environment. Do not reinstall.

**Windows PowerShell**

~~~powershell
.\mosaic\.venv\Scripts\Activate.ps1
cd mosaic-smc-tutorial/presentation
python labs/play.py
~~~

**macOS / Linux**

~~~bash
source mosaic/.venv/bin/activate
cd mosaic-smc-tutorial/presentation
python labs/play.py
~~~

For blocked PowerShell activation, enter presentation and use ..\..\mosaic\.venv\Scripts\python.exe instead of python.

## Exercises

### Rescue a victim

Run play.py. Plan a route, stand beside a real victim, face it and press Tab. Observe the saved count. Use an early rescue because the final one can immediately reset the map.

### Change the building

Edit NUM_ROWS and NUM_COLS in labs/play.py from 2 to 3, save, close and rerun. Predict the requested count, then compare it with the game. Restore 2×2 afterward.

Keep maps square on this revision. Use modest densities. Set LAVA_ENABLED=False to remove lava; a zero LAVA_PER_ROOM invokes random placement. Keep LOCKED_ROOM_PROB below 1.0; even zero locks one room in the current placer.

### Compare cameras

Run python labs/tweak.py with CAMERA="room", then CAMERA="cone". Restart each script with identical map settings and seed. Describe what disappears as you turn.

The script seeds both Python random and the environment, then the GUI performs another reset at launch. Fresh script launches repeat that initialization sequence. Backspace advances to another map. Save the actual initial state for research, not just a seed.

### Replace the advice text

Run python labs/advisor.py, move or turn once, then press Alt. Edit the returned sentence in ControlsAdvisor.query(), save and rerun.

This client supplies a fixed controls reminder. It does not assess route correctness or implement a calibrated reliability condition.

### Inspect a scripted trace

~~~bash
python labs/record.py
~~~

Open recordings/demo.jsonl. It contains three scripted turns with observations, actions, rewards, termination flags and events. Rerunning overwrites this demo file.

For human sessions, record actual GUI actions and timestamps before automatic resets. The full grid includes information outside the player's view. The observation image is MiniGrid encoding; env.render() supplies RGB.

## Troubleshooting

| Symptom | Action |
| --- | --- |
| Python or Git not found | Finish installation, reopen the terminal, use py -3.12 on Windows |
| ensurepip unavailable | Install matching venv support and recreate the incomplete environment |
| PowerShell blocks scripts | Use the direct venv interpreter or CMD activation |
| externally-managed-environment | Select the project venv rather than system Python |
| No module named mosaic | Check sys.executable and install from the MOSAIC folder with that interpreter |
| Cannot open labs/play.py | Change to mosaic-smc-tutorial/presentation |
| DIRECTION_LTR or missing pygame.surface | Repeat graphics repair with --force-reinstall |
| Missing tabulate | Install with the selected venv's python -m pip |
| No available video device | Use a desktop display; native Windows Python is the simplest Windows route |
| Window too large | Set SCREEN_SIZE=500 or use F11 |
| Alt gives a neutral reply | Expected in play.py; use advisor.py for a custom reply |
| Input pauses during advice | This GUI ignores keys while the advisor thread runs |
| Countdown expires but game continues | Base GUI behavior; implement the study stopping rule |
| Repeated generation messages | Ctrl+C and restore the small default map, modest densities and locking below 1 |
| FullviewCamera has no reset | Use EdgeFollowCamera, AgentFOVCamera or AgentConeCamera |
| ZeroDivisionError after a keypress | Keep llm_nudge_interval positive |
| Font warnings with a working window | Lazy font loading alone does not indicate installation failure |
| Network or package download failure | Check the first failed command and permitted network access; pair with a prepared laptop if needed |

For a report, include OS, Python version, interpreter path, MOSAIC commit, command and complete error. Do not include API keys.

## Optional study extensions

### Configuration ownership

The labs use Python constants, not configs/experiment.yaml. Environment settings, GUI settings and participant/session settings have different owners.

### Decoys, health and outcomes

Default VictimPlacer adds real victims with neutral initial health. The study-specific LavaRiskVictimPlacer in src/experiment/placers.py adds decoys and health tuning. src/experiment/game.py wires health updates and timing. Setting initial health alone does not make it decay.

RescueAction with RescueRewards changes penalty magnitudes. A decoy penalty requires decoys in the world. The current verifier checks removal of all real victims, including dead ones; define a living-rescue outcome separately if needed. Custom rescue handling also bypasses the normal MiniGrid step increment.

### External model providers

LLMClient is the reusable contract. src/experiment/llm.py contains LlamaIndex provider adapters. They require compatible provider packages, credentials and a model. The tutorial itself makes no external model calls.

For research, define what the prompt can see and log requests and responses. Evaluate correctness against an independent task oracle or annotations. A random label is not ground truth.

### Full study runner

The actual file is src/experiment/experiment.py, not experiment_main.py. It imports ixp, Ray and device-related packages. Arrange access to the lab framework and configure task blocks, sensors and imports first. Installing the experiment extra adds LlamaIndex but does not resolve every study dependency.

Run modules from the MOSAIC root because configuration paths are repository-relative. Expose src with PYTHONPATH=src on macOS/Linux or $env:PYTHONPATH = "src" in PowerShell.

### Replay

After recording the scripted trace, from presentation:

~~~bash
python ../../mosaic/src/experiment/replay.py recordings/demo.jsonl
~~~

The argument is a positional JSONL filename, not --file. Space pauses, Left/Right step while paused and Esc quits. Replay reconstructs an encoded map view, not the original GUI pixel for pixel.

## Links

- [Tutorial branch](https://github.com/Bkdogbey/mosaic-smc-tutorial/tree/tutorial/task-focused-redesign)
- [Pinned MOSAIC source](https://github.com/Bkdogbey/mosaic/tree/a409222534dcd234dd2925a5adab8da9db17e6b2)
- [MOSAIC documentation](https://ihuman-lab.github.io/mosaic/)
- [Python virtual environments](https://docs.python.org/3/library/venv.html)
