from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from . models import Student
# Create your views here.

class StudentViews(APIView):
    def post(self, request):
        serializer_class = StudentSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({"status": "success", "data": serializer_class.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer_class.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            query = Student.objects.get(id=id)
            serializer = StudentSerializer(query)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        query = Student.objects.all()
        serializer_class = StudentSerializer(query, many=True)
        return Response({"status": "success", "data": serializer_class.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        query = Student.objects.get(id=id)
        serializer = StudentSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        query = get_object_or_404(Student, id=id)
        query.delete()
        return Response({"status": "success", "data": "Item Deleted"})



