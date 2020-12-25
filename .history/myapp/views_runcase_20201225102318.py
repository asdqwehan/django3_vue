import os, json
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from myapp.models import CaseInput, HeadersG
