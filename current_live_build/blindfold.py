import cv2
import numpy as np
import os
import sys
import winreg
import ctypes
import subprocess
import time
import random
# import numpy as np
# img = np.zeros([100,100,3],dtype=np.uint8)
# now add right click context menu

input = sys.argv[1] 


def image_eater(image_path):
    ### image_path here is the string path 
    vakes=[]
    try:
        image_file = cv2.imread(image_path)
        # cv2.imshow("1h",image_file)
        # cv2.waitKey(0)
        x,y,z = image_file.shape
        # time.sleep(20)
        """check what Z does"""
        # print(x,y,z)
        temp_= np.zeros([x,y,z])
        for rows in range(0,x):
            for cols in range(0,y):
                for dim in range(0,z):
                    strength = random.randint(-2,2)
                    
                    if image_file[rows,cols,dim] +strength > 255:
                        image_file[rows,cols,dim] = 254
                    elif image_file[rows,cols,dim] + strength < 0:
                        image_file[rows,cols,dim] = 1

                    else:
                        image_file[rows,cols,dim] = image_file[rows,cols,dim]+strength
                        temp_[rows,cols,dim] = temp_[rows,cols,dim]+strength*20
                    vakes.append(image_file[rows,cols,0])
                # print(image_path)
        # cv2.imshow("h",image_file)
        # cv2.waitKey(0)
        Path_todirect= image_path
        Path_todirect= Path_todirect.split("\\")
        name=  Path_todirect[-1]
        Path_todirect=Path_todirect[:-1]
        Path_todirect= "\\\\".join(Path_todirect)
        final_name=(Path_todirect+"\\\\"+name[:-4]+"_blindfold.png")
        final_name_code=(Path_todirect+"\\\\"+name[:-4]+"_blindfold_code.png")
        print(max(vakes),min(vakes))
        time.sleep(20)
        cv2.imwrite(final_name, image_file) 
        cv2.imwrite(final_name_code, temp_) 
    except Exception as e:
        print(e)
        

#removed check due to the registry just being on pngs
image_eater(input)
# C:\Users\pokem\OneDrive\Pictures\goals.png

