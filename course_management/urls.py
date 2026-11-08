from django.urls import path

from course_management.views import AdminCreateView,UserCreateView
from course_management.views import CourseListView
from course_management.views import CourseCreateView
from course_management.views import CourseRetrieveUpdateDeleteView


urlpatterns=[
     path('register/', AdminCreateView.as_view()),
     path('register/user/', UserCreateView.as_view()),
     path('all/', CourseListView.as_view()),
     path('courses/create/', CourseCreateView.as_view()),
     path('courses/<int:pk>/', CourseRetrieveUpdateDeleteView.as_view()),

]