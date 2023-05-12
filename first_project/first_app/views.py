from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# 'request' name is convention. It can be some other name too.

from first_app.models import Program, Student

click = 1
def index(request) :
  global click
  click += 1
  my_dict = { 'count' : click,
              'program_rows' : program_values,
              'student_rows' : student_values,}
  return render(request, 'index.html', context=my_dict)

def help(request):
  global click
  click += 1
  my_dict = { 'count' : click}
  return render(request, 'help.html', context=my_dict)

from .forms import StudentForm

def get_student(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
        s_name = form.cleaned_data['name']
        s_roll = form.cleaned_data['roll']
        s_degree = form.cleaned_data['degree']
        s_branch = form.cleaned_data['branch']

        return HttpResponseRedirect('/student/')
  else:
      form =StudentForm()
      return render(request, 'StudentForm.html', {'form': form})


program_values = Program.objects.all()
student_values = Student.objects.all()
