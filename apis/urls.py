from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('messages/', views.messageList, name="message-list"),
    path('messages/add/', views.messageCreate, name="message-create"),
    path('messages/edit/<str:pk>/', views.messageUpdate, name="message-update"),
    path('messages/delete/<str:pk>/', views.messageDelete, name="message-delete"),

    path('students/', views.studentList, name="student-list"),
    path('students/add/', views.studentCreate, name="student-create"),
    path('students/edit/<str:pk>/', views.studentUpdate, name="student-update"),
    path('students/delete/<str:pk>/', views.studentDelete, name="student-delete"),

    path('news/', views.newList, name="new-list"),
    path('news/add/', views.newCreate, name="new-create"),
    path('news/edit/<str:pk>/', views.newUpdate, name="new-update"),
    path('news/delete/<str:pk>/', views.newDelete, name="new-delete"),

    path('quotas/', views.quotaList, name="quota-list"),
    path('quotas/add/', views.quotaCreate, name="quota-create"),
    path('quotas/edit/<str:pk>/', views.quotaUpdate, name="quota-update"),
    path('quotas/delete/<str:pk>/', views.quotaDelete, name="quota-delete"),

    path('images/', views.imageList, name="image-list"),
    path('images/add/', views.imageCreate, name="image-create"),
    path('images/edit/<str:pk>/', views.imageUpdate, name="image-update"),
    path('images/delete/<str:pk>/', views.imageDelete, name="image-delete"),

    path('vacancy/', views.vacancyList, name="vacancy-list"),
    path('vacancy/add/', views.vacancyCreate, name="vacancy-create"),
    path('vacancy/edit/<str:pk>/', views.vacancyUpdate, name="vacancy-update"),
    path('vacancy/delete/<str:pk>/', views.vacancyDelete, name="vacancy-delete"),
]
