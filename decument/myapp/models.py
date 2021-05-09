from django.db import models
import datetime
# Create your models here.
#USERS
class USERS(models.Model):
    USER_NAME=models.CharField(max_length=30,null=True,blank=True)
    EMAIL_iD=models.EmailField(max_length=250,null=True,blank=True)
    MOBILE_NUMBER=models.BigIntegerField()
    plan=(
        ('monthly','monthly'),
        ('anual','anual'),
        ('unlimited','unlimited')
    )
    PLAN=models.CharField(max_length=20,choices=plan)
    def __str__(self):
        return self.PLAN
#Previous_plan        
class Previous_plan(models.Model):
    plan_name=models.CharField(max_length=30,null=True,blank=True)
    plan_type=models.ForeignKey(USERS,on_delete=models.CASCADE)
    date=models.DateField()
    Amount=models.FloatField()
    discount=models.CharField(max_length=30,null=True,blank=True)
    transaction_id=models.BigIntegerField()
    def __str__(self):
        return self.plan_type.PLAN
#Download        
class All_download_files(models.Model):
    File_name=models.CharField(max_length=30,null=True,blank=True)
    file_size=models.FileField(upload_to='file/')
    Date=models.DateField()
    def __str__(self):
        return self.File_name
#AllPlan
class AllPlan(Previous_plan):
    Action=models.FileField(upload_to='allplan/')
    # def __str__(self):
    #     return self.Action
#Document    
class Document(models.Model):
    Business = models.FileField(upload_to='documents/')
    Realestate=models.FileField(upload_to='Realestate/')
    Financial=models.FileField(upload_to='Financial/')
    Family=models.FileField(upload_to='Family/')
    All=models.FileField(upload_to='All/')
    uploaded_at=models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.uploaded
#TestiMonial    
class TestiMonial(models.Model):
    username=models.CharField(max_length=30)
    UserDetail=models.CharField(max_length=30)
    User_Test=models.TextField(max_length=150)
    def __str__(self):
        return self.username