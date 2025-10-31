A lightweight Python library for simulating keyboard and mouse input in Wayland environments, implemented as a wrapper around the ydotool command-line utility.

This package provides a simple, Pythonic way to interact with your Wayland session for automation, testing, and scripting purposes.

🚀 Installation and Setup

1. Prerequisites

This library acts as a wrapper for the ydotool command-line utility. You must install ydotool and its daemon, ydotoold, which is essential for creating virtual input devices.
Component	Installation Command
Python 3.x	Usually pre-installed.

ydotool (Ubuntu/Debian)	
```
sudo apt update && sudo apt install ydotool
```
ydotool (Fedora)	
```
sudo dnf install ydotool
```
ydotool (Arch Linux)	
```
sudo pacman -S ydotool
```
2. Run the ydotool Daemon (ydotoold)

The automation commands will not work unless the background daemon, ydotoold, is running. The daemon requires special permissions to access /dev/uinput.

Recommended Method (Systemd User Service)

The cleanest way is to use the systemd user service that comes with ydotool:

# Enable and start the ydotoold daemon for your user
```Bash
systemctl --user enable ydotoold.service
systemctl --user start ydotoold.service
```
Note: You might need to ensure your user is part of the input group or set up a udev rule to grant permission to /dev/uinput if the user service fails. Consult the ydotool documentation for advanced configuration.

Quick Test Method (Troubleshooting)

You can manually launch the daemon in the background (may require sudo):
```Bash
sudo ydotoold &
```
3. Clone and Import the Library

Since your files are structured as a local package, clone the repository and import the modules:

```Bash
git clone https://github.com/weriaxoid/wayland-interction
cd https://github.com/weriaxoid/wayland-interction
```
You can now use the library by importing the package name: from wayland_interction import mouse, keyboard.

💻 Usage Examples

The package contains two main modules: mouse and keyboard.

Module: mouse.py (Mouse Automation)

This module handles cursor movement, clicking, and button presses/releases.
Function	Description	Mouse Code (for reference)
move(isAbsolute, x, y)	Moves the cursor. isAbsolute=True for screen coordinates, False for relative movement.	N/A
click(button, repeat=1)	Simulates a full click (press down and release). Supported buttons: 'left', 'right', 'middle'.	0xC0, 0xC1, 0xC2
press(button)	Presses and holds a mouse button down.	0x40, 0x41, 0x42
release(button)	Releases a held mouse button.	0x80, 0x81, 0x82

Example: Basic Movement and Clicking

```python
from wayland_interction import mouse
import time

# 1. Absolute movement to screen center (e.g., 800x600)
print("Moving to (800, 600) in 2 seconds...")
time.sleep(2)
mouse.move(isAbsolute=True, x=800, y=600)

# 2. Triple Left Click
print("Performing a triple left click...")
time.sleep(1)
mouse.click(button='left', repeat=3)

# 3. Relative movement
print("Moving 100 pixels up and 50 right...")
mouse.move(isAbsolute=False, x=50, y=-100)
```
Example: Drag and Drop Simulation

```python
from wayland_interction import mouse
import time

print("Starting drag-and-drop simulation in 3 seconds...")
time.sleep(3)

# 1. Move to the source element
mouse.move(isAbsolute=True, x=300, y=400)
time.sleep(0.5)

# 2. Press and hold the LEFT button
print("Pressing and holding LEFT button...")
mouse.press('left') 
time.sleep(0.5)

# 3. Drag to the target location (500 pixels right)
print("Dragging 500 pixels to the right...")
mouse.move(isAbsolute=False, x=500, y=0) 
time.sleep(0.5)

# 4. Release the button
print("Releasing LEFT button.")
mouse.release('left')
```
Module: keyboard.py (Keyboard Automation)

This module handles text typing and single key presses. It includes an internal KEY_MAP to translate common key names (e.g., 'a', 'enter') to ydotool's KEY_ codes.
Function	Description
type(text, typing_speed, key_hold, escape)	Types a string. Parameters control speed, hold time, and escape sequences.
type_from_file(path, typing_speed, key_hold, escape)	Types the content of a file located at path.
press_key(key)	Simulates a single key press (press down and release). Accepts keys from the internal KEY_MAP (case-insensitive).

Example: Typing and Single Key Press


```python
from wayland_interction import keyboard
import time

# Wait for 3 seconds to let you focus on a text field
print("Typing in 3 seconds (please focus a window)...")
time.sleep(3)

# 1. Type a sentence with default speed
keyboard.type("Hello Wayland, this is automated input from Python!")

# 2. Press the ENTER key
print("Pressing ENTER...")
time.sleep(1)
keyboard.press_key('enter')

# 3. Type from a file (assuming 'notes.txt' exists)
# keyboard.type_from_file("/path/to/notes.txt")
```
Example: Simulating Hotkeys (Advanced)

Since your press_key function performs a full press-and-release, simulating a complex hotkey like Ctrl+C requires executing the raw ydotool commands using subprocess.

For true hotkeys, it is highly recommended to add separate key_down (:1) and key_up (:0) functions to keyboard.py.

Workaround for Hotkeys (Using Internal Key Map):

```python
from wayland_interction import keyboard
import time
import subprocess

def simulate_hotkey(key1: str, key2: str):
    """
    Simulates a key combination (HotKey) by executing raw ydotool commands
    to press and release keys in the correct sequence.
    """
    try:
        # Get key codes from the internal map
        k1_code = keyboard.KEY_MAP[key1.lower()]
        k2_code = keyboard.KEY_MAP[key2.lower()]
        
        # 1. Press both keys down (KEY:1)
        print(f"Pressing {key1} and {key2} down...")
        subprocess.Popen(f"ydotool key KEY_{k1_code}:1 KEY_{k2_code}:1", shell=True).wait()
        
        # 2. Release both keys (KEY:0)
        print(f"Releasing both keys...")
        subprocess.Popen(f"ydotool key KEY_{k2_code}:0 KEY_{k1_code}:0", shell=True).wait()

    except KeyError:
        print(f"Error: One or both keys ('{key1}', '{key2}') are not in the KEY_MAP.")
    except Exception as e:
        print(f"Hotkey execution error: {e}")


print("Attempting to press Ctrl+V in 3 seconds (Paste)...")
time.sleep(3)
simulate_hotkey('leftctrl', 'v')
```
