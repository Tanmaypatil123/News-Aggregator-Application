from django.shortcuts import render
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from rest_framework.response import Response
from main.serializers import NewsSerializer
from main.models import News_data


@api_view(["GET"])
def api_home(request,*args,**kwargs):
    instance = News_data.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = NewsSerializer(instance).data

    return Response(data)    
