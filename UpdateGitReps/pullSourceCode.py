#!/bin/env python

import sys
import os

def isFileExist(fileName):
    return os.path.exists(fileName)

def isIgnoredReps(rep):
    ignoreList = ['scm_il', '.ilgit']
    return rep in ignoreList

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print 'Usage: %s <source code path>' %sys.argv[0]
        exit(2)

    sourcePath = sys.argv[1]

    if not isFileExist(sourcePath):
        print 'No such file or directory: %s' %sourcePath
        exit(2)

    dirs = os.listdir(sourcePath)
    #print dirs
    for dir in dirs:
        #print dir
        print '\n\nProcessing %d/%d: %s' %(dirs.index(dir), len(dirs), dir)
        if isIgnoredReps(dir):
            continue

        currDir = os.path.join(sourcePath, dir)
        #print currDir
        os.chdir(currDir)
        #print os.getcwd()
        os.system("git checkout -f; git pull ")

