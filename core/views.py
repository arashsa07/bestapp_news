from models import Category, News
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

import json


def get_child_categories(category):
    result = []
    for item in category.category_childs.all():
        result.append(item)
        result + get_child_categories(item)
    return result


def news_post(request, post_id, slug):
    try:
        n = News.objects.select_related().get(id=post_id)
        p = n.writer
        category = n.category
        result = model_to_dict(n)
        result['photo'] = result['photo'].url if result['photo'] else ''
        result['category_name'] = category.title
        result['writer'] = model_to_dict(p)
        result['writer']['photo'] = result['writer']['photo'].url if result['writer']['photo'] else ''
        return JsonResponse(result)
    except News.DoesNotExist:
        return HttpResponseNotFound()


def get_categories(request, agency_id):
    result = []
    categories = Category.objects.filter(agency_id=agency_id)
    for item in categories:
        result.append(model_to_dict(item))

    return JsonResponse(result, safe=False)


@csrf_exempt
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
        queryset = query.filter(Q(category=category) | Q(category__in=get_child_categories(category)))

    result = [{'id': item.id, 'url': item.url, 'category': item.category.title, 'category_id': item.category.id}
              for item in queryset[offset: limit+offset]]

    return JsonResponse(result, safe=False)


