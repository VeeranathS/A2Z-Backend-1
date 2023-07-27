from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.http import JsonResponse
from .models import *
from rest_framework import status
from .serializers import *
import googlemaps
from django.conf import settings
from math import radians, sin, cos, sqrt, atan2
from .models import DispatchEntry, Cases, Accounts, ServiceTypes, Reasons, Customers, DispatchEntryAssets, DispatchStatus, SystemUser, Company,Vehicles
from .serializers import DispatchEntrySerializer


# @api_view(['POST'])
# def create_dispatch_entry(request):
#     service_id = request.data.get('service', {}).get('serviceId')
#     customer_partner_id = request.data.get('Customer Partner', {}).get('id')
#     customer_name = request.data.get('CustomerInfo', {}).get('name')
#     customer_phone = request.data.get('CustomerInfo', {}).get('phone')
#     customer_email = request.data.get('CustomerInfo', {}).get('email')
#     make = request.data.get('assets', {}).get('make')
#     model = request.data.get('assets', {}).get('model')
#     color = request.data.get('assets', {}).get('color')
#     year = request.data.get('assets', {}).get('year')
#     street = request.data.get('location', {}).get('street')
#     city = request.data.get('location', {}).get('city')
#     state = request.data.get('location', {}).get('state')
#     zip_code = request.data.get('location', {}).get('zip')
#     longitude = request.data.get('location', {}).get('longitude')
#     latitude = request.data.get('location', {}).get('latitude')
#     address = request.data.get('location', {}).get('address')
#     job_price = request.data.get('jobInfo', {}).get('price')

#     dispatch_entry = DispatchEntry.objects.create(
#         service_type_id=ServiceTypes.objects.get(service_type_id=service_id),
#         customer_id=Customers.objects.create(name=customer_name, phone=customer_phone, email=customer_email),
#         asset_id=DispatchEntryAssets.objects.create(make=make, model=model, colorid=color, model_year=year),
#     )

#     response_data = {
#         "service": {"serviceId": service_id},
#         "Customer Partner": {"id": customer_partner_id},
#         "CustomerInfo": {"name": customer_name, "phone": customer_phone, "email": customer_email},
#         "location": {"street": street, "city": city, "state": state, "zip": zip_code, "longitude": longitude, "latitude": latitude, "address": address},
#         "assets": {"make": make, "model": model, "color": color, "year": year},
#         "jobInfo": {"price": job_price}
#     }
#     return Response(response_data)

