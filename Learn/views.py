from django.shortcuts import render

from .models import Topic, Entry

from .forms import TopicForm, EntryForm

from django.http import HttpResponseRedirect

from django.urls import reverse

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


def add_topic(request):
	if (request.method!='POST'):
		form = TopicForm()

	else:
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('Learn:topics'))

	context = {'form': form}
	return render(request, 'Learn/add_topic.html', context)


def add_entry(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	if (request.method!='POST'):
		form = EntryForm()
	else:
		form = EntryForm(request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('Learn:topic', args=[topic.id]))

	context = {'form': form, 'topic': topic}
	return render(request, 'Learn/add_entry.html', context)


def edit_entry(request, entry_id):
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if (request.method!='POST'):
		form = EntryForm(instance=entry)

	else:
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('Learn:topic', args=[topic.id]))

	context = {'topic': topic, 'entry': entry, 'form': form}
	return render(request, 'Learn/edit_entry.html', context)
