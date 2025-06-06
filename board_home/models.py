from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class StudyPost(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=50)
    participants = models.CharField(max_length=20)  # 예: "3/5"
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class CustomUserManager(BaseUserManager):
    def create_user(self, student_id, name, password=None):
        if not student_id:
            raise ValueError('학번은 필수입니다.')
        user = self.model(student_id=student_id, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, student_id, name, password):
        user = self.create_user(student_id=student_id, name=name, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    ROLE_CHOICES = (
        ('student', '학부생'),
        ('professor', '교수'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    objects = CustomUserManager()

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['name', 'role']



# 공지사항용 모델
class Notice(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    date = models.DateField()
    link = models.URLField()

    def __str__(self):
        return self.title
