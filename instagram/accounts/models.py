from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "남성"
        FEMALE = "F", "여성"

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(validators=[RegexValidator(r"^010-?\d{4}-?\d{4}$")], max_length=15, blank=True)
    gender = models.CharField(choices=GenderChoices.choices, max_length=10, blank=True)
    avatar = models.ImageField(blank=True, upload_to="accounts/avatar/%Y/%m/%d", help_text="48px * 48px 크기의 png/jpg 파일을 업로드 해주세요.")
