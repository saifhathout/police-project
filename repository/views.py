from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache
from django.contrib import messages
from .models import Material
from .forms import MaterialForm

# Add this new introduction view
@never_cache
def introduction(request):
    return render(request, 'introduction.html')

@never_cache
def home(request):
    query = request.GET.get('q')
    if query:
        materials = Material.objects.filter(name__istartswith=query).order_by('-uploaded_at')
    else:
        materials = Material.objects.all().order_by('-uploaded_at')
    
    return render(request, 'home.html', {'materials': materials})

@never_cache
def upload_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Material uploaded successfully!')
            return redirect('home')
    else:
        form = MaterialForm()
    
    return render(request, 'upload.html', {'form': form})

@never_cache
def material_detail(request, id):
    material = get_object_or_404(Material, id=id)
    return render(request, 'detail.html', {'material': material})

@never_cache
def delete_material(request, id):
    material = get_object_or_404(Material, id=id)
    
    if request.method == 'POST':
        if material.picture:
            material.picture.delete()
        material.delete()
        messages.success(request, f'"{material.name}" has been deleted successfully!')
        return redirect('home')
    
    return render(request, 'confirm_delete.html', {'material': material})

# أضف هذه الدالة (الصفحة الأولى)
@never_cache
def first_page(request):
    return render(request, 'first_page.html')

# أضف هذه الدالة (الصفحة الثانية)
@never_cache
def second_page(request):
    return render(request, 'second_page.html')

# دوال الأقسام
@never_cache
def section1_page(request):
    query = request.GET.get('q', '')
    if query:
        materials = Material.objects.filter(
            name__icontains=query,
            department='section1'
        ).order_by('-uploaded_at')
    else:
        materials = Material.objects.filter(department='section1').order_by('-uploaded_at')
    
    return render(request, 'section_page.html', {
        'materials': materials,
        'section_name': 'القسم الأول - محجوزين',
        'section_number': 1,
        'section_color': '#1e3c72',
        'section_icon': '🔒',
        'query': query
    })

@never_cache
def section2_page(request):
    query = request.GET.get('q', '')
    if query:
        materials = Material.objects.filter(
            name__icontains=query,
            department='section2'
        ).order_by('-uploaded_at')
    else:
        materials = Material.objects.filter(department='section2').order_by('-uploaded_at')
    
    return render(request, 'section_page.html', {
        'materials': materials,
        'section_name': 'القسم الثاني - محبوسين',
        'section_number': 2,
        'section_color': '#11998e',
        'section_icon': '⛓️',
        'query': query
    })

@never_cache
def section3_page(request):
    query = request.GET.get('q', '')
    if query:
        materials = Material.objects.filter(
            name__icontains=query,
            department='section3'
        ).order_by('-uploaded_at')
    else:
        materials = Material.objects.filter(department='section3').order_by('-uploaded_at')
    
    return render(request, 'section_page.html', {
        'materials': materials,
        'section_name': 'القسم الثالث - محكوم عليهم',
        'section_number': 3,
        'section_color': '#cb2d3e',
        'section_icon': '⚖️',
        'query': query
    })

# دوال رفع البيانات لكل قسم
@never_cache
def upload_section1(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.department = 'section1'
            material.save()
            messages.success(request, '✅ تم حفظ البيانات في القسم 1 بنجاح!')
            return redirect('section1_page')
        else:
            messages.error(request, '❌ يرجى تصحيح الأخطاء أدناه')
    else:
        form = MaterialForm()
    
    return render(request, 'upload_section.html', {
        'form': form,
        'section_name': 'القسم الأول',
        'section_number': 1,
        'section_color': '#1e3c72',
        'section_icon': '🔒'
    })

@never_cache
def upload_section2(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.department = 'section2'
            material.save()
            messages.success(request, '✅ تم حفظ البيانات في القسم 2 بنجاح!')
            return redirect('section2_page')
        else:
            messages.error(request, '❌ يرجى تصحيح الأخطاء أدناه')
    else:
        form = MaterialForm()
    
    return render(request, 'upload_section.html', {
        'form': form,
        'section_name': 'القسم الثاني',
        'section_number': 2,
        'section_color': '#11998e',
        'section_icon': '⛓️'
    })

@never_cache
def upload_section3(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.department = 'section3'
            material.save()
            messages.success(request, '✅ تم حفظ البيانات في القسم 3 بنجاح!')
            return redirect('section3_page')
        else:
            messages.error(request, '❌ يرجى تصحيح الأخطاء أدناه')
    else:
        form = MaterialForm()
    
    return render(request, 'upload_section.html', {
        'form': form,
        'section_name': 'القسم الثالث',
        'section_number': 3,
        'section_color': '#cb2d3e',
        'section_icon': '⚖️'
    })




# repository/views.py - تحديث دوال الأقسام

@never_cache
def section1_page(request):
    query = request.GET.get('q', '')
    sort_by = request.GET.get('sort', 'date_sessions')  # إضافة متغير الترتيب
    
    if query:
        materials = Material.objects.filter(
            name__icontains=query,
            department='section1'
        ).order_by(sort_by)
    else:
        materials = Material.objects.filter(department='section1').order_by(sort_by)
    
    return render(request, 'section_page.html', {
        'materials': materials,
        'section_name': 'القسم الأول - محجوزين',
        'section_number': 1,
        'section_color': '#1e3c72',
        'section_icon': '🔒',
        'query': query,
        'sort_by': sort_by,
    })

@never_cache
def section2_page(request):
    query = request.GET.get('q', '')
    sort_by = request.GET.get('sort', 'date_sessions')
    
    if query:
        materials = Material.objects.filter(
            name__icontains=query,
            department='section2'
        ).order_by(sort_by)
    else:
        materials = Material.objects.filter(department='section2').order_by(sort_by)
    
    return render(request, 'section_page.html', {
        'materials': materials,
        'section_name': 'القسم الثاني - محبوسين',
        'section_number': 2,
        'section_color': '#11998e',
        'section_icon': '⛓️',
        'query': query,
        'sort_by': sort_by,
    })

@never_cache
def section3_page(request):
    query = request.GET.get('q', '')
    sort_by = request.GET.get('sort', '-date_sessions')
    
    if query:
        materials = Material.objects.filter(
            name__icontains=query,
            department='section3'
        ).order_by(sort_by)
    else:
        materials = Material.objects.filter(department='section3').order_by(sort_by)
    
    return render(request, 'section_page.html', {
        'materials': materials,
        'section_name': 'القسم الثالث - محكوم عليهم',
        'section_number': 3,
        'section_color': '#cb2d3e',
        'section_icon': '⚖️',
        'query': query,
        'sort_by': sort_by,
    })


# repository/views.py - أضف هذه الدالة

@never_cache
def edit_session(request, id):
    material = get_object_or_404(Material, id=id)
    
    if request.method == 'POST':
        new_date = request.POST.get('date_sessions')
        if new_date:
            material.date_sessions = new_date
            material.save()
            messages.success(request, '✅ تم تحديث تاريخ الجلسة بنجاح!')
        else:
            messages.error(request, '❌ يرجى إدخال تاريخ صحيح')
        
        # العودة إلى صفحة التفاصيل
        return redirect('material_detail', id=material.id)
    
    return render(request, 'edit_session.html', {
        'material': material,
    })