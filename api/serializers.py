from rest_framework import serializers
from .models import BlogPost

# serializers convert data from ORM into a format suitable for data transfer such as JSON

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "title", "content", "published_date"] # columns from orm (object relational model) present in the model
