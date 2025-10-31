import subprocess

def move(isAbsolute : bool, x : int, y : int):
    try:
        if isAbsolute:
            proc = subprocess.Popen(f"ydotool mousemove --absolute {x} {y}", shell=True)
        if not isAbsolute:
            proc = subprocess.Popen(f"ydotool mousemove {x} {y}", shell=True)
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


def press(button: str):
    try:
        button_code = None
        if button == 'left':
            button_code = '0x40'
        elif button == 'right':
            button_code = '0x41'
        elif button == 'middle':
            button_code = '0x42'
        else:
            print(f'unexcepted button: {button}')
            return   
        proc = subprocess.Popen(f"ydotool click {button_code}", shell=True)
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


def release(button: str):
    try:
        button_code = None
        if button == 'left':
            button_code = '0x80'
        elif button == 'right':
            button_code = '0x81'
        elif button == 'middle':
            button_code = '0x82'
        else:
            print(f'unexcepted button: {button}')
            return   

        proc = subprocess.Popen(f"ydotool click {button_code}", shell=True)
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



def click(button: str, repeat: int = 1):
    try:
        button_code = None
        if button == 'left':
            button_code = '0xC0'
        elif button == 'right':
            button_code = '0xC1'
        elif button == 'middle':
            button_code = '0xC2'
        else:
            print(f'unexcepted button: {button}')
            return   

        proc = subprocess.Popen(f"ydotool click --repeat {repeat} --next-delay 0 {button_code}", shell=True)
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

