from django.shortcuts import render, HttpResponse


# Create your views here.
from django.shortcuts import render

def home(request):
    
    return render(request, 'home.html')

def college(request):
    return render(request, 'college.html')

def compare(request):
    return render(request, 'compare.html')



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile


@login_required
def profile(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }
    )

    if request.method == "POST":

        profile.first_name = request.POST.get("first_name")
        profile.last_name = request.POST.get("last_name")
        profile.email = request.POST.get("email")
        profile.phone = request.POST.get("phone")
        profile.city = request.POST.get("city")
        profile.state = request.POST.get("state")
        profile.about = request.POST.get("about")

        profile.target_exam = request.POST.get("target_exam")
        profile.expected_rank = request.POST.get("expected_rank") or None
        profile.preferred_stream = request.POST.get("preferred_stream")
        profile.budget = request.POST.get("budget")
        profile.preferred_cities = request.POST.get("preferred_cities")

        profile.save()

        return redirect('profile')

    context = {
        'profile': profile
    }

    return render(request, 'profile.html', context)

def qa(request):
    
    return render(request, 'qa.html')
def search(request):
    
    return render(request, 'search.html')
