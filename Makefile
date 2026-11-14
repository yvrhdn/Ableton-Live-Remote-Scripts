# Makefile for Ableton Live Remote Scripts

# Clean up __pycache__ directories
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +

# Show the Live log, filtered to session starts, errors and script activity
LOG := $(HOME)/Library/Preferences/Ableton/Live 12.4.16/Log.txt
log:
	@cat "$(LOG)" | grep -iE --line-buffered '#######################################|Started: Live|error|traceback|exception|XjamMixer|ParksTool8ES'

# Default target
all: clean
