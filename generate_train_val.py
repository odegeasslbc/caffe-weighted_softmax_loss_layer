#import subprocess
import re
import sys
import os

def checkName(string):
    # make sure to get rid of all spaces and only store the string
    tmpName1 = re.search(r'\s\w+', string).group()
    tmpName = re.search(r'\w+', tmpName1).group()
    
    # make sure the name is only in lower case format
    if len(re.search(r'[a-z]+', tmpName).group()) == len(tmpName):
        return tmpName
    else:
        return 0

def write_train(root):

    # the file that going to be write in
    resFile = open("train.txt", "w")
    
    for foldername in os.listdir(root):
        tmpNbr = re.search(r'\d+_[a-z]', foldername)
        if tmpNbr:
            print foldername, " done" 
            
            folderNbr = re.search(r'\d+', tmpNbr.group()).group()
            flag = 0

            for filename in os.listdir(root+'/'+foldername):
                if filename.endswith(".jpg"):
                    if flag%8 != 0:
                        newline = foldername + "/" + filename + " " + folderNbr + "\n"
                        resFile.write(newline)
                    flag += 1
		    

def write_val(root):

    # the file that going to be write in
    resFile = open("val.txt", "w")
    
    for foldername in os.listdir(root):
        tmpNbr = re.search(r'\d+_[a-z]', foldername)
        if tmpNbr:
            
            print foldername, " done" 
            
            folderNbr = re.search(r'\d+', tmpNbr.group()).group()
            flag = 0

            for filename in os.listdir(root+'/'+foldername):
                if filename.endswith(".jpg"):
                    if flag%8 == 0:
                        newline = foldername + "/" + filename + " " + folderNbr + "\n"
                        resFile.write(newline)
                    flag += 1
            

if __name__ == '__main__':
    root = sys.argv[1]
    write_train(root) 
    write_val(root)
