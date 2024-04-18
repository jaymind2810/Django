from django.urls import path, include
from . import views
from .views import StudentView, StudentDetail, StudentList, UserDetail, UserList, StudentHighlight


urlpatterns = [
    # =========== Rest API ==================
    path('basic/', StudentView.as_view()),
    path('basic/<int:id>/', StudentView.as_view()),

    # ========== Using Permission =================
    path('std/', StudentList.as_view()),
    path('std/<int:pk>/', StudentDetail.as_view()),

    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),

    path('student/<int:pk>/highlight/', StudentHighlight.as_view()),

    # ========== Serializer Use Case =================
    path('student/', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),

    # ========== Django Forms =================
    path('student_home/', views.student_home_view, name='student_home_view'),
    path('submit_form/', views.submit_form, name='submit_form'),
    path('success/', views.success, name='success'),
    path('student_home/<int:id>', views.update_student_form, name='update_student_form'),

]