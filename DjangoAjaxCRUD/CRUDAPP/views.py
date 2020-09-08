from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import StudentData
import json

# Create your views here.
from CRUDAPP.models import StudentData

def HomePage(request):
    students = StudentData.objects.all()
    return render(request,"homepage.html",{"students":students})

@csrf_exempt
def InsertStudent(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    gender = request.POST.get("gender")
    
    try:
        student = StudentData(name = name, email = email, gender = gender)
        student.save()
        student_data = {"id":student.id, "created_at":student.created_at,"error":False,"errorMessage":"Student Added Successfully"}
        return JsonResponse(student_data,safe=False)
    except:
        student_data = {"error":True,"errorMessage":"Failed To Add Student"}
        return JsonResponse(student_data,safe=False)

@csrf_exempt
def update_all(request):
    data=request.POST.get("data")
    dict_data=json.loads(data)
    try:
        for dic_single in dict_data:
            student = StudentData.objects.get(id=dic_single['id'])
            student.name = dic_single['name']
            student.email = dic_single['email']
            student.gender = dic_single['gender']
            student.save()
        student_data = {"error":False,"errorMessage":"Data Updated Successfully"}
        return JsonResponse(student_data,safe=False)
    except:
        student_data = {"error":True,"errorMessage":"Failed To Update Data"}
        return JsonResponse(student_data,safe=False)

@csrf_exempt
def delete_data(request):
    id = request.POST.get('id')
    try:    
        student = StudentData.objects.get(id=id)
        student.delete()
        student_data = {"error":False,"errorMessage":"Data Deleted Successfully"}
        return JsonResponse(student_data,safe=False)
    except:
        student_data = {"error":True,"errorMessage":"Failed To Delete Data"}
        return JsonResponse(student_data,safe=False)