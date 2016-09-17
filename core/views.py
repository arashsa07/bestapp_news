from models import Category, News
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

from serializer import NewsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

import json


def get_child_categories(category):
    result = []
    for item in category.category_childs.all():
        result.append(item)
        result + get_child_categories(item)
    return result


@api_view(['GET'])
def news_post(request, post_id, slug):
    try:
        n = News.objects.select_related().get(id=post_id)
        result = NewsSerializer(n, many=False)
        return Response(result.data)

    except News.DoesNotExist:
        return HttpResponseNotFound()


def get_categories(request, agency_id):
    result = []
    categories = Category.objects.filter(agency_id=agency_id)
    for item in categories:
        result.append(model_to_dict(item))

    return JsonResponse(result, safe=False)


@csrf_exempt
@api_view(['POST'])
def search_news(request, category_id, regex):
    try:
        data = json.loads(request.body)
    except KeyError:
        return HttpResponseServerError("Malformed data!")

    limit = data.get('limit', 25)
    offset = data.get('offset', 0)

    try:
        limit = int(limit)
    except ValueError:
        limit = 25
    else:
        if limit > 25:
            limit = 25

    try:
        offset = int(offset)
    except ValueError:
        offset = 0

    query = News.objects.filter(title__contains=regex)

    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        queryset = query
    else:
        queryset = query.filter(Q(category=category) | Q(category__in=get_child_categories(category)))[offset: limit+offset]

    if queryset:
        result = NewsSerializer(queryset, many=True)
        return Response(result.data)
    else:
        return Response({})


@api_view(['GET'])
def get_news(request, agency_id):

    limit = request.data.get('limit', 25)
    offset = request.data.get('offset', 0)
    order_by = request.data.get('order_by', 'id')

    try:
        offset = int(offset)
        limit = int(limit)
    except ValueError:
        return Response({'error': 406, 'message': 'query values not acceptable'}, status=status.HTTP_406_NOT_ACCEPTABLE)

    category = Category.objects.filter(agency_id=agency_id)
    news = News.objects.filter(category__in=category).order_by(order_by)[offset: limit+offset]

    if news:
        result = NewsSerializer(news, many=True)
        return Response(result.data)
    else:
        return Response([])
