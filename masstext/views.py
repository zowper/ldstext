import json

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt

from itertools import chain

from masstext.models import Thread
from masstext.models import Member


def index(request):
	thread_list = Thread.objects.order_by('-newest_message_date')
	context = {'thread_list': thread_list}
	return render(request, 'masstext/index.html', context)

def getUser(request, apiKey):
	user = Member.objects.get(api_key=apiKey)
	data = serializers.serialize("json", Member.objects.filter(pk=user.id))
	return HttpResponse(data, content_type='application/json')
	
def getWardThreads(apiKey):
	user = Member.objects.get(api_key=apiKey)
	threads = Thread.objects.filter(ward=user.ward)
	return threads
	
def getMembers(request, apiKey):
	user = Member.objects.get(api_key=apiKey)
	members = Member.objects.filter(ward=user.ward)
	data = serializers.serialize("json", members)
	return HttpResponse(data, content_type='application/json')

def getArchived(request, apiKey):
	threads = getWardThreads(apiKey).filter(archived=True)
	data = serializers.serialize("json", threads)
	return HttpResponse(data, content_type='application/json')
	
def getUnarchived(request, apiKey):
	threads = getWardThreads(apiKey).filter(archived=False)
	data = serializers.serialize("json", threads)
	return HttpResponse(data, content_type='application/json')
	
def getRead(request, apiKey):
	threads = getWardThreads(apiKey).filter(read=True)
	data = serializers.serialize("json", threads)
	return HttpResponse(data, content_type='application/json')
	
def getUnread(request, apiKey):
	threads = getWardThreads(apiKey).filter(read=False)
	data = serializers.serialize("json", threads)
	return HttpResponse(data, content_type='application/json')
	
def getStarred(request, apiKey):
	threads = getWardThreads(apiKey).filter(starred=True)
	data = serializers.serialize("json", threads)
	return HttpResponse(data, content_type='application/json')
	
def getUnstarred(request, apiKey):
	threads = getWardThreads(apiKey).filter(starred=False)
	data = serializers.serialize("json", threads)
	return HttpResponse(data, content_type='application/json')
	
def getMessages(request, apiKey, threadId):
	outboundMessages = Thread.objects.get(pk=threadId).outboundmessage_set.all()
	inboundMessages = Thread.objects.get(pk=threadId).inboundmessage_set.all()
	allMessages = list(chain(outboundMessages, inboundMessages))
	data = serializers.serialize("json", allMessages)
	return HttpResponse(data, content_type='application/json')


@csrf_exempt
def sendMessage(request, apiKey, memberId, message):
	member = get_object_or_404(Member, pk=memberId)
	member.cell_phone = 8019999999
	member.save()
	return HttpResponse("Done", content_type='text/html')

def vote(request, thread_id):
	p = get_object_or_404(Thread, pk=thread_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the thread voting form.
		return render(request, 'masstext/detail.html', {
			'thread': p,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('masstext:results', args=(p.id,)))