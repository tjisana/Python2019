from django.urls import path
from .views import company_list, company_detail

app_name = 'companyapp'

urlpatterns = [
    path('', company_list, name='company-list'),
    path('<int:company_id>/', company_detail, name='company-detail'),
]
