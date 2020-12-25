from django.urls import path
from myapp import views, views_runcase, tasks

urlpatterns = [
    path('test_login', views.test_login),
    # path('output_res', tasks.output_res),
    #"""用例"""
    path('show_cases', views.show_cases),
    path('case_detail/<int:case_id>/', views.case_detail),
    path('create_case', views.create_case),
    path('edit_case/<int:case_id>', views.edit_case),
    path('delete_case/<int:case_id>', views.delete_case),

    #"""headers"""
    path('show_headers', views.show_headers),
    path('add_headers', views.add_headers),

    #"""执行用例"""
    path('run_case', views_runcase.run_case),
]