from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views import View
from .models import Tag
import json


class TagApiDetail(View):
    def get(self, request, pk):
        tag = get_object_or_404(Tag,pk=pk)
        # try:
        #     tag = Tag.objects.get(pk=pk)
        # except Tag.DoesNotExist:
        #     raise Http404()
        tag_json = json.dumps(dict(id=tag.pk, name=tag.name, slug=tag.slug))
        return HttpResponse(tag_json, content_type='application/json')


class TagApiList(View):
    def get(self, request):
        tag_list = get_list_or_404(Tag)
        # tag_list = Tag.objects.all()
        tag_json = json.dumps([dict(id=tag.pk, name=tag.name, slug=tag.slug) for tag in tag_list])
        return HttpResponse(tag_json, content_type='application/json')
