
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Student
from .forms import StudentForm 
import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class UserLoginView(LoginView):
    template_name = 'results/login.html'

    def get_success_url(self):
        return reverse_lazy('home')
    
                                   # ✅ Correct import
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'results/student_list.html', {'students': students})

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()

    return render(request, 'results/add_student.html', {'form': form})

@login_required
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'results/add_student.html', {'form': form})

@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')

@login_required
def student_chart(request):
    students = Student.objects.all()

    names = [s.name for s in students]
    totals = [s.total() for s in students]

    plt.figure(figsize=(8, 5))
    plt.bar(names, totals)
    plt.title("Student Total Marks")
    plt.xlabel("Students")
    plt.ylabel("Total Marks")

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')
    buffer.close()
    plt.close()

    return render(request, 'results/chart.html', {"graph": graph})

@login_required
def pass_fail_chart(request):
    students = Student.objects.all()

    pass_count = 0
    fail_count = 0

    for s in students:
        if s.subject1 >= 35 and s.subject2 >= 35 and s.subject3 >= 35:
            pass_count += 1
        else:
            fail_count += 1

    labels = ['Pass', 'Fail']
    sizes = [pass_count, fail_count]

    plt.figure(figsize=(4,4))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Student Pass vs Fail")

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    image_png = buffer.getvalue()
    buffer.close()

    graph = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'results/pie_chart.html', {'graph': graph})