from venv import create
from django.shortcuts import render
from rest_framework import generics,authentication,permissions

from .permissions import IsStaffEditorPermission
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import News_data
from .serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework import mixins


@api_view(["GET"])
def news_all_list(request,pk = None,*args,**kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(News_data,pk=pk)
            data = NewsSerializer(obj,many=False)
            return Response(data)
        queryset = News_data.objects.all()
        data = NewsSerializer(queryset,many=True).data
        return Response(data)   

