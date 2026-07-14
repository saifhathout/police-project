# repository/models.py
from django.db import models

class Material(models.Model):
    # خيارات الأقسام
    DEPARTMENT_CHOICES = [
        ('section1', 'القسم الأول'),
        ('section2', 'القسم الثاني'),
        ('section3', 'القسم الثالث'),
    ]
    
    name = models.CharField(max_length=200, verbose_name="الاسم")
    age = models.IntegerField(verbose_name="العمر")
    address = models.CharField(max_length=300, default='', blank=True, verbose_name="العنوان")
    case_number = models.CharField(max_length=100, default='', blank=True, verbose_name="رقم القضية")
    case_type = models.CharField(max_length=200, default='', blank=True, verbose_name="نوع القضية")
    date_sessions = models.DateField(null=True, blank=True, verbose_name="تاريخ الجلسات") 
    paper = models.FileField(upload_to='papers/', null=True, blank=True, verbose_name="الاوراق الخاصة بالمتهم")
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES, default='section1', verbose_name="القسم")
    picture = models.ImageField(upload_to='pictures/', null=True, blank=True, verbose_name="الصورة")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الرفع")

    def __str__(self):
        return f"{self.name} - {self.get_department_display()}"
    