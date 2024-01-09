import os 
from utils.utils import merger

path = '/Users/chinmaychoudhary/Downloads/ST'
filelist = os.listdir(path)

merger(filelist,path,'gate_statistics_pyp.pdf')