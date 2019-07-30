from django.shortcuts import render
from .models import Company
from .serializers import CompanySerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(company_id=company_id)
    except Company.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(CompanySerializer(company).data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        company.delete()
        return HttpResponse(status=204)