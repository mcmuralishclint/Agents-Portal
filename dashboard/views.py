from django.shortcuts import render, redirect
from dashboard.models import Scholarship, University
from dashboard.forms import ScholarshipEditForm
from django.core.paginator import Paginator
# Create your views here.
def home(request):
	context = {

	}
	return render(request, "dashboard/home.html",context)

def scholarship(request):
	scholarships = Scholarship.objects.all().order_by("-id")
	paginator = Paginator(scholarships, 3) # Show 25 contacts per page
	page = request.GET.get('page')
	schol = paginator.get_page(page)

	context = {
	'scholarships':schol
	}
	return render(request, "dashboard/scholarship.html",context)

def scholarship_view(request,id):
	scholarship = Scholarship.objects.get(id=id)
	university = University.objects.get(university = scholarship.university)
	context={
	'scholarship':scholarship,
	'university' :university
	}
	return render(request, "dashboard/scholarship_view.html",context)

def scholarship_edit(request,id):
	form = ScholarshipEditForm(instance = Scholarship.objects.get(id=id))
	if request.method=="POST":
		form = ScholarshipEditForm(request.POST,  instance = Scholarship.objects.get(id=id))
		if form.is_valid():
			form.save()
			return redirect("/scholarship/")
	context={
	'form':form
	}
	return render(request, "dashboard/scholarship_edit.html",context)





