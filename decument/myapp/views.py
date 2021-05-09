from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
#USERS
class UserView(APIView):
    def get(self,request):
        user=USERS.objects.all()
        serialdata=UserSerializer(user,many=True)
        return Response(serialdata.data)
    def post(self,request):
        serialdata=UserSerializer(data=request.data)
        if serialdata.is_valid():
            serialdata.save()
            return Response(serialdata.data,status=status.HTTP_201_CREATED)
        return Response(serialdata.errors,status.HTTP_400_BAD_REQUEST)
#Previous_plan        
class Previous_planView(APIView):
    def get(self,request):
        plan=Previous_plan.objects.all()
        srdata=Previous_planSerializer(plan,many=True)
        return Response(srdata.data)
    def post(self,request):
        srdata=Previous_planSerializer(data=request.data)
        if srdata.is_valid():
            srdata.save()
            return Response(srdata.data,status=status.HTTP_201_CREATED)
        return Response(srdata.errors,status.HTTP_400_BAD_REQUEST)
class PlanDetail(APIView):
    def get(self,request,pk):
        plan= Previous_plan.objects.get(pk=pk)
        srdata=Previous_planSerializer(plan)
        return Response(srdata.data)
    def put(self,request,pk):
        plan=Previous_plan.objects.get(pk=pk)
        srdata=Previous_planSerializer(plan,data=request.data)
        if srdata.is_valid():
            srdata.save()
            return Response(srdata.data)
        return Response(srdata.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        plan=Previous_plan.objects.get(pk=pk)
        plan.delete()
        return Response("successfully deleted")
#Download
class DownloadView(APIView):
    def get(self,request,pk):
        file=All_download_files.objects.get(id=pk)
        planser=All_download_filesSerializatio(file)
        return Response(planser.data)
    def post(self,request):
        planser=All_download_filesSerializatio(data=request.data)
        if planser.is_valid():
            planser.save()
            return Response(planser.data)
        return Response(planser.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        planser=All_download_filesSerializatio(data=request.data)
        if planser.is_valid():
            planser.save()
            return Response(planser.data)
        return Response(planser.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        file.delete()
        return Response("successfully deleted file")
#AllPlan
class AllPlanView(APIView):
    def get(self,request):
        plan=AllPlan.objects.all()
        planser=AllPlanSerializer(plan,many=True)
        return Response(planser.data)
    def post(self,request):
        planser=AllPlan(data=request.data)
        if AllPlanSerializer.is_valid():
            planser.save()
            return Response(planser.data)
        return Response(planser.errors,status=status.HTTP_400_BAD_REQUEST)

class PlanDelete(APIView):
    def get(self,request,pk):
        plan=AllPlan.objects.get(pk=pk)
        Planser=AllPlanSerializer(plan,many=True)
    def delete(self,request,pk):
        plan=AllPlan.objects.get(pk=pk)
        plan.delete()
        return Response("successfuly deleted")
#Document 
class DocView(APIView):
    def get(self,request):
        doc=Document.objects.all()
        docser=DocumentSerializer(doc,many=True)
        return Response(docser.data)
    def post(self,request):
        doc=Document.objects.all()
        docser=DocumentSerializer(data=request.data)
        if docser.is_valid():
            docser.save()
            return Response(docser.data,status=status.HTTP_201_CREATED)
        return Response(docser.errors,status.HTTP_400_BAD_REQUEST)
#TestiMonial
class TestView(APIView):
    def get(self,request):
        t=TestiMonial.objects.all()
        testser=TestiMonialSerializare(t,many=True)
        return Response(testser.data)
    def post(self,request):
        testser=TestiMonialSerializare(data=request.data)
        if testser.is_valid():
            testser.save()
            return Response(testser.data,status=status.HTTP_201_CREATED)
        return Response(testser.errors,status.HTTP_400_BAD_REQUEST)
