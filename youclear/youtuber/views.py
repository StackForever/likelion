from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from .models import *
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User

def index(request):
    youtubers = Youtuber.objects.all()
    youtuber_lists = YoutuberList.objects.all()[0:2]

    context = {
        'youtubers': youtubers, 
        'youtuber_lists': youtuber_lists,
    }
    
    return render(request, 'youtuber/index.html', context)

@login_required
def youtuber(request, youtuber_id):
    try: 
        my_youtuber = MyYoutuber.objects.get(user=request.user.id, youtuber=youtuber_id, activated=True)
    except ObjectDoesNotExist:
        my_youtuber = None

    try:
        youtuber = Youtuber.objects.get(pk=youtuber_id)
        videos = Video.objects.filter(youtuber_name=youtuber_id)
        context = {'youtuber': youtuber, 'videos': videos}
    except Youtuber.DoesNotExist:
        raise Http404('유투버명을 확인해 주세요!')

    context['my_youtuber'] = my_youtuber is None

    return render(request, 'youtuber/youtuber.html', context)

@login_required
def my_youtuber(request, user_id):
    my_youtubers = MyYoutuber.objects.filter(user=user_id, activated=True).order_by('-listed_date')
    context = {'my_youtuber': my_youtubers}
        
    return render(request, 'youtuber/my_youtuber.html', context)

@login_required
def add_my_youtuber(request, youtuber_id):
        
    my_youtuber, created = MyYoutuber.objects.get_or_create(
        user= User.objects.get(pk=request.user.id),
        youtuber= Youtuber.objects.get(pk=youtuber_id),
    )
    if not created:
        my_youtuber.activated = True
        my_youtuber.listed_date = timezone.now()
        my_youtuber.save()

    return redirect('youtuber:youtuber', youtuber_id)

@login_required
def remove_my_youtuber(request, youtuber_id):
    my_youtuber = MyYoutuber.objects.get(user=request.user.id, youtuber=youtuber_id)
    my_youtuber.activated = False
    my_youtuber.save()

    return redirect('youtuber:youtuber', youtuber_id)

@login_required
def edit_my_youtuber(request, user_id):
    my_youtubers = MyYoutuber.objects.filter(user=user_id, activated=True).order_by('-listed_date')
    context = {'my_youtuber': my_youtubers}

    return render(request, 'youtuber/edit_my_youtuber.html', context)

@login_required
def delete_my_youtuber(request, youtuber_id):
    my_youtuber = MyYoutuber.objects.get(user=request.user.id, youtuber=youtuber_id)
    my_youtuber.activated = False
    my_youtuber.save()

    return redirect('youtuber:edit_my_youtuber', request.user.id)

@login_required
def my_list(request, user_id):
    context={}

    return render('youtuber/my_list.html', context)
