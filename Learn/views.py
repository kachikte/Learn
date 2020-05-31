from django.shortcuts import render

from .models import Topic

# Create your views here.

def index(request):
	return render(request, 'Learn/index.html')

def topics(request):
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'Learn/topics.html', context)

def topic(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	entry = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entry': entry}
	return render(request, 'Learn/topic.html', context)
