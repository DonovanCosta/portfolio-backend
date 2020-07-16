from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers

# Create your views here.

class Biography(APIView):
    """
    List all projects in the portfolio.
    """
    def get(self, request):
        biography = models.Biography.objects.first()
        serializer = serializers.BiographySerializer(biography, fields=('about_me','experience'))
        return Response(serializer.data)

class ProjectList(APIView):
    """
    List all projects in the portfolio.
    """
    def get(self, request):
        projects = models.Projects.objects.all()
        serializer = serializers.ProjectsSerializer(projects, context={'request': request}, fields=('id', 'project_name', 'image','short_description'), many=True)
        return Response(serializer.data)

class ProjectDetail(APIView):
    """
    Project detail - view project detail based on id.
    """
    def get(self,request, pk, format=None):
        project = models.Projects.objects.get(pk=pk)
        serializer = serializers.ProjectsSerializer(project, context={'request': request},)
        return Response(serializer.data)

class ContactMe(APIView):
    """
    Contact Me
    """

    def post(self, request, *args, **kwargs):
        serializer = serializers.ContactMeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            #store the info in the database
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            errors = serializer.errors
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)