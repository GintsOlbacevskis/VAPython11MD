import time
import signal
import sys

def long_running_task():
    print("Starting a long task. Press 'Ctrl+C' to exit gracefully.")
    try:
        for i in range(1, 101):  # Simulate a task with 100 steps
            print(f"Processing step {i}/100...")
            time.sleep(1)  # Simulate processing time 1sec
    except KeyboardInterrupt:
        print("\nGraceful shutdown initiated. Exiting...")
        sys.exit(0)  # Exit without error

def signal_handler(sig, frame):
    print("\nSIGINT received. Exiting gracefully...")
    sys.exit(0)

# Main program
if __name__ == "__main__":
    # Register signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)

    # Execute the long-running task
    long_running_task()