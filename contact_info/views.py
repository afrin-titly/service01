from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from contact_info.models import CustomerContactInfo


class CustomerContactInfoView(APIView):

    def get(self, request):
        customer_infos = CustomerContactInfo.objects.all()
        response = []
        for customer_info in customer_infos:
            response += [customer_info.name,customer_info.phone_no,customer_info.operator]
        return Response(response)

    def post(self, request):
        name = request.data.get('name')
        phone = request.data.get('phone_no')
        operator = request.data.get('operator')
        if name:
            CustomerContactInfo(name=name,phone_no=phone,operator=operator).save()
            return Response({'result':'success'})
        else:
            return Response({'result': 'fail'})
