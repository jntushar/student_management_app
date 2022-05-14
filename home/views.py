from django.shortcuts import render, redirect, HttpResponse
from home.models import Contact, Student
from datetime import datetime


def index(request):
    students = Student.objects.all()
    return render(request, "index.html", {'students': students})


def add_student(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        email = request.POST['email']
        school_name = request.POST['school_name']
        book = request.POST['book']
        book_pages = request.POST['book_pages']
        student = Student(first_name=first_name, last_name=last_name, email=email, gender=gender,
                          school_name=school_name, book=book, book_pages=book_pages)
        student.save()
        return redirect('add_student')
    else:
        return render(request, "student.html")


def student_info(request, stu_id):
    student_details = Student.objects.filter(id=stu_id)
    return render(request, "search.html", {'students': student_details})


def search(request):
    if request.method == 'POST':
        searched = request.POST['search'].strip()
        results = Student.objects.filter(id=searched) if searched.isnumeric() else \
            Student.objects.filter(first_name__iregex=rf'.*{searched}.*')
        if results.count() == 0 or len(searched) == 0:
            return HttpResponse('<b>404: Not Found</b>')
        return render(request, 'search.html', {'students': results})


def contactus(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        date = datetime.now()
        contact = Contact(name=name, email=email, message=message, date=date)
        contact.save()
        return redirect('contactus')
    else:
        return render(request, 'contactus.html')
