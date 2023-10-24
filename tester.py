import os 
import sys
import winreg as reg

try:
    cwd= os.getcwd()

    
    python_exe=sys.executable

    
    
    key_path = r"Software\Classes\*\shell\Blindfold"
    
    # "D:\dev\python\script.py %1"
    
    key = reg.CreateKeyEx(reg.HKEY_CLASSES_ROOT,key_path)
    reg.SetValue(key,'',reg.REG_SZ,'&Blindfold')
    
    key1=reg.CreateKeyEx(key,r"command")
    # reg.SetValue(key1,reg.REG_SZ,python_exe+f'"{cwd}\\blindfold.py"')
    reg.SetValue(key1, '', reg.REG_SZ, python_exe + f' "{cwd}\\blindfold.py" "%1"')
except Exception as e:
    print("error is ",str(e))
