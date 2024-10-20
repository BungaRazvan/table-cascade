import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ChangeHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.last_modified_time = time.time()

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            current_time = time.time()

            if current_time - self.last_modified_time > 1:
                print(f"File changed: {event.src_path}")
                self.last_modified_time = current_time
                run_script()


def run_script():
    result = subprocess.run(
        ["poetry", "run", "python", "main.py"], 
        capture_output=True,
        text=True,
    )
    print(result.stdout)

    if result.stderr:
        print(f"Error: {result.stderr}")


if __name__ == "__main__":
    run_script()
    path = "."
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    print("Watching for changes...")
    observer.start()  # Start the observer
    try:
        while True:
            time.sleep(1) 
    except KeyboardInterrupt:
        observer.stop()
    observer.join()