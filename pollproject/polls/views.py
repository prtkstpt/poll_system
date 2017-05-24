from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import *


def index(request):
    output = "\n"
    candidate_list = Candidate.objects.all()
    student_list = Student.objects.all()
    context = {'student_list': student_list, 'candidate_list': candidate_list}

    return render(request, 'polls/index.html', context)


def detail(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    return render(request, 'polls/detail.html', {'candidate': candidate})


def result(request):
    final_votes = {}
    candidate_list = Candidate.objects.all()
    for candidate in candidate_list:
        final_votes[candidate.student.username] = candidate.vote_count

    final_votes['winner'] = max(final_votes, key=final_votes.get)
    print("======================\n", final_votes)
    return render(request, 'polls/result.html', {'final_votes': final_votes})


def vote(request, candidate_id):
    candidate = Candidate.objects.get(id=candidate_id)
    candidate.vote_count += 1
    candidate.save()

    return HttpResponseRedirect("/")
