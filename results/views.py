from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Sum
from .models import AnnouncedPuResults, PollingUnit
from .forms import PollingResultForm, AnnouncedPuResultsForm

# Create your views here.
def polling_unit_result_list(request):
    queryset = AnnouncedPuResults.objects.filter(polling_unit_uniqueid="8").aggregate(Sum('party_score'))['party_score__sum']
    qs = AnnouncedPuResults.objects.order_by('polling_unit_uniqueid').distinct()  
    context = {
        'polling_unit_result': queryset,
        'qs': qs,
    }
    return render(request, 'results/list.html', context)

def polling_unit_result_detail(request, result_id):
    polling_unit_results = get_object_or_404(AnnouncedPuResults, result_id=result_id)
    context = {
        'polling_unit_results': polling_unit_results,
    }
    return render(request, 'results/detail.html', context)


def polling_create(request):
    title = 'Create'
    form = PollingResultForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("results:polling_unit_result_list"))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "results/poll_create.html", context)

def polling_update(request, uniqueid):
    title = 'Update'
    poll = get_object_or_404(PollingUnit, uniqueid=uniqueid)
    form = PollingResultForm(request.POST, instance=poll)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("results:polling_unit_result_list", kwargs={
                'uniqueid': form.instance.uniqueid,
            }))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "results/poll_create.html", context)

def polling_delete(request, uniqueid):
    poll = get_object_or_404(PollingUnit, uniqueid=uniqueid)
    poll.delete()
    return redirect(reverse("results:polling_unit_result_list"))

def add_polling_result(request):
    title = 'Create'
    form = AnnouncedPuResultsForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("results:polling_unit_result_list"))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "results/add_result.html", context)
    
def polling_result_update(request, result_id):
    title = 'Update'
    add_result = get_object_or_404(AnnouncedPuResults, result_id=result_id)
    form = AnnouncedPuResultsForm(request.POST, instance=add_result)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("results:polling_unit_result_list", kwargs={
                'uniqueid': form.instance.result_id,
            }))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "results/add_result.html", context)
    
def result_delete(request, result_id):
    result = get_object_or_404(AnnouncedPuResults, result_id=result_id)
    result.delete()
    return redirect(reverse("results:polling_unit_result_list"))