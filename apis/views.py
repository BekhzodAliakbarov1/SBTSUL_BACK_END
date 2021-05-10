from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

from .models import *


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'MessagesURL': 'messages/ ; messages/add/ ; messages/edit/<str:pk>/ ; messages/delete/<str:pk>/ ',
        'NewsURL': 'news/ ; news/add/ ; news/edit/<str:pk>/ ; news/delete/<str:pk>/ ',
        'StudentsURL': 'students/ ; students/add/ ; students/edit/<str:pk>/ ; students/delete/<str:pk>/ ',
        'QuotasURL': 'quotas/ ; quotas/add/ ; quotas/edit/<str:pk>/ ; quotas/delete/<str:pk>/ ',
        'ImagesURL': 'images/ ; images/add/ ; images/edit/<str:pk>/ ; images/delete/<str:pk>/ ',
        'VacancyURL': 'vacancy/ ; vacancy/add/ ; vacancy/edit/<str:pk>/ ; vacancy/delete/<str:pk>/ ',

    }
    return Response(api_urls)


# GET ALL
@api_view(['GET'])
def messageList(request):
    messages = Message.objects.all().order_by('-id')
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def studentList(request):
    students = Students.objects.all().order_by('-id')
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def newList(request):
    news = News.objects.all().order_by('-id')
    serializer = NewSerializer(news, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def quotaList(request):
    quotas = Quotas.objects.all().order_by('-id')
    serializer = QuotaSerializer(quotas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def vacancyList(request):
    vacancys = Vacancys.objects.all().order_by('-id')
    serializer = VacancySerializer(vacancys, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def imageList(request):
    images = Images.objects.all().order_by('-id')
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)

# CREATE ALL


@api_view(['POST'])
def messageCreate(request):
    serializer = MessageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def studentCreate(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def newCreate(request):
    serializer = NewSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def quotaCreate(request):
    serializer = QuotaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def vacancyCreate(request):
    serializer = VacancySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def imageCreate(request):
    serializer = ImageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# CREATE UPDATE


@api_view(['POST'])
def messageUpdate(request, pk):
    message = Message.objects.get(id=pk)
    serializer = MessageSerializer(instance=message, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def studentUpdate(request, pk):
    student = Students.objects.get(id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def newUpdate(request, pk):
    new = News.objects.get(id=pk)
    serializer = NewSerializer(instance=new, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def quotaUpdate(request, pk):
    quota = Quotas.objects.get(id=pk)
    serializer = QuotaSerializer(instance=quota, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def vacancyUpdate(request, pk):
    vacancy = Vacancys.objects.get(id=pk)
    serializer = VacancySerializer(instance=vacancy, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def imageUpdate(request, pk):
    image = Images.objects.get(id=pk)
    serializer = ImageSerializer(instance=image, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# CREATE DELETE


@api_view(['DELETE'])
def messageDelete(request, pk):
    message = Message.objects.get(id=pk)
    message.delete()

    return Response('Item succsesfully delete!')


@api_view(['DELETE'])
def studentDelete(request, pk):
    student = Students.objects.get(id=pk)
    student.delete()

    return Response('Item succsesfully delete!')


@api_view(['DELETE'])
def newDelete(request, pk):
    new = News.objects.get(id=pk)
    new.delete()

    return Response('Item succsesfully delete!')


@api_view(['DELETE'])
def quotaDelete(request, pk):
    quota = Quotas.objects.get(id=pk)
    quota.delete()

    return Response('Item succsesfully delete!')


@api_view(['DELETE'])
def vacancyDelete(request, pk):
    vacancy = Vacancys.objects.get(id=pk)
    vacancy.delete()

    return Response('Item succsesfully delete!')


@api_view(['DELETE'])
def imageDelete(request, pk):
    image = Images.objects.get(id=pk)
    image.delete()

    return Response('Item succsesfully delete!')
