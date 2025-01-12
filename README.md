# VAPython11MD

### Sigint.py
The signal.signal() function registers a custom handler (signal_handler) for the SIGINT signal, which is triggered when Ctrl+C is pressed

Python can also handle other operating system signals. Common ones include:
- SIGINT	Interrupt from keyboard (Ctrl+C).	Pressing Ctrl+C.
- SIGTERM	Termination signal.	Sent by kill or task managers.
- SIGHUP	Hangup signal (used for reloading configurations in daemons).	Terminal closure or nohup.
- SIGKILL	Forcefully kill the process (cannot be caught).	Sent by kill -9.
