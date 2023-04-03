import os

from django.shortcuts import render
from django.core.cache import cache
import re


def index(request):
    return render(request, 'index.html')
