from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = "Доктора"

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    details = models.TextField()

    def __str__(self):
        return f"{self.patient.username} - {self.doctor.name} on {self.appointment_date}"


class Result(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пациент",
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата исследования",
    )
    medical_test = models.CharField(
        max_length=200,
        verbose_name="Название исследования",
    )
    test_result = models.CharField(
        max_length=150,
        verbose_name="Результат",
    )

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"
        ordering = ["-date"]

    def __str__(self):
        return (
            f"Пациент {self.user.last_name}, Исследование: {self.medical_test}, "
            f"Результат: {self.test_result}"
        )
