from django.test import TestCase
from companyapp.models import Company
from datetime import date
from decimal import Decimal
from django.urls import reverse


class CompanyListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 10 companies
        number_of_companies = 10
        for company_id in range(1, number_of_companies+1):
            Company.objects.create(company_id=company_id, name="Company A LLC", share_price_date=date(2019, 7, 24),
                                   share_price=Decimal(15.254), comments="Data Provided by John Doe")

    def test_list_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_list_view_by_name(self):
        response = self.client.get(reverse('companyapp:company-list'))
        self.assertEqual(response.status_code, 200)
