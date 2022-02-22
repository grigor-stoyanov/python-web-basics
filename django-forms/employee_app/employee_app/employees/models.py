from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.core import validators


class TestModel(models.Model):
    id2 = models.IntegerField(
        primary_key=True
    )


class AuditEntity(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )

    # makes abstract class and stops generating a table
    class Meta:
        abstract = True


class Department(AuditEntity):
    name = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('department details', kwargs={id: self.id})


class Employee(models.Model):
    class Meta:
        ordering = ('company', 'first_name')

    image = models.ImageField(null=True, blank=True)
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    age = models.IntegerField()
    email = models.EmailField(max_length=60)
    egn = models.CharField(max_length=10, unique=True, verbose_name='EGN',
                           validators=(validators.MaxLengthValidator(10),)
                           )
    SOFTWARE_DEVELOPER = 1
    QA_ENGINEER = 2
    DEV_OPS = 3
    job_title = models.IntegerField(
        max_length=20,
        choices=(
            (SOFTWARE_DEVELOPER, 'Software Developer'),
            (QA_ENGINEER, 'QA Engineer'),
            (DEV_OPS, 'Dev Ops Specialist')
        )
    )
    SOFT_UNI = 'SoftUni'
    GOOGLE = 'Google'
    FACEBOOK = 'Facebook'
    COMPANIES = [SOFT_UNI, GOOGLE, FACEBOOK]
    company = models.CharField(
        max_length=max(len(c) for c in COMPANIES),
        choices=(
            (SOFT_UNI, SOFT_UNI),
            (GOOGLE, GOOGLE),
            (FACEBOOK, FACEBOOK)
        )
    )
    # one to many
    department = models.ForeignKey(
        Department,
        # delete all employees of department when dep is deleted
        on_delete=models.CASCADE,
    )


class Project(models.Model):
    name = models.CharField(max_length=30, )
    deadline = models.DateField(null=True, blank=True, )
    # generates a connecting table on its own
    # needs to be only in 1 of the tables
    employees = models.ManyToManyField(
        to=Employee
    )


class User(models.Model):
    username = models.CharField(max_length=254)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
