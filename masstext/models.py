from django.db import models
from itertools import chain

class Stake(models.Model):
	creation_date = models.DateTimeField()
	name = models.CharField(max_length=16)
	unit_number = models.IntegerField(default=0)
	def __str__(self):
		return self.name

class Ward(models.Model):
	stake = models.ForeignKey(Stake)
	creation_date = models.DateTimeField()
	name = models.CharField(max_length=16)
	unit_number = models.IntegerField(default=0)
	def __str__(self):
		return self.name
	
class Calling(models.Model):
	creation_date = models.DateTimeField()
	name = models.CharField(max_length=32)
	auto_admin = models.BooleanField(default=False)
	def __str__(self):
		return self.name
	
class Member(models.Model):
	ward = models.ForeignKey(Ward)
	calling = models.ForeignKey(Calling)
	creation_date = models.DateTimeField()
	preferred_first_name = models.CharField(max_length=16)
	given_names = models.CharField(max_length=32)
	last_name = models.CharField(max_length=32)
	cell_phone = models.BigIntegerField()
	verified_number = models.BooleanField(default=False)
	requested_stop = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	password = models.CharField(max_length=32)
	login_code = models.IntegerField()
	login_code_time = models.DateTimeField()
	api_key = models.CharField(max_length=32)
	def __str__(self):
		return self.given_names + " " + self.last_name + " (" + self.preferred_first_name + ")"
	def getPhoneString(self):
		raw = str(self.cell_phone)
		formatted = "(" + raw[:3] + ') ' + raw[3:6] + '-' + raw[6:]
		return formatted

class Group(models.Model):
	name = models.CharField(max_length=32)
	members = models.ManyToManyField(Member)
	
class Thread(models.Model):
	recipient = models.ForeignKey(Member)
	ward = models.ForeignKey(Ward)
	creation_date = models.DateTimeField()
	newest_message_date = models.DateTimeField()
	read = models.BooleanField(default=False)
	starred = models.BooleanField(default=False)
	archived = models.BooleanField(default=False)
	def __str__(self):
		return "Thread with: " + self.recipient.__str__()
	def getMessages(self):
		result_list = list(chain(self.outboundmessage_set.all(), self.inboundmessage_set.all()))
		return result_list
	def updateWard(self):
		ward = recipient.ward

class OutboundMessage(models.Model):
	creation_date = models.DateTimeField()
	thread = models.ForeignKey(Thread)
	author = models.ForeignKey(Member)
	content = models.CharField(max_length=200)
	def __str__(self):
		return "To " + self.thread.recipient.__str__() + ": \"" + self.content + "\""

class InboundMessage(models.Model):
	creation_date = models.DateTimeField()
	thread = models.ForeignKey(Thread)
	content = models.CharField(max_length=200)
	def __str__(self):
		return "From " + self.thread.recipient.__str__() + ": \"" + self.content + "\""