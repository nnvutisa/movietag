import numpy as np
import csv
import os

def read_files():
    module_dir = os.path.dirname(__file__)
    fp_children_left = os.path.join(module_dir, 'children_left.csv')
    fp_children_right = os.path.join(module_dir, 'children_right.csv')
    fp_feature = os.path.join(module_dir, 'feature.csv')
    fp_movie_name = os.path.join(module_dir, 'movie_name.csv')
    fp_prediction = os.path.join(module_dir, 'prediction.npy')
    
    #read children arrays
    children_left = np.genfromtxt(fp_children_left,delimiter=',')
    children_right = np.genfromtxt(fp_children_right,delimiter=',')

    #read feature array
    with open(fp_feature,'r') as myFile:
        data_iter = csv.reader(myFile, 
                               delimiter = ',', 
                               quotechar = '"')
        data = [data for data in data_iter]
    feature = np.asarray(data[0], dtype = unicode)

    return [children_left,children_right,feature]
