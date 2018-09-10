import csv, codecs, cStringIO
import os
import numpy as np

class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")


class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self

def make_prediction(leaf_node):
    module_dir = os.path.dirname(__file__)
    fp_movie_name = os.path.join(module_dir, 'movie_name.csv')
    fp_prediction = os.path.join(module_dir, 'prediction_dict.npy')
     
    #read movie name
    with open(fp_movie_name,'r') as myFile:
        data_iter = UnicodeReader(myFile)
        data = [data for data in data_iter]
    movie_name = np.asarray(data[0], dtype = unicode)

    #read the prediction array
    prediction = np.load(fp_prediction).item()

    #get the prediction of the leaf node
    y = prediction[leaf_node][0]
    y_ind = y==1

    #get the name of the movie for the prediction
    predicted_movie = movie_name[y_ind]  # a list
    
    return predicted_movie
 
