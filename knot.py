import os
import winreg as reg
import subprocess
def find_system_python():
    try:

        output = subprocess.check_output(['where', 'python'], text=True)
        
     
        return output
    except Exception as e:
        # Handle exceptions (e.g., FileNotFoundError) if the command fails
        print("Error:",str(e))
        return None

# Call the function to find the system Python binary
system_python_path = find_system_python()

try:



    python_exe = system_python_path[:-1]
    # python_exe = sys.executable
    print(python_exe)
    # print(python_exe)
    #I don't want to add a for loop but I might soon
    key_path = r"SystemFileAssociations\.png\shell\Blindfold"

    # Create the registry entry for the context menu
    key = reg.CreateKeyEx(reg.HKEY_CLASSES_ROOT, key_path)
    reg.SetValue(key, '', reg.REG_SZ, '&Blindfold')

    # Create the command registry entry
    key_command = reg.CreateKeyEx(key, r"command")
    reg.SetValue(key_command, '', reg.REG_SZ, f'"{python_exe}" "{os.path.abspath("blindfold.py")}" "%1"')
    
    print("Context menu added successfully.")
except Exception as e:
    print("Error:", str(e))

