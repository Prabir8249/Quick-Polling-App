 polls/views.py
from django.core.paginator import Paginator
from .models import Poll

def poll_list(request):
    polls = Poll.objects.all()
    paginator = Paginator(polls, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'polls/poll_list.html', {'page_obj': page_obj})



Poll Participation


 polls/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Poll, Choice

@login_required
def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.method == 'POST':
        chosen_choice = request.POST.get('choice')
        if chosen_choice:
            choice = poll.choices.get(pk=chosen_choice)
            choice.votes += 1
            choice.save()
            return redirect('poll_result', poll_id=poll.id)
    return render(request, 'polls/poll_detail.html', {'poll': poll})

@login_required
def ajax_vote(request, poll_id):
    if request.method == 'POST':
        poll = get_object_or_404(Poll, pk=poll_id)
        chosen_choice_id = request.POST.get('choice')
        if chosen_choice_id:
            chosen_choice = poll.choices.get(pk=chosen_choice_id)
            chosen_choice.votes += 1
            chosen_choice.save()
            total_votes = sum(choice.votes for choice in poll.choices.all())
            return JsonResponse({'success': True, 'votes': chosen_choice.votes, 'total_votes': total_votes})
    return JsonResponse({'success': False})

Result Display

polls/views.py
from django.shortcuts import render, get_object_or_404

def poll_result(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    total_votes = sum(choice.votes for choice in poll.choices.all())
    return render(request, 'polls/poll_result.html', {'poll': poll, 'total_votes': total_votes})


Functionality for voting and poll creation


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Poll, Choice
from .forms import PollForm, ChoiceForm

@login_required
def create_poll(request):
    if request.method == 'POST':
        poll_form = PollForm(request.POST)
        choice_forms = [ChoiceForm(request.POST, prefix=f'choice{i}') for i in range(3)]
        if poll_form.is_valid() and all(cf.is_valid() for cf in choice_forms):
            poll = poll_form.save(commit=False)
            poll.created_by = request.user
            poll.save()
            for cf in choice_forms:
                choice = cf.save(commit=False)
                choice.poll = poll
                choice.save()
            return redirect('poll_list')
    else:
        poll_form = PollForm()
        choice_forms = [ChoiceForm(prefix=f'choice{i}') for i in range(3)]
    return render(request, 'polls/create_poll.html', {'poll_form': poll_form, 'choice_forms': choice_forms})

@login_required
def ajax_create_poll(request):
    if request.method == 'POST':
        poll_form = PollForm(request.POST)
        choice_forms = [ChoiceForm(request.POST, prefix=f'choice{i}') for i in range(3)]
        if poll_form.is_valid() and all(cf.is_valid() for cf in choice_forms):
            poll = poll_form.save(commit=False)
            poll.created_by = request.user
            poll.save()
            for cf in choice_forms:
                choice = cf.save(commit=False)
                choice.poll = poll
                choice.save()
            return JsonResponse({'success': True, 'poll_id': poll.id})
        else:
            return JsonResponse({'success': False, 'errors': poll_form.errors})
    return JsonResponse({'success': False})

def poll_list(request):
    polls = Poll.objects.all()
    paginator = Paginator(polls, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'polls/poll_list.html', {'page_obj': page_obj})

@login_required
def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.method == 'POST':
        chosen_choice = request.POST.get('choice')
        if chosen_choice:
            choice = poll.choices.get(pk=chosen_choice)
            choice.votes += 1
            choice.save()
            return redirect('poll_result', poll_id=poll.id)
    return render(request, 'polls/poll_detail.html', {'poll': poll})

@login_required
def ajax_vote(request, poll_id):
    if request.method == 'POST':
        poll = get_object_or_404(Poll, pk=poll_id)
        chosen_choice_id = request.POST.get('choice')
        if chosen_choice_id:
            chosen_choice = poll.choices.get(pk=chosen_choice_id)
            chosen_choice.votes += 1
            chosen_choice.save()
            total_votes = sum(choice.votes for choice in poll.choices.all())
            return JsonResponse({'success': True, 'votes': chosen_choice.votes, 'total_votes': total_votes})
    return JsonResponse({'success': False})

def poll_result(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    total_votes = sum(choice.votes for choice in poll.choices.all())
    return render(request, 'polls/poll_result.html', {'poll': poll, 'total_votes': total_votes})

