from rest_framework import serializers
from django.utils.timezone import now
from .models import Company
from django.core.validators import MaxLengthValidator


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_id', 'name', 'share_price_date', 'share_price', 'comments']

# class CompanySerializer(serializers.Serializer):
#     company_id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=80)
#     share_price_date = serializers.DateField(default=now)
#     share_price = serializers.DecimalField(max_digits=8, decimal_places=3)
#     comments = serializers.CharField(max_length=256)
#
#     def create(self, validated_data):
#         print("In create function")
#         return Company.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         print("In update function")
#         instance.company_id = validated_data.get('company_id', instance.company_id)
#         instance.name = validated_data.get('company_id', instance.name)
#         instance.share_price_date = validated_data.get('company_id', instance.share_price_date)
#         instance.share_price = validated_data.get('company_id', instance.share_price)
#         instance.comments = validated_data.get('company_id', instance.comments)