## Accounts API
@api_view(['GET', 'POST'])
def accounts_list(request):
    if request.method == 'GET':
        accounts = Accounts.objects.all()
        serializer = AccountsSerializer(accounts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AccountsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def accounts_detail(request, account_id):
    try:
        account = Accounts.objects.get(account_id=account_id)
    except Accounts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AccountsSerializer(account)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AccountsSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
## AccountTypes API
@api_view(['GET', 'POST'])
def account_types_list(request):
    if request.method == 'GET':
        account_types = AccountTypes.objects.all()
        serializer = AccountTypesSerializer(account_types, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AccountTypesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def account_types_detail(request, account_type_id):
    try:
        account_type = AccountTypes.objects.get(account_type_id=account_type_id)
    except AccountTypes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AccountTypesSerializer(account_type)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AccountTypesSerializer(account_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        account_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
## Cases API
@api_view(['GET', 'POST'])
def cases_list(request):
    if request.method == 'GET':
        cases = Cases.objects.all()
        serializer = CasesSerializer(cases, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CasesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cases_detail(request, case_id):
    try:
        cases = Cases.objects.get(case_id=case_id)
    except Cases.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CasesSerializer(cases)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CasesSerializer(cases, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        cases.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
## Company API
@api_view(['GET', 'POST'])
def companies_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def companies_detail(request, company_id):
    try:
        company = Company.objects.get(company_id=company_id)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
## CompanyFeatures API
@api_view(['GET', 'POST'])
def company_features_list(request):
    if request.method == 'GET':
        company_features = CompanyFeatures.objects.all()
        serializer = CompanyFeaturesSerializer(company_features, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CompanyFeaturesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def company_features_detail(request, feature_id):
    try:
        company_feature = CompanyFeatures.objects.get(feature_id=feature_id)
    except CompanyFeatures.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CompanyFeaturesSerializer(company_feature)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CompanyFeaturesSerializer(company_feature, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        company_feature.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
## CompanyPricing API
@api_view(['GET', 'POST'])
def company_pricing_list(request):
    if request.method == 'GET':
        company_pricing = CompanyPricing.objects.all()
        serializer = CompanyPricingSerializer(company_pricing, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CompanyPricingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def company_pricing_detail(request, pricing_id):
    try:
        company_pricing = CompanyPricing.objects.get(id=pricing_id)
    except CompanyPricing.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CompanyPricingSerializer(company_pricing)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CompanyPricingSerializer(company_pricing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        company_pricing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
## Customers API
@api_view(['GET', 'POST'])
def customers_list(request):
    if request.method == 'GET':
        customers = Customers.objects.all()
        serializer = CustomersSerializer(customers, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CustomersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def customers_detail(request, customer_id):
    try:
        customer = Customers.objects.get(customer_id=customer_id)
    except Customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CustomersSerializer(customer)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CustomersSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
## CustomerFeedback API
@api_view(['GET', 'POST'])
def customer_feedback_list(request):
    if request.method == 'GET':
        feedbacks = CustomerFeedback.objects.all()
        serializer = CustomerFeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CustomerFeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def customer_feedback_detail(request, feedback_id):
    try:
        feedback = CustomerFeedback.objects.get(id=feedback_id)
    except CustomerFeedback.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CustomerFeedbackSerializer(feedback)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CustomerFeedbackSerializer(feedback, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

## DispatchEntryAssets API
@api_view(['GET', 'POST'])
def dispatch_entry_assets_list(request):
    if request.method == 'GET':
        assets = DispatchEntryAssets.objects.all()
        serializer = DispatchEntryAssetsSerializer(assets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DispatchEntryAssetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def dispatch_entry_assets_detail(request, asset_id):
    try:
        asset = DispatchEntryAssets.objects.get(asset_id=asset_id)
    except DispatchEntryAssets.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DispatchEntryAssetsSerializer(asset)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DispatchEntryAssetsSerializer(asset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        asset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
## DispatchStatus API
@api_view(['GET', 'POST'])
def dispatch_status_list(request):
    if request.method == 'GET':
        statuses = DispatchStatus.objects.all()
        serializer = DispatchStatusSerializer(statuses, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DispatchStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def dispatch_status_detail(request, dispatch_status_id):
    try:
        status = DispatchStatus.objects.get(dispatch_status_id=dispatch_status_id)
    except DispatchStatus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DispatchStatusSerializer(status)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DispatchStatusSerializer(status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
## DispatchStatusRecords API
@api_view(['GET', 'POST'])
def dispatch_entry_status_records_list(request):
    if request.method == 'GET':
        records = DispatchEntryStatusRecords.objects.all()
        serializer = DispatchEntryStatusRecordsSerializer(records, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DispatchEntryStatusRecordsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def dispatch_entry_status_records_detail(request, record_id):
    try:
        record = DispatchEntryStatusRecords.objects.get(id=record_id)
    except DispatchEntryStatusRecords.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DispatchEntryStatusRecordsSerializer(record)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DispatchEntryStatusRecordsSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

## Dispatch Entry API
@api_view(['GET', 'POST'])
def dispatch_entry_list(request):
    if request.method == 'GET':
        dispatch_entries = DispatchEntry.objects.all()
        serializer = DispatchEntrySerializer(dispatch_entries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DispatchEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def dispatch_entry_detail(request, entry_id):
    try:
        dispatch_entry = DispatchEntry.objects.get(dispatch_entry_id=entry_id)
    except DispatchEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DispatchEntrySerializer(dispatch_entry)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DispatchEntrySerializer(dispatch_entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        dispatch_entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
## DriverLocation API
@api_view(['GET', 'POST'])
def driver_location_list(request):
    if request.method == 'GET':
        locations = DriverLocation.objects.all()
        serializer = DriverLocationSerializer(locations, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DriverLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def driver_location_detail(request, location_id):
    try:
        location = DriverLocation.objects.get(driverLocation_id=location_id)
    except DriverLocation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DriverLocationSerializer(location)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DriverLocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
## Features API
@api_view(['GET', 'POST'])
def features_list(request):
    if request.method == 'GET':
        features = Features.objects.all()
        serializer = FeaturesSerializer(features, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FeaturesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def features_detail(request, feature_id):
    try:
        feature = Features.objects.get(feature_id=feature_id)
    except Features.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FeaturesSerializer(feature)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = FeaturesSerializer(feature, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        feature.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
## Invoice API
@api_view(['GET', 'POST'])
def invoices_list(request):
    if request.method == 'GET':
        invoices = Invoices.objects.all()
        serializer = InvoicesSerializer(invoices, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InvoicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def invoices_detail(request, invoice_id):
    try:
        invoice = Invoices.objects.get(invoice_id=invoice_id)
    except Invoices.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InvoicesSerializer(invoice)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InvoicesSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
## Payments API
@api_view(['GET', 'POST'])
def payments_list(request):
    if request.method == 'GET':
        payments = Payments.objects.all()
        serializer = PaymentsSerializer(payments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PaymentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def payments_detail(request, payment_id):
    try:
        payment = Payments.objects.get(payment_id=payment_id)
    except Payments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PaymentsSerializer(payment)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PaymentsSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
## RateItem API
@api_view(['GET', 'POST'])
def rate_items_list(request):
    if request.method == 'GET':
        rate_items = RateItem.objects.all()
        serializer = RateItemSerializer(rate_items, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = RateItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def rate_items_detail(request, rate_item_id):
    try:
        rate_item = RateItem.objects.get(rate_item_id=rate_item_id)
    except RateItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RateItemSerializer(rate_item)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = RateItemSerializer(rate_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        rate_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
## Reasons API
@api_view(['GET', 'POST'])
def reasons_list(request):
    if request.method == 'GET':
        reasons = Reasons.objects.all()
        serializer = ReasonsSerializer(reasons, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ReasonsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def reasons_detail(request, reason_id):
    try:
        reason = Reasons.objects.get(reason_id=reason_id)
    except Reasons.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ReasonsSerializer(reason)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReasonsSerializer(reason, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        reason.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
## ServiceProvider API
# @api_view(['GET', 'POST'])
# def service_providers_list(request):
#     if request.method == 'GET':
#         service_providers = ServiceProvider.objects.all()
#         serializer = ServiceProviderSerializer(service_providers, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ServiceProviderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def service_provider_detail(request, provider_id):
#     try:
#         service_provider = ServiceProvider.objects.get(service_provider_id=provider_id)
#     except ServiceProvider.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ServiceProviderSerializer(service_provider)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ServiceProviderSerializer(service_provider, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         service_provider.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
## ServiceTypes API
@api_view(['GET', 'POST'])
def service_types_list(request):
    if request.method == 'GET':
        service_types = ServiceTypes.objects.all()
        serializer = ServiceTypesSerializer(service_types, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ServiceTypesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def service_types_detail(request, type_id):
    try:
        service_type = ServiceTypes.objects.get(service_type_id=type_id)
    except ServiceTypes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ServiceTypesSerializer(service_type)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ServiceTypesSerializer(service_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        service_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
## SystemUser API
@api_view(['GET', 'POST'])
def system_users_list(request):
    if request.method == 'GET':
        system_users = SystemUser.objects.all()
        serializer = SystemUserSerializer(system_users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SystemUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def system_users_detail(request, csr_id):
    try:
        system_user = SystemUser.objects.get(csr_id=csr_id)
    except SystemUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SystemUserSerializer(system_user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SystemUserSerializer(system_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        system_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
## SystemUserStatusRecords API
@api_view(['GET', 'POST'])
def user_status_records_list(request):
    if request.method == 'GET':
        user_status_records = SystemUserStatusRecords.objects.all()
        serializer = SystemUserStatusRecordsSerializer(user_status_records, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SystemUserStatusRecordsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_status_records_detail(request, record_id):
    try:
        user_status_record = SystemUserStatusRecords.objects.get(id=record_id)
    except SystemUserStatusRecords.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SystemUserStatusRecordsSerializer(user_status_record)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SystemUserStatusRecordsSerializer(user_status_record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user_status_record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    



## Vehicles API
@api_view(['GET', 'POST'])
def vehicles_list(request):
    if request.method == 'GET':
        vehicles = Vehicles.objects.all()
        serializer = VehiclesSerializer(vehicles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = VehiclesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vehicles_detail(request, vehicle_id):
    try:
        vehicle = Vehicles.objects.get(vehicle_id=vehicle_id)
    except Vehicles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = VehiclesSerializer(vehicle)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = VehiclesSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    radius = 6371

    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = radius * c

    return distance

@api_view(['GET'])
def nearby_drivers(request):
    pickup_latitude = request.GET.get('pickup_latitude')
    pickup_longitude = request.GET.get('pickup_longitude')
    distance = 2

    if pickup_latitude and pickup_longitude and distance:
        gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

        nearby_drivers = []
        for driver in Company.objects.all():
            driver_latitude = driver.latitude
            driver_longitude = driver.longitude

            dist = haversine(float(pickup_latitude), float(pickup_longitude), driver_latitude, driver_longitude)

            if dist <= float(distance):
                nearby_drivers.append(driver)

        serializer = CompanySerializer(nearby_drivers, many=True)
        return Response(serializer.data)

    return Response([])

# @api_view(['GET', 'POST'])
# def create_dispatch_entry(request):
#     if request.method == 'GET':
#         dispatch_entries = DispatchEntry.objects.all()
#         serializer = DispatchEntrySerializer(dispatch_entries, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         case_data = {
#         }
#         case = Cases.objects.create(**case_data)

#         account_data = {
#         }
#         account = Accounts.objects.create(**account_data)

#         service_type_data = {
#         }
#         service_type = ServiceTypes.objects.create(**service_type_data)

#         reason_data = {
#         }
#         reason = Reasons.objects.create(**reason_data)

#         customer_data = {
#         }
#         customer = Customers.objects.create(**customer_data)

#         asset_data = {
#         }
#         asset = DispatchEntryAssets.objects.create(**asset_data)

#         dispatch_status_data = {
#         }
#         dispatch_status = DispatchStatus.objects.create(**dispatch_status_data)

#         csr_data = {
#         }
#         csr = SystemUser.objects.create(**csr_data)

#         company_data = {
#         }
#         company = Company.objects.create(**company_data)

#         dispatch_entry_data = {
#             'case_id': case,
#             'partner_service_id': 12345,
#             'account_id': account,
#             'service_type_id': service_type,
#             'reason_id': reason,
#             'customer_id': customer,
#             'asset_id': asset,
#             'dispatch_status_id': dispatch_status,
#             'csr_id': csr,
#             'company_id': company,
#             'pickup_location': 'Some pickup location',
#             'dropoff_location': 'Some dropoff location',
#         }

#         dispatch_entry = DispatchEntry.objects.create(**dispatch_entry_data)

#         serializer = DispatchEntrySerializer(dispatch_entry)
#         return Response(serializer.data)


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DispatchEntry, Customers, DispatchEntryAssets, Vehicles

@csrf_exempt
def WebPortalView(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        whatsapp_number = data.get('whatsapp_number')
        license_plate = data.get('license_plate')
        make = data.get('make')
        # vehicle_class = data.get('vehicle_class')
        # vehicle_type = data.get('vehicle_type')
        pickup_location = data.get('pickup_location')
        breakdown_issue = data.get('breakdown_issue')

        customer = Customers.objects.create(
            name=name,
            email=email,
            phone=phone,
            whatsapp_number=whatsapp_number
        )

        customer_id = customer.customer_id

        try:
            vehicle = Vehicles.objects.get(make=make)
        except Vehicles.DoesNotExist:
            return JsonResponse({'error': 'Vehicle not found in the database.'}, status=404)

        asset = DispatchEntryAssets.objects.create(
            customer_id=customer,
            license_plate=license_plate,
            vehicle_id=vehicle
        )

        asset_id = asset.asset_id
        try:
            csr = SystemUser.objects.get(name='Rohan')
        except SystemUser.DoesNotExist:
            return JsonResponse({'error': 'CSR not found in the database.'}, status=404)
        try:
            reason = Reasons.objects.get(name=breakdown_issue, service_type='ROS')
        except Reasons.DoesNotExist:
            return JsonResponse({'error': 'Reason not found in the database.'}, status=404)
        try:
            service_type = ServiceTypes.objects.get(service='AIR FILL', service_type='ROS')
        except ServiceTypes.DoesNotExist:
            return JsonResponse({'error': 'ServiceType not found in the database.'}, status=404)
        try:
            dispatch_status = DispatchStatus.objects.get(name='Waiting')
        except DispatchStatus.DoesNotExist:
            return JsonResponse({'error': 'DispatchStatus not found in the database.'}, status=404)
        try:
            company = Company.objects.get(name="A2Z ASSIST")
        except Company.DoesNotExist:
            return JsonResponse({'error': 'Company not found in the database.'}, status=404)
        try:
            account = Accounts.objects.get(name="ALLIANZ")
        except Accounts.DoesNotExist:
            return JsonResponse({'error':"Account not found in the database."},status=404)


        case = Cases.objects.create(
            dispatch_entry_id=None,  
            csr_id=csr,  
        )

        dispatch_entry = DispatchEntry.objects.create(
            customer_id=customer,
            asset_id=asset,
            account_id=account,
            case_id=case,  
            partner_service_id=0, 
            service_type_id=service_type,  
            reason_id=reason,  
            dispatch_status_id=dispatch_status, 
            csr_id=csr,  
            company_id=company,  
            pickup_location=pickup_location,  
            dropoff_location="None"  
        )

        return JsonResponse({'message': 'Data successfully stored in DispatchEntry model.', 'customer_id': customer_id, 'asset_id': asset_id}, status=201)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)






# @api_view(['GET', 'POST'])
# def create_dispatch_entry(request):
#     if request.method == 'GET':
#         dispatch_entries = DispatchEntry.objects.all()
#         serializer = DispatchEntrySerializer(dispatch_entries, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         customer_data = {}
#         customer = Customers.objects.create(**customer_data)


#         dispatch_entry_data = {
#             'customer_id': customer,
#         }

#         dispatch_entry = DispatchEntry.objects.create(**dispatch_entry_data)
#         serializer = DispatchEntrySerializer(dispatch_entry)
#         return Response(serializer.data)


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RateItem, Vehicles

@csrf_exempt
def get_default_rate(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = data.get('breakdown_issue')
        account_id = data.get('account_id')
        account_name = data.get('account_name')
        account_company_id = data.get('account_company_id')
        make = data.get('make')

        try:
            vehicle = Vehicles.objects.get(
                make=make
            )
        except Vehicles.DoesNotExist:
            return JsonResponse({'error': 'Vehicle not found for the given criteria.'}, status=404)

        try:
            rate_item = RateItem.objects.get(
                name=name,
                account_id=account_id,
                account_name=account_name,
                account_company_id=account_company_id,
                vehicle_id=vehicle
            )
        except RateItem.DoesNotExist:
            return JsonResponse({'error': 'RateItem not found for the given criteria.'}, status=404)

        response_data = {
            'default_rate': rate_item.default_rate,
        }

        return JsonResponse(response_data, status=200)

    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)

@api_view(['GET'])
def get_dispatch_entry(request,dispatch_entry_id):
    try:
        account = DispatchEntry.objects.get(dispatch_entry_id=dispatch_entry_id)
    except DispatchEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DispatchEntrySerializer(account)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def create_dispatch_entry(request):
    if request.method == 'GET':
        dispatch_entries = DispatchEntry.objects.all()
        serializer = DispatchEntrySerializer(dispatch_entries, many=True)
        return Response(serializer.data)
    
    
@csrf_exempt
def newcases(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        whatsapp_number = data.get('whatsapp_number')
        license_plate = data.get('license_plate')
        make = data.get('make')
        partner_service_id=data.get('partner_service_id')
        # vehicle_class = data.get('vehicle_class')
        # vehicle_type = data.get('vehicle_type')
        pickup_location = data.get('pickup_location')
        breakdown_issue = data.get('breakdown_issue')

        customer = Customers.objects.create(
            name=name,
            email=email,
            phone=phone,
            whatsapp_number=whatsapp_number
        )

        customer_id = customer.customer_id

        try:
            vehicle = Vehicles.objects.get(make=make)
        except Vehicles.DoesNotExist:
            return JsonResponse({'error': 'Vehicle not found in the database.'}, status=404)

        asset = DispatchEntryAssets.objects.create(
            customer_id=customer,
            license_plate=license_plate,
            vehicle_id=vehicle
        )

        asset_id = asset.asset_id
        try:
            csr = SystemUser.objects.get(name='Rohan')
        except SystemUser.DoesNotExist:
            return JsonResponse({'error': 'CSR not found in the database.'}, status=404)
        try:
            reason = Reasons.objects.get(name=breakdown_issue, service_type='ROS')
        except Reasons.DoesNotExist:
            return JsonResponse({'error': 'Reason not found in the database.'}, status=404)
        try:
            service_type = ServiceTypes.objects.get(service='AIR FILL', service_type='ROS')
        except ServiceTypes.DoesNotExist:
            return JsonResponse({'error': 'ServiceType not found in the database.'}, status=404)
        try:
            dispatch_status = DispatchStatus.objects.get(name='Waiting')
        except DispatchStatus.DoesNotExist:
            return JsonResponse({'error': 'DispatchStatus not found in the database.'}, status=404)
        try:
            company = Company.objects.get(name="A2Z ASSIST")
        except Company.DoesNotExist:
            return JsonResponse({'error': 'Company not found in the database.'}, status=404)
        try:
            account = Accounts.objects.get(name="ALLIANZ")
        except Accounts.DoesNotExist:
            return JsonResponse({'error':"Account not found in the database."},status=404)


        case = Cases.objects.create(
            dispatch_entry_id=None,  
            csr_id=csr,  
        )

        dispatch_entry = DispatchEntry.objects.create(
            customer_id=customer,
            asset_id=asset,
            account_id=account,
            case_id=case,  
            partner_service_id=partner_service_id, 
            service_type_id=service_type,  
            reason_id=reason,  
            dispatch_status_id=dispatch_status, 
            csr_id=csr,  
            company_id=company,  
            pickup_location=pickup_location,  
            dropoff_location="None"  
        )

        return JsonResponse({'message': 'Data successfully stored in DispatchEntry model.', 'customer_id': customer_id, 'asset_id': asset_id}, status=201)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
#     elif request.method == 'POST':
#         customer_data = {}
#         customer = Customers.objects.create(**customer_data)


#         dispatch_entry_data = {
#             'customer_id': customer,
#         }

#         dispatch_entry = DispatchEntry.objects.create(**dispatch_entry_data)
#         serializer = DispatchEntrySerializer(dispatch_entry)
#         return Response(serializer.data)
    

# class WebPortalView(APIView):
#     def get(self, request):
#         # Render the web portal HTML form here
#         return render(request, 'web_portal.html')

#     def post(self, request):
#         # Process form data from the web portal
#         customer_name = request.POST.get('customer_name')
#         customer_email = request.POST.get('customer_email')
#         customer_phone = request.POST.get('customer_phone')
#         # Get other form fields as needed

#         # Create a new Customers entry
#         customer = Customers.objects.create(
#             name=customer_name,
#             email=customer_email,
#             phone=customer_phone
#             # Set other fields accordingly
#         )

#         # Process form data for DispatchEntryAssets
#         asset_license_plate = request.POST.get('license_plate')
#         # Get other form fields for DispatchEntryAssets as needed

#         # Create a new DispatchEntryAssets entry
#         dispatch_entry_asset = DispatchEntryAssets.objects.create(
#             customer_id=customer.id,
#             license_plate=asset_license_plate
#             # Set other fields accordingly
#         )

#         # Process form data for Vehicles
#         vehicle_make = request.POST.get('vehicle_make')
#         vehicle_class = request.POST.get('vehicle_class')
#         vehicle_type = request.POST.get('vehicle_type')
#         # Get other form fields for Vehicles as needed

#         # Create a new Vehicles entry
#         vehicle = Vehicles.objects.create(
#             make=vehicle_make,
#             vehicle_class=vehicle_class,
#             vehicle_type=vehicle_type
#             # Set other fields accordingly
#         )

#         # Once you have the data from all models, create a DispatchEntry
#         dispatch_entry = DispatchEntry.objects.create(
#             customer_id=customer.id,
#             asset_id=dispatch_entry_asset.id,
#             vehicle_id=vehicle.id
#             # Set other fields for DispatchEntry as needed
#         )

#         return Response({'message': 'Data saved successfully!'})


# views.py
# views.py
# views.py

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Customers, DispatchEntryAssets, DispatchEntry, Vehicles
# from .serializers import CustomersSerializer, DispatchEntryAssetsSerializer, DispatchEntrySerializer, VehiclesSerializer

# class WebPortalView(APIView):
#     def post(self, request):
#         # Deserialize the JSON data sent by ReactJS
#         data = request.data

#         # Create a new Customers entry
#         customer_serializer = CustomersSerializer(data=data)
#         if customer_serializer.is_valid():
#             customer = customer_serializer.save()
#         else:
#             return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         # Create a new DispatchEntryAssets entry
#         dispatch_entry_asset_serializer = DispatchEntryAssetsSerializer(data=data)
#         if dispatch_entry_asset_serializer.is_valid():
#             dispatch_entry_asset = dispatch_entry_asset_serializer.save()
#         else:
#             return Response(dispatch_entry_asset_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         # Create a new Vehicles entry
#         vehicle_serializer = VehiclesSerializer(data=data)
#         if vehicle_serializer.is_valid():
#             vehicle = vehicle_serializer.save()
#         else:
#             return Response(vehicle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         # Create a new DispatchEntry
#         dispatch_entry_data = {
#             "customer_id": customer.id,
#             "asset_id": dispatch_entry_asset.id,
#             "vehicle_id": vehicle.id,
#             "dispatch_status_id": 1,  # Example: Set the dispatch status ID here
#             "pickup_location": "Some location",  # Example: Set the pickup location here
#             # Add other fields for DispatchEntry as needed
#         }

#         dispatch_entry_serializer = DispatchEntrySerializer(data=dispatch_entry_data)
#         if dispatch_entry_serializer.is_valid():
#             dispatch_entry_serializer.save()
#         else:
#             return Response(dispatch_entry_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         return Response({'message': 'Data saved successfully!'})

# 










# serializer = VehiclesSerializer(vehicle, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['POST'])
# def create_customer(request):
#     name = request.data.get('name')
#     email = request.data.get('email')
#     phone_number = request.data.get('phone_number')
#     whatsapp_number = request.data.get('whatsapp_number')

#     if not all([name, email, phone_number, whatsapp_number]):
#         return Response({'error': 'Missing required fields'}, status=400)

#     customer = Customers(
#         name=name,
#         email=email,
#         phone_number=phone_number,
#         whatsapp_number=whatsapp_number
#     )
#     customer.save()

#     return Response({'message': 'Customer created successfully'}, status=201)

# @api_view(['POST'])
# def create_service(request):
#     service_type = request.data.get('service_type')
#     name = request.data.get('name')

#     if not all([service_type, name]):
#         return Response({'error': 'Missing required fields'}, status=400)

#     service = ServiceTypes(service_type=service_type, name=name)
#     service.save()

#     return Response({'message': 'Service created successfully'}, status=201)


# @csrf_exempt
# def create_dispatch_entry(request):
#     if request.method == 'POST':
#         data = request.POST

#         service_id = data.get('service.serviceId')
#         customer_id = data.get('Customer Partner.id')
#         customer_name = data.get('CustomerInfo.name')
#         phone = data.get('CustomerInfo.phone')
#         email = data.get('CustomerInfo.email')
#         device = data.get('CustomerInfo.device')
#         street = data.get('location.street')
#         city = data.get('location.city')
#         state = data.get('location.state')
#         zip_code = data.get('location.zip')
#         longitude = data.get('location.longitude')
#         latitude = data.get('location.latitude')
#         address = data.get('location.address')
#         make = data.get('make')
#         model = data.get('model')
#         color = data.get('color')
#         year = data.get('year')
#         price = data.get('jobInfo.price')

#         dispatch_entry = DispatchEntry.objects.create(
#             service_id=service_id,
#             customer_id=customer_id,
#             customer_name=customer_name,
#             phone=phone,
#             email=email,
#             device=device,
#             street=street,
#             city=city,
#             state=state,
#             zip_code=zip_code,
#             longitude=longitude,
#             latitude=latitude,
#             address=address,
#             make=make,
#             model=model,
#             color=color,
#             year=year,
#             price=price
#         )
#         return JsonResponse({'message': 'DispatchEntry created successfully.'}, status=201)
#     return JsonResponse({'error': 'Invalid request method.'}, status=400)