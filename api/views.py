# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Students
from .serializers import StudentsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employee.models import Employee
from .serializers import EmployeeSerializer
from django.http import Http404

# Create your views here.
@api_view(['GET','POST'])
def studentsViews(request):
    # std=Students.objects.all()
    # std_list=list(std.values())
    # print(std_list)
    if request.method=='GET':
        std=Students.objects.all()
        serializer=StudentsSerializer(std,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])   
def studentDetailViews(request,pk):
    try:
        student=Students.objects.get(id=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  
    if request.method=='GET':
        serializer=StudentsSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)    
    elif request.method=='PUT':
        serializer=StudentsSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class employee(APIView):
    def get(self,request):
        emp=Employee.objects.all()
        serializer=EmployeeSerializer(emp,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    def post(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
class employeeDetail(APIView):
    def get_object(self,pk):
        try:
            return Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        emp=self.get_object(pk)
        serializer=EmployeeSerializer(emp)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
           
    