from django.shortcuts import render, HttpResponse
from admin_user.models import Case, Suspect


def home(request):
	return render(request, 'officer/index.html')

def viewAllCases(request):
	if request.method=='POST':
		status = request.POST['status']
	try:
		print(status)
	except:
		status = "pending"
	if request.user.is_authenticated:
		casesObj = Case.objects.filter(officer=request.user.id, status=status)
		#return HttpResponse(casesObj)
		return render(request, 'Officer/viewAllCases.html', {'casesObj':casesObj})
	else:
		return HttpResponse("You need to be authenticated as admin-user")

def addSuspect(request):
	if request.method=="POST":
		try:
			susObj = Suspect()
			susObj.suspect_id = request.POST['id']
			susObj.name = request.POST['name']
			susObj.image = request.FILES['image']
			susObj.phone_number = request.POST['phone_number']
			susObj.age = request.POST['age']
			susObj.gender = request.POST['gender']
			susObj.relation = request.POST['relation']
			susObj.description = request.POST['description']
			susObj.weight = request.POST['weight']
			caseObj = Case.objects.get(case_id=request.POST['case_id'])
			susObj.case = caseObj
			susObj.save()
			return HttpResponse("Suspect added!")
		except:
			return HttpResponse("Error!!!")

	return render(request, "officer/addSuspect.html")

def detailCaseView(request, slug):
	if request.user.is_authenticated:
		caseObj = Case.objects.get(case_id=slug)
		return render(request, 'detailCaseView.html', {'caseObj':caseObj})
		

