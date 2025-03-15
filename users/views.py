from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import render,redirect

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
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        tel_num = request.POST.get('tel_num')
        fan_id = request.POST.get('fan')
        email = request.POST.get('email')
        fan = Fanlar.objects.get(id=fan_id)

        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            tel_num = tel_num,
            email = email,
            fan = fan
        )
        return redirect('home')
    

    fanlar = Fanlar.objects.all()
    return render(request= request,template_name='add_stu.html',context={"fanlar":fanlar})




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








