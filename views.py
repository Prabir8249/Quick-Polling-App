# polls/views.py
from django.core.paginator import Paginator
from .models import Poll

def poll_list(request):
    polls = Poll.objects.all()
    paginator = Paginator(polls, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'polls/poll_list.html', {'page_obj': page_obj})
