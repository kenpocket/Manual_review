import base64
import json
import os
import time

from django.shortcuts import render, HttpResponse
from .models import SketchfabInfo
from django.core.cache import cache


# Create your views here.


def task_1(request):
    print(request.META['REMOTE_ADDR'])
    s = SketchfabInfo.objects.filter(is_check__range=[1, 2]).first()
    if not s:
        return HttpResponse('no data')
    print(s)

    uid = s.uid
    a = cache.get(uid)
    a = r'F:\toolkit\workspace\glb' + '\\' + a
    print(a)
    test = [base64.b64encode(open(a + '\\' + i, 'rb').read()).decode() for i in os.listdir(a)]
    # print(test)
    test = {
        "file": a,
        "test": test
    }
    request.session['uid'] = uid
    return render(request, 'task_1.html', test)


def task_2(request):
    s = SketchfabInfo.objects.filter(is_check=-1).first()
    if not s:
        return HttpResponse('暂无')
    # print(s)
    uid = s.uid
    print(uid)
    a = cache.get(uid)
    a = r'F:\toolkit\workspace\glb' + '\\' + a
    print(a)
    test = [base64.b64encode(open(a + '\\' + i, 'rb').read()).decode() for i in os.listdir(a)]
    # print(test)
    test = {
        "file": a,
        "test": test
    }
    request.session['uid'] = uid
    return render(request, 'task_2.html', test)


def process_true(request):
    uid = request.session['uid']
    t1 = SketchfabInfo.objects.filter(uid=uid)
    t1.update(is_check=1)
    cache.set(request.META['REMOTE_ADDR'], uid, timeout=180)
    print(cache)
    return HttpResponse(json.dumps({'ret': 0, "message": "is_check=1"}))


def process_false(request):
    print(request.POST['reason'])
    uid = request.session['uid']
    t1 = SketchfabInfo.objects.filter(uid=uid)
    t1.update(is_check=2)
    return HttpResponse(json.dumps({'ret': 0, "message": "is_check=2"}))


def next_page(request):
    num = request.session.get('num', None)
    if num is None:
        num = 1
        request.session['num'] = 1
    else:
        num += 1
        request.session['num'] = num
    print(request.session.values())
    try:
        s = SketchfabInfo.objects.filter(is_check__range=[1, 2])[num]
        fp = cache.get(s.uid, None)
        a = r'F:\toolkit\workspace\glb' + '\\' + fp
        request.session['uid'] = s.uid
        test = [base64.b64encode(open(a + '\\' + i, 'rb').read()).decode() for i in os.listdir(a)]
        data = {"ret": 0,
                'value': test,
                "file": a
                }
        return HttpResponse(json.dumps(data))
    except IndexError:
        request.session['num'] = 0
        return HttpResponse(json.dumps({'ret': -1, 'value': []}))
