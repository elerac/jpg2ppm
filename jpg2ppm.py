import cv2
import os
import glob as glob
from tkinter import filedialog

def main():
    print("Select input directory")
    f_in = filedialog.askdirectory(initialdir=".")
    
    print("Select output directory")
    f_out = filedialog.askdirectory(initialdir=".")
    f_out = f_out.split("/")[-1]
    
    dirs = list(dict.fromkeys([os.path.dirname(filedir) for filedir in glob.glob(f_in+"/**/*.*", recursive=True)]))
    
    for Dir in dirs:
        names = glob.glob(Dir+"/*.jpg")
        imgs_jpg = [cv2.imread(name, 1) for name in names]
        for name,img in zip(names, imgs_jpg):
            name_split = name.split("/")
            img_name = (name_split[-1]).split(".")[0]
            dir_name = name_split[-2]

            out_dir = "./"+f_out+"/"+dir_name
            if os.path.isdir(out_dir)  == False:
                os.makedirs(out_dir)

            cv2.imwrite(out_dir+"/"+img_name+".ppm", img) 

if __name__=="__main__":
    main()
