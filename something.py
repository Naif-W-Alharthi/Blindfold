import sys
import subprocess
import time
def find_system_python():
    try:
        # Get the output of the command "which python" in Unix-like systems
        # or "where python" in Windows.
        if sys.platform.startswith('win'):
            # Windows platform
            output = subprocess.check_output(['where', 'python'], text=True)
        else:
            # Unix-like platforms (Linux, macOS)
            output = subprocess.check_output(['which', 'python'], text=True)

        # Return the path to the system Python binary
        return output.strip()
    except Exception as e:
        # Handle exceptions (e.g., FileNotFoundError) if the command fails
        print(f"Error: {e}")
        return None

# Call the function to find the system Python binary
system_python_path = find_system_python()

if system_python_path:
    print(f"System Python binary is located at: {system_python_path}")
else:
    print("System Python binary not found.")

time.sleep(20)