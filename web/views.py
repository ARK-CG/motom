from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
# from .models import Card, Request, ProgrammingLanguage, Tag, Category
# from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required
def index(request):
    return render(request,'motom/index.html')