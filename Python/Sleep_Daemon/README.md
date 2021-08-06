## Sleep Daemon
Tired of having to move your mouse to stop your system from idling? Python's got you covered. 
Just run this script and it will keep on moving the mouse and clicking it for you and provide the illusion we all need during WFH.

### Usage
```
cd Python/Sleep_Daemon
pip install -r requirements.txt

py no_sleep.py

# Press Ctrl+C to interrupt and take over control
```

Note - Try not leaving the script on for too long `pyautogui` has a failsafe for that and will kill your process. Best for a 30-40 min break.