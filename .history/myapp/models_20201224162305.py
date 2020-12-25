from django.db import models

# Create your models here.

class HeadersG(models.Model):
    user_agent = models.TextField(default="User-Agent")
    content_type = models.CharField(max_length=64, default="Content-Type")
    token = models.CharField(max_length=256, default="token")


class CaseInput(models.Model):
    case_name = models.CharField(max_length=64)
    case_url = models.TextField()
    #case_body = models.TextField()
    case_body = models.JSONField()
    case_method = models.CharField(max_length=32)
    case_assert = models.TextField()
    case_add_time = models.DateTimeField(auto_now_add=True, null=False)
    case_file_path = models.TextField()

class CaseResult(models.Model):
    #case_name = models.Foreignkey()
    case_name = models.CharField(max_length=64)
    cost_time = models.CharField(max_length=64)
    result_add_time = models.DateTimeField(auto_now_add=True, null=False)
    result_content = models.TextField()

class TestProject(models.Model):
    project_name = models.CharField(max_length=32)
    has_cases = models.TextField()

class TestLog(models.Model):
    log_name = models.CharField(max_length=32)
    log_add_time = models.DateTimeField(auto_now_add=True, null=False)
    log_content = models.TextField()