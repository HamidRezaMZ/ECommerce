from django.db import models


# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=150, verbose_name='ایمیل')
    subject = models.CharField(max_length=200, verbose_name='عنوان پیام')
    text = models.TextField(verbose_name='پیام شما')
    is_read = models.BooleanField(verbose_name='خوانده شده/نشده')

    class Meta:
        verbose_name = ' تماس با ما'
        verbose_name_plural = 'تماس های کاربران'

    def __str__(self):
        return self.subject
