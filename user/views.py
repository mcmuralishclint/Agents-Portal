from django.shortcuts import render
from user.models import UserDetail
from dashboard.models import Scholarship
from django.contrib.auth.models import User

# Create your views here.
def profile(request,id):
	details = UserDetail.objects.get(id=id)
	try:
		scholarships = Scholarship.objects.filter(agent = details.user)
	except:
		scholarships=""
	context={
	'details':details,
	'scholarships':scholarships
	}
	return render(request,"user/profile.html",context)

def featured(request):
	try:
		featured = UserDetail.objects.filter(featured=True)
		context={
		'featured':featured
		}
	except:
		context={'featured':None}
		
	return render(request,"user/featured.html",context)

