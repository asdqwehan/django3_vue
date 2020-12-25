import os, json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers


from myapp.models import CaseInput, HeadersG

def run_case(self, case_id, headers_id):
    case = CaseInput.objects.get(id=case_id)
    headers_g = HeadersG.objects.get(headers_id)
    url = case.case_url
    data = case.case_body
    method = case.case_method
    headers = {
        "User-Agent": headers_g.user_agent,
        "Content-Type": headers_g.content_type,
        "token": headers_g.token
        }
    if method == "GET":
        response = requests.get(url=url, headers=headers)
        response = response.json()
        code = response['code']
        
        
    