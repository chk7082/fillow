from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response




from rest_framework import status


# Create your views here.

@api_view(['GET', 'POST'])
def movie_list(request):
    # get method는 모든 목록을 달라고 할때
    if request.method == "GET":
        pass
    
    # post method는 영화 데이터를 넣을때
    if request.method == "POST":
        pass
    
    
