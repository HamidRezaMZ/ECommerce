import os

from django.db import models


# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}{ext}"
    return f"logo-image/{final_name}"


class SiteSettings(models.Model):

    siteTitle = models.CharField(max_length=150, verbose_name='عنوان سایت')
    address = models.CharField(max_length=300, verbose_name='آدرس')
    phone = models.CharField(max_length=50, verbose_name='تلفن')
    mobile = models.CharField(max_length=50, verbose_name='تلفن تماس')
    fax = models.CharField(max_length=50, verbose_name='فکس')
    email = models.EmailField(max_length=150, verbose_name='ایمیل')
    about_us = models.TextField(
     verbose_name='درباره ما', null=True, blank=True)
    copy_right = models.CharField(
      verbose_name='متن کپی رایت', null=True, blank=True, max_length=200)
    logo_image = models.ImageField(
       verbose_name="تصویر لوگو", null=True, blank=True, upload_to=upload_image_path)

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'مدریت تنظیمات'

    def __str__(self):
        return self.siteTitle
