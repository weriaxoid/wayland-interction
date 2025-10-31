import subprocess

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







