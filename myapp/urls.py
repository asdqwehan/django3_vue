from django.urls import path
from myapp import views, tasks

urlpatterns = [
    path('test_login', views.test_login),
    # path('output_res', tasks.output_res),
    path('show_cases', views.show_cases),
    path('case_detail/<int:case_id>/', views.case_detail),
    path('create_case', views.create_case),
    path('edit_case/<int:case_id>', views.edit_case),
]