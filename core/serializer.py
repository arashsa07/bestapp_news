from rest_framework import serializers
from .models import News, Person, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person


class NewsSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField('category_name_field')
    writer = PersonSerializer(many=False, read_only=True)

    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        super(NewsSerializer, self).__init__(*args, **kwargs)

        if remove_fields:
            for field_name in remove_fields:
                self.fields.pop(field_name)

    def category_name_field(self, news):
        return news.category.title

    class Meta:
        model = News
        fields = ('id', 'category', 'category_name', 'title', 'sub_title', 'slug', 'photo', 'body', 'source', 'writer',
                  'date_added', 'date_modify')




