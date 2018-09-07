from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from read_files import read_files
from make_prediction import make_prediction
from rec.models import MovieRec

import json
import numpy as np

# Create your views here.

def index(request):
    # load the template
    template = loader.get_template('tag/index.html')

    # load tree variables
    [children_left,children_right,feature] = read_files()
    n_nodes = children_left.size
    # convert to JASON format
    json_children_left = json.dumps(children_left.tolist())
    json_children_right = json.dumps(children_right.tolist())
    json_feature = json.dumps(feature.tolist())

    # reading the user inputs
    if (request.POST.get('ans')):
        leaf_node = request.POST.get('ans')
        leaf_node = int(leaf_node)
        # make a prediction
        predicted_movie = make_prediction(leaf_node) #returns an ndarray
        # randomly choose a movie if more than one returned
        if predicted_movie.size > 1:
            movie_list =[np.choice(predicted_movie)]
        else:
            movie_list = predicted_movie.tolist()

        movie_id = str(MovieRec.objects.get(name=movie_list[0]).movie_id)
        json_predicted_movie = json.dumps(movie_list)

    else:
        predicted_movie = ["none"]
        movie_id = None
        json_predicted_movie = json.dumps(predicted_movie)
    

    # create context to pass to the template
    context = {
        'json_children_left':json_children_left,
        'json_children_right':json_children_right,
        'json_feature':json_feature,
        'json_predicted_movie':json_predicted_movie,
        'predicted_movie_py':predicted_movie,
        'movie_id_py':movie_id,
        'n_nodes':n_nodes,
    }
    return HttpResponse(template.render(context, request))

def about(request):
    # load the template
    template = loader.get_template('tag/about.html')

    # create context to pass to the template
    context = {
    }

    return HttpResponse(template.render(context, request))
