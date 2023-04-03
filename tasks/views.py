import json

from django.shortcuts import render, HttpResponse


# Create your views here.

def get_img_path():
    return


def task_1(request):
    imgs = get_img_path()
    test = {
        "imgs": "",
        "test": [1, 2, 3, 4, 5, 6, 7, 8, 9]
    }
    return render(request, 'task_1.html', test)


def task_2(request):
    return render(request, 'task_2.html')


def process_true(request):
    print(1)
    return HttpResponse(json.dumps({'ret': 0}))


def process_false(request):
    return HttpResponse(json.dumps({'ret': 0}))
