from django.contrib import admin
# from myapp.models import *
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display=["USER_NAME","EMAIL_iD","MOBILE_NUMBER","PLAN"]

class Preplan(admin.ModelAdmin):
    list_display=["plan_name","plan_type","date","Amount","transaction_id","discount"]

class DownloadAdmin(admin.ModelAdmin):
    list_display=["File_name","file_size","Date"]

class AllplanAdmin(admin.ModelAdmin):
    list_display=['Action']

class DocAdmin(admin.ModelAdmin):
     list_display=['Business','Realestate','Financial','Family','All','uploaded_at']

class TestAdmin(admin.ModelAdmin):
    list_display=['username','UserDetail','User_Test']    

admin.site.register(USERS,UserAdmin)
admin.site.register(Previous_plan,Preplan)
admin.site.register(All_download_files,DownloadAdmin)
admin.site.register(AllPlan,AllplanAdmin)
admin.site.register(Document,DocAdmin)
admin.site.register(TestiMonial,TestAdmin)