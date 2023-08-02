from django.shortcuts import render

# Create your views here.
	
#Class based views
from Dhanalaxshmi.models import Student

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

class StudentReg(CreateView):
	model = Student
	fields = '__all__'
	template_name = 'Dhana/studentreg.html'
	success_url ="/"

class Studentlist(ListView):
	model = Student
	template_name = 'Dhana/studentlist.html'

class Studentdetail(DetailView):
	model =Student
	template_name = 'Dhana/studentdetail.html'

class StudentUpdate(UpdateView):
	model = Student
	fields = "__all__"
	template_name = 'Dhana/studentupdate.html'
	success_url ="/"


class StudentDelete(DeleteView):
	model = Student
	template_name = 'Dhana/studentdelete.html'
	success_url ="/"
