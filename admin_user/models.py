from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
	admin_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	image = models.ImageField(upload_to="images/admin/", blank=True)
	phone_number = models.CharField(max_length=12)
	mail = models.EmailField(max_length=50)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return str(self.name)


class Officer(models.Model):
	officer_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=40)
	image = models.ImageField(upload_to="images/officer/")
	department = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=12)
	mail = models.EmailField(max_length=50)
	rank_of_officer = models.CharField(max_length=30)
	location = models.CharField(max_length=20)
	created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="admin_officers")
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_officer")

	def __str__(self):
		return str(self.name)

class Case(models.Model):
	case_id = models.IntegerField(primary_key=True)
	case_name = models.CharField(max_length=50)
	case_type = models.CharField(max_length=50)
	notes = models.CharField(max_length=500)
	description = models.CharField(max_length=500)
	type_of_weapon = models.CharField(max_length=255, blank=True)
	time = models.TimeField()
	date = models.DateField()
	status = models.CharField(blank=True, max_length=255, default="pending")
	officer = models.ForeignKey(Officer, on_delete=models.DO_NOTHING, related_name="officers")
	status = models.CharField(max_length=255, default="pending")
	created_by = models.ForeignKey(Admin, on_delete=models.DO_NOTHING, related_name="admin", blank=True, default=None)

	def __str__(self):
		return self.case_name

class Suspect(models.Model):
	suspect_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to="images/suspects")
	phone_number = models.CharField(max_length=12)
	age = models.IntegerField()
	gender = models.CharField(max_length=40)
	relation = models.CharField(max_length=255)
	description = models.CharField(max_length=500)
	weight = models.IntegerField(blank=True, null=True)
	case = models.ForeignKey(Case, on_delete=models.DO_NOTHING)


class Criminal_Record(models.Model):
	criminal_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=255)
	image = models.ImageField(upload_to="images/criminal_record")
	phone_number = models.CharField(max_length=12)
	age = models.IntegerField()
	gender = models.CharField(max_length=10)
	relation = models.CharField(max_length=255)
	description = models.CharField(max_length=500)
	suspect = models.ForeignKey(Suspect, on_delete=models.DO_NOTHING)
	case = models.ForeignKey(Case, on_delete=models.DO_NOTHING)

