import subprocess
#need for key pressing
KEY_MAP = {
    "esc": "ESC",
    "escape": "ESC",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "0": "0",
    "minus": "MINUS",
    "equal": "EQUAL",
    "backspace": "BACKSPACE",
    "tab": "TAB",
    "q": "Q",
    "w": "W",
    "e": "E",
    "r": "R",
    "t": "T",
    "y": "Y",
    "u": "U",
    "i": "I",
    "o": "O",
    "p": "P",
    "leftbrace": "LEFTBRACE",
    "rightbrace": "RIGHTBRACE",
    "enter": "ENTER",
    "return": "ENTER",
    "a": "A",
    "s": "S",
    "d": "D",
    "f": "F",
    "g": "G",
    "h": "H",
    "j": "J",
    "k": "K",
    "l": "L",
    "semicolon": "SEMICOLON",
    "apostrophe": "APOSTROPHE",
    "grave": "GRAVE",
    "backslash": "BACKSLASH",
    "z": "Z",
    "x": "X",
    "c": "C",
    "v": "V",
    "b": "B",
    "n": "N",
    "m": "M",
    "comma": "COMMA",
    "dot": "DOT",
    "slash": "SLASH",
    "space": "SPACE",
    "capslock": "CAPSLOCK",
    "numlock": "NUMLOCK",
    "scrolllock": "SCROLLLOCK",
    "lctrl": "LEFTCTRL",
    "leftctrl": "LEFTCTRL",
    "rctrl": "RIGHTCTRL",
    "rightctrl": "RIGHTCTRL",
    "lshift": "LEFTSHIFT",
    "leftshift": "LEFTSHIFT",
    "rshift": "RIGHTSHIFT",
    "rightshift": "RIGHTSHIFT",
    "lalt": "LEFTALT",
    "leftalt": "LEFTALT",
    "ralt": "RIGHTALT",
    "rightalt": "RIGHTALT",
    "lmeta": "LEFTMETA",
    "leftmeta": "LEFTMETA",
    "rmeta": "RIGHTMETA",
    "rightmeta": "RIGHTMETA",
    "altgr": "RIGHTALT",
    "compose": "COMPOSE",
    "f1": "F1",
    "f2": "F2",
    "f3": "F3",
    "f4": "F4",
    "f5": "F5",
    "f6": "F6",
    "f7": "F7",
    "f8": "F8",
    "f9": "F9",
    "f10": "F10",
    "f11": "F11",
    "f12": "F12",
    "f13": "F13",
    "f14": "F14",
    "f15": "F15",
    "f16": "F16",
    "f17": "F17",
    "f18": "F18",
    "f19": "F19",
    "f20": "F20",
    "f21": "F21",
    "f22": "F22",
    "f23": "F23",
    "f24": "F24",
    "kpasterisk": "KPASTERISK",
    "kpslash": "KPSLASH",
    "kphome": "KP7",
    "kpup": "KP8",
    "kppageup": "KP9",
    "kpminus": "KPMINUS",
    "kpleft": "KP4",
    "kp5": "KP5",
    "kpright": "KP6",
    "kpplus": "KPPLUS",
    "kpend": "KP1",
    "kpdown": "KP2",
    "kppagedown": "KP3",
    "kpinsert": "KP0",
    "kpdelete": "KPDOT",
    "kpequal": "KPEQUAL",
    "kpenter": "KPENTER",
    "printscreen": "SYSRQ",
    "sysrq": "SYSRQ",
    "pause": "PAUSE",
    "linefeed": "LINEFEED",
    "home": "HOME",
    "up": "UP",
    "pageup": "PAGEUP",
    "left": "LEFT",
    "right": "RIGHT",
    "end": "END",
    "down": "DOWN",
    "pagedown": "PAGEDOWN",
    "insert": "INSERT",
    "delete": "DELETE",
    "macro": "MACRO",
    "mute": "MUTE",
    "volumedown": "VOLUMEDOWN",
    "volumeup": "VOLUMEUP",
    "power": "POWER",
    "scale": "SCALE",
    "stop": "STOP",
    "again": "AGAIN",
    "undo": "UNDO",
    "copy": "COPY",
    "open": "OPEN",
    "paste": "PASTE",
    "cut": "CUT",
    "help": "HELP",
    "menu": "MENU",
    "sleep": "SLEEP",
    "wakeup": "WAKEUP",
    "www": "WWW",
    "mail": "MAIL",
    "back": "BACK",
    "forward": "FORWARD",
    "nextsong": "NEXTSONG",
    "playpause": "PLAYPAUSE",
    "prevsong": "PREVIOUSSONG",
    "stopcd": "STOPCD",
    "record": "RECORD",
    "rewind": "REWIND",
    "refresh": "REFRESH",
    "exit": "EXIT",
    "brightnessdown": "BRIGHTNESSDOWN",
    "brightnessup": "BRIGHTNESSUP",
    "micmute": "MICMUTE",
    "displaytoggle": "DISPLAYTOGGLE",
    "screenlock": "SCREENLOCK",
    "leftclick": "BTN_LEFT",
    "rightclick": "BTN_RIGHT",
    "middleclick": "BTN_MIDDLE",
    "forwardbutton": "BTN_FORWARD",
    "start": "BTN_START",
    "select": "BTN_SELECT",
}

def type(text : str, typing_speed : int = 20, key_hold : int = 20, escape : bool = True):
    try:
        process = subprocess.Popen(f'ydotool type --key-delay {typing_speed} --key-hold {key_hold} --escape {escape} "{text}"', shell=True)
        process.wait()
    except Exception as e:
        print(f"error: {e}")
    except KeyboardInterrupt:
        print("exiting..")
    finally:
        process.terminate()

        try:
            process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            process.kill()
  
def type_from_file(path : str, typing_speed : int = 20, key_hold : int = 20, escape : bool = True):
    try:
        process = subprocess.Popen(f'ydotool type --key-delay {typing_speed} --key-hold {key_hold} --escape {escape} --file="{path}"', shell=True)
        process.wait()
    except Exception as e:
        print(f"error: {e}")
    except KeyboardInterrupt:
        print("exiting..")
    finally:
        process.terminate()

        try:
            process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            process.kill()

def press_key(key : str):
    try:
        if key.lower() in KEY_MAP:
            formated_key = f"KEY_{KEY_MAP[key.lower()]}"
            print(formated_key)
        else:
            print(f"unexcepted key: {key}")
            return
    
        proc = subprocess.Popen(f"ydotool key --key-delay=0 '{formated_key}'", shell=True)
        proc.wait()
    except Exception as e:
        print(f"error: {e}")
    except KeyboardInterrupt:
        print("exiting..")
    finally:
        proc.terminate()

        try:
            proc.wait(timeout=2)
        except subprocess.TimeoutExpired:
            proc.kill()
__import__('time').sleep(1)
press_key("q")





