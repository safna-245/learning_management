from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListAPIView

from course_management.serializers import UserSerializer,CourseSerializer
from course_management.models import Course


class AdminCreateView(APIView):

    def post(self, request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_superuser(**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class UserCreateView(APIView):

    def post(self, request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_user(**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

# class CourseListView(APIView):

#     authentication_classes = [authentication.TokenAuthentication]

#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):

#         instance = Course.objects.all()

#         serializer_instance = CourseSerializer(instance, many=True)

#         return Response(data=serializer_instance.data)

class CourseListView(ListAPIView):

    authentication_classes = [authentication.BasicAuthentication]
    
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = CourseSerializer

    queryset = Course.objects.all()

    
class CourseCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def post(self, request):

        form_data = request.data

        serializer_instance = CourseSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)


class CourseRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = CourseSerializer

    queryset = Course.objects.all()


