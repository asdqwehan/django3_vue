import os, json
from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import CaseInput
from django.core import serializers #序列化

from myapp import tasks


# Create your views here.

def test_login(request):
    response = {}
    try:
        response['msg'] = 'success'
        response['error_num'] = 0
        #tasks.output_res.delay(response)
        os.system('python d:\\TestFramework\\cases\\test_movtile_login.py')
        # response['msg'] = 'success'
        # response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def show_cases(request):
    """测试用例展示列表"""
    response = {}
    try:
        # case_list = CaseInput.objects.values() # .value(),则返回的是一个 ValueQuerySet 格式的数据
        # ValuQuerySet是QuerySet的子类,返回的是一个字典dict并不是一个列表list数据.
        case_list = CaseInput.objects.all()
        response['msg'] = json.loads(serializers.serialize('json', case_list))
        response['code'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1
    print(response['msg'])
    return JsonResponse(response)

def case_detail(request, case_id):
    """用例详情"""
    response = {}
    try:
        case = CaseInput.objects.filter(id=case_id)
        response['msg'] = json.loads(serializers.serialize('json', case))
        response['code'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1
    print(response['msg'])
    #res = json.parser(response)
    return JsonResponse(response)

def create_case(request):
    """添加用例"""
    response = {}
    if request.method == "POST":
        try:
            #request_body = request.POST #request.POST()部分无法获取,如application/json,只能使用request.body()
            #body = json.loads(request_body)
            #body = request_body
            #print(json.loads(request.body))
            body = json.loads(request.body)

            CaseInput.objects.create(
                case_name = body['case_name'],
                case_method = body['case_method'],
                case_url = body['case_url'],
                case_body = body['case_body'],
                case_assert = body['case_assert'],
                case_file_path = body['case_file_path'],
            )
            response['msg'] = '创建成功'
            response['code'] = 0
        except Exception as e:
            response['msg'] = str(e)
            response['code'] = 1
    return JsonResponse(response)

def edit_case(request, case_id):
    """修改用例"""
    response = {}
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            print(body)
            CaseInput.objects.filter(id=case_id).update(
                case_name = body['case_name'],
                case_method = body['case_method'],
                case_url = body['case_url'],
                case_body = body['case_body'],
                case_assert = body['case_assert'],
                case_file_path = body['case_file_path'],
            )
            response['msg'] = '修改成功'
            response['code'] = 0
        except Exception as e:
            response['msg'] = str(e)
            response['code'] = 1
    return JsonResponse(response)