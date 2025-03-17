from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect

from users.forms import StudentForm

from .models import *

def home_page(request):
    fanlar = Fanlar.objects.all()
    student = Student.objects.all()

    db = {
        'fan': fanlar,
        'student':student
    }

    return render(request=request,template_name='index.html',context=db)


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request=request,template_name='add_stu.html',context={'form':form})




# def add_student(request):
#     if request.method == "POST":
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         tel_num = request.POST.get('tel_num')
#         fan_id = request.POST.get('fan')
#         email = request.POST.get('email')
#         fan = Fanlar.objects.get(id=fan_id)

#         Student.objects.create(
#             first_name=first_name,
#             last_name=last_name,
#             tel_num = tel_num,
#             email = email,
#             fan = fan
#         )
#         return redirect('home')
    

#     fanlar = Fanlar.objects.all()
#     return render(request= request,template_name='add_stu.html',context={"fanlar":fanlar})




def download_students_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="students.pdf"'

    p = canvas.Canvas(response)
    p.drawString(100, 800, "Studentlar ro'yxati")

    students = Student.objects.all()
    y = 780
    for student in students:
        p.drawString(100, y, f"{student.first_name} {student.last_name} {student.fan} - {student.email}")
        y -= 20

    p.showPage()
    p.save()
    return response


def view_full(request,student_id):
    student_v = get_object_or_404(Student,id=student_id)
    context = {
        "student_v": student_v,

    }
    return render(request=request,template_name='student_v.html',context=context)



def udate_student(request,student_id):
    student = get_object_or_404(Student,id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form  = StudentForm(instance=student)
    return render(request=request,template_name="update_stu.html", context={'form':form})
    








