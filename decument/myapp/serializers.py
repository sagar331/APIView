from rest_framework import serializers
from .models import *
#USERS
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=USERS
        fields=['USER_NAME','EMAIL_iD','MOBILE_NUMBER','PLAN']
#Previous_plan 
class Previous_planSerializer(serializers.ModelSerializer):          #PlanSerial
    class Meta:
        model=Previous_plan
        fields=['plan_name','plan_type','date','Amount','discount','transaction_id']            

class PlanTypeSeialiser(serializers.ModelSerializer):
    class Meta:
        model=USERS
        fields=('USER_NAME','EMAIL_iD')
#Download
class All_download_filesSerializatio(serializers.ModelSerializer):     #DownloadSerial
    class Meta:
        model=All_download_files
        fields=['File_name','file_size','Date']
#AllPlan        
class AllPlanSerializer(serializers.ModelSerializer):
    plan_type=UserSerializer()
    class Meta:
        model=Previous_plan
        fields=['id','plan_name','plan_type','Amount','discount']
#Document
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Document
        fields=['Business','Realestate','Financial','Family','All','uploaded_at']
#TestiMonial
class TestiMonialSerializare(serializers.ModelSerializer):
    class Meta:
        model=TestiMonial
        fields=['username','UserDetail','User_Test']