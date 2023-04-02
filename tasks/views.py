from django.shortcuts import render

# Create your views here.

def get_img_path():

    return
def task_1(request):
    imgs = get_img_path()
    test = {
        "imgs":"",
    }
    return render(request, 'task_1.html', test)
def task_2(request):
    return render(request, 'task_2.html')