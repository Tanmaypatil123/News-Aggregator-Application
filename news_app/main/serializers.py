from rest_framework import serializers

from .models import News_data

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News_data
        fields = [
            "id",
            "category",
            "heading",
            "img",
            "url",
            "content",
            "date"
        ]