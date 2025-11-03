from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def studentsViews(request):
    students={
        'id':1,
        'name':'Alice',
        'class':'Biology'
    }
    return JsonResponse(students)