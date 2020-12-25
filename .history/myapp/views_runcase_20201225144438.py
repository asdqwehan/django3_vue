import os, json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers


from myapp.models import CaseInput, HeadersG

def run_case(case_id, headers_id):
    case = CaseInput.objects.get(id=case_id)
    headers = HeadersG.objects.get(headers_id)
    data = case.case_body
    