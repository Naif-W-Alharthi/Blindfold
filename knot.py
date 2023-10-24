import os
import sys
import winreg as reg

try:
    python_exe = sys.executable
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
