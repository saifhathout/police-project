# repository/forms.py
from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'age', 'address','case_number', 'case_type', 'date_sessions', 'paper', 'picture']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل الاسم الكامل'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل العمر'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل العنوان'}),
            'case_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل رقم القضية'}),
            'case_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل نوع القضية'}),
            'date_sessions': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'اختر تاريخ الجلسة'}),
            'paper': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'الاسم الكامل',
            'age': 'العمر',
            'address': 'العنوان',
            'case_number': 'رقم القضية',
            'case_type': 'نوع القضية',
            'date_sessions': 'تاريخ الجلسات',
            'paper': 'الأوراق الخاصة بالمتهم',
            'picture': 'الصورة الشخصية',
        }