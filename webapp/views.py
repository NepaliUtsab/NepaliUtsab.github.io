from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Student
from .serializers import studentSerializer



# Create your views here.
class studentList(APIView):
        
        def get(self, request):
                students = Student.objects.all()
                serializer = studentSerializer(students, many = True)
                content = {'status':'success','data':serializer.data}
                
                return Response(content)
        
        def post(self, request):
                students = Student.objects.all()
                serializer = studentSerializer(students, many = True)
                form = self.form_class(request.POST)
                return render(request, self.template_name, {'form': form})
        
    