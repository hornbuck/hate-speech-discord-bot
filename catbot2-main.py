# Discord Cat Bot 2.0 - Main
# Updated: January 11, 2025
# Developed by Kaitlyn Hornbuckle (https://www.linkedin.com/in/kaitlynhornbuckle/)
# Purpose: Runs all processes and features of Cat Bot 2.0

import subprocess

# Define paths to your Python scripts
script1_path = 'catbot2.py'
script2_path = 'catbot2-commands.py'

# Start script1.py in a separate process
process1 = subprocess.Popen(['python', script1_path])

# Start script2.py in a separate process
process2 = subprocess.Popen(['python', script2_path])

# Wait for processes to complete (optional)
process1.wait()
process2.wait()
