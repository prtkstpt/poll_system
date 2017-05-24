from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from polls.models import *


def index(request):
    output = "\n"
    candidate_list = Candidate.objects.all()
    context = {'candidate_list': candidate_list}

    return render(request, 'polls/index.html', context)


def detail(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    return render(request, 'polls/detail.html', {'candidate': candidate})


def result(request, candidate_id):
    return HttpResponse("N o t   Y e t   D e c l a r e . . !")


def vote(request, candidate_id):
    return HttpResponse("You are voting on Candidate %s." % candidate_id)
