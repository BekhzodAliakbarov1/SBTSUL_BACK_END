from django.db import models

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    paragraph = models.TextField(max_length=1000, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class News(models.Model):
    titleUzb = models.CharField(max_length=200, blank=True, null=True)
    titleRus = models.CharField(max_length=200, blank=True, null=True)
    titleEng = models.CharField(max_length=200, blank=True, null=True)
    paragraphUzb = models.TextField(max_length=1000, blank=True, null=True)
    paragraphRus = models.TextField(max_length=1000, blank=True, null=True)
    paragraphEng = models.TextField(max_length=1000, blank=True, null=True)
    date = models.DateField(auto_now=True, blank=True, null=True)
    pictureURL = models.CharField(max_length=2000, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.titleUzb


class Students(models.Model):
    nameUzb = models.CharField(max_length=200, blank=True, null=True)
    nameRus = models.CharField(max_length=200, blank=True, null=True)
    nameEng = models.CharField(max_length=200, blank=True, null=True)
    informationUzb = models.TextField(max_length=1000, blank=True, null=True)
    informationRus = models.TextField(max_length=1000, blank=True, null=True)
    informationEng = models.TextField(max_length=1000, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.nameUzb


class Quotas(models.Model):
    titleUzb = models.CharField(max_length=200, blank=True, null=True)
    titleEng = models.CharField(max_length=200, blank=True, null=True)
    titleRus = models.CharField(max_length=200, blank=True, null=True)
    numberOfAllQuotasUzb = models.TextField(
        max_length=1000, blank=True, null=True)
    numberOfAllQuotasRus = models.TextField(
        max_length=1000, blank=True, null=True)
    numberOfAllQuotasEng = models.TextField(
        max_length=1000, blank=True, null=True)
    numberOfStudentsAllUzb = models.TextField(
        max_length=1000, blank=True, null=True)
    numberOfStudentsAllRus = models.TextField(
        max_length=1000, blank=True, null=True)
    numberOfStudentsAllEng = models.TextField(
        max_length=1000, blank=True, null=True)
    numberOfStudentsDailyUzb = models.TextField(
        max_length=1000, blank=True, null=True)
    numberOfStudentsDailyEng = models.TextField(
        max_length=1000, blank=True, null=True)
    numberOfStudentsDailyRus = models.TextField(
        max_length=1000, blank=True, null=True)
    date = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.titleUzb


class Images(models.Model):
    titleUzb = models.CharField(max_length=200, blank=True, null=True)
    titleRus = models.CharField(max_length=200, blank=True, null=True)
    titleEng = models.CharField(max_length=200, blank=True, null=True)
    pictureURL = models.CharField(max_length=2000, blank=True, null=True)
    date = models.DateField(auto_now=True, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.titleUzb


class Vacancys(models.Model):
    titleUzb = models.CharField(max_length=200, blank=True, null=True)
    titleRus = models.CharField(max_length=200, blank=True, null=True)
    titleEng = models.CharField(max_length=200, blank=True, null=True)
    subTitleUzb = models.CharField(max_length=200, blank=True, null=True)
    subTitleRus = models.CharField(max_length=200, blank=True, null=True)
    subTitleEng = models.CharField(max_length=200, blank=True, null=True)
    paragraphUzb = models.TextField(max_length=1000, blank=True, null=True)
    paragraphRus = models.TextField(max_length=1000, blank=True, null=True)
    paragraphEng = models.TextField(max_length=1000, blank=True, null=True)
    costUzb = models.TextField(max_length=1000, blank=True, null=True)
    costRus = models.TextField(max_length=1000, blank=True, null=True)
    costEng = models.TextField(max_length=1000, blank=True, null=True)
    date = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.titleUzb
