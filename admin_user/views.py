from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from admin_user.models import Admin, Officer, Case



def home(request):
	return render(request, 'admin-user/index.html')

def login(request):
	if request.user.is_authenticated:
		return redirect('/')
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		try:
			user = authenticate(request, username=username, password=password)
			if user is not None:
				print("login check", user)
				auth_login(request, user)
			else:
				return HttpResponse("No user found")
		except Exception as e:
			print(e)
			return HttpResponse("Error while loggin in the user")
		
		if user.is_staff == True:
			return redirect("/admin-user")
		elif user.is_staff == False:
			return redirect("/officer")
		else:
			return HttpResponse("Not a valid user")

		return HttpResponse("Login success")


	return render(request, 'login.html')


def create(request):
	if request.method=='POST':
		name = request.POST['name']
		password = request.POST['password']
		phone_number = request.POST['phone_number']
		mail = request.POST['mail']
		image = request.FILES['image']
		department = request.POST['department']
		rank_of_officer = request.POST['rank_of_officer']
		location = request.POST['location']
		admin_id = request.user.id

		try:
			user = User.objects.get(username=name)			
			return HttpResponse("Error while inserting into DB")
		except User.DoesNotExist:
			pass

		user = User.objects.create_user(name, mail, password, is_staff=False)		
		officerObj = Officer()
		officerObj.id = user.id
		officerObj.name = name
		officerObj.image = image
		officerObj.phone_number = phone_number
		officerObj.mail = mail
		officerObj.department = department
		officerObj.rank_of_officer = rank_of_officer
		officerObj.location = location
		#print(admin_id, request.user.id, user.id)
		officerObj.created_by = request.user
		officerObj.user = user
		try:
			officerObj.save()
		except Exception as e:
			print(e)
			user.delete()
			return HttpResponse("Error while creating admin")
		return HttpResponse("Admin user added successfully")
	return render(request, 'admin-user/create.html')



def retrieve(request):
	if request.method=="POST":
		id = request.POST['id']
		officerObj = Officer.objects.get(officer_id=id)
		return render(request, 'admin-user/retrieve-view.html' ,{'off':officerObj})	
		
	return render(request, 'admin-user/retrieve.html')


def addCase(request):
	if request.method=='POST':
		caseObj = Case()
		caseObj.case_id = request.POST['case_id']
		caseObj.case_name = request.POST['case_name']
		caseObj.case_type = request.POST['case_type']
		caseObj.notes = request.POST['notes']
		caseObj.description = request.POST['description']
		caseObj.type_of_weapon = request.POST['type_of_weapon']
		caseObj.time = request.POST['time']
		caseObj.date = request.POST['date']
		off = Officer.objects.get(officer_id=request.POST['officer_id'])
		caseObj.officer_id = off.officer_id
		#return HttpResponse(request.user.username)
		adm = Admin.objects.get(admin_id=request.user.id)

		caseObj.created_by = adm
		caseObj.status = "pending"
		try:
			caseObj.save()
			return HttpResponse("Case created")
		except Exception as e:
			return HttpResponse(e)
			return HttpResponse("Error! Try again with correct details")
	return render(request, 'admin-user/addCase.html')



def logout(request):
	auth_logout(request)
	return redirect('/')

