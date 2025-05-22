from django.shortcuts import render, get_object_or_404, redirect
from .models import Feedback, Faculty, University
from django.core.paginator import Paginator
from .forms import FeedbackSubmission

def main_land(request):
    page = request.GET.get('page', 1)
    feedbacks = Feedback.objects.all()
    paginator = Paginator(feedbacks, 5)
    currentpage = paginator.page(int(page))
    return render(request, 'main/index.html', {'feedbacks': feedbacks,
                                               'paginator': currentpage,})


def selection(request):
    faculty = Faculty.objects.all()
    return render(request, 'main/select.html', {'faculty': faculty})



def selected(request, slug):
    video_url = Faculty.objects.filter(slug=slug).first()
    if request.method == "POST":
        form = FeedbackSubmission(request.POST, request.FILES)
        print("Form valid?", form.is_valid())
        if form.is_valid():
            print("POST data:", request.POST)
            print("FILES data:", request.FILES)
            form.save()
            return render('main/added.html')
    else:
        form = FeedbackSubmission()
    return render(request, 'main/selected.html', {'video': video_url,
                                                  'form': form})


def select_uni(request):
    uni = University.objects.all()
    return render(request, 'main/select_uni.html', {'uni': uni})