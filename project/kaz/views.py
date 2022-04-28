from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import Registration
from .models import *


# Create your views here.

def home(request):
    return render(request, 'kaz/home.html', {'name': 'Kaz', 'kaz': home})


def tours(request):
    tours = Tour.objects.all()
    return render(request, 'kaz/tours.html', {'name': 'Tours', 'tours': tours})


def tourists(request):
    tourists = Tourists.objects.all()
    return render(request, 'kaz/tourists.html', {'name': 'Tourists', 'tourists': tourists})


def info(request):
    info = Info.objects.all()
    return render(request, 'kaz/info.html', {'name': 'Info', 'info': info})


def reg(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kaz:tourists')
    else:
        form = Registration()
    return render(request, 'kaz/reg.html', {'form': form, 'name': 'Reg', 'reg': reg})


def update_tour(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Tourists.objects.get(id=post_id)
    except Tourists.DoesNotExist:
        return redirect('kaz:registration')
    post_form = Registration(request.POST or None, instance=post_sel)
    if post_form.is_valid():
        post_form.save()
        return redirect('kaz:tourists')
    return render(request, 'kaz/reg.html', {'reg': post_form})


def delete_tour(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Tourists.objects.get(id=post_id)
    except Tourists.DoesNotExist:
        return redirect('kaz:tourists')
    post_sel.delete()
    return redirect('kaz:tourists')


def show_post(request, post_slug):
    post = get_object_or_404(Posts, slug=post_slug)
    context = {'post': post}
    return render(request, 'kaz/post.html', context=context)


def cat(request):
    return render(request, 'kaz/cat.html')


def list_cat(request):
    return render(request, 'kaz/list_cat.html')


def send_message(request):
    send_mail("Web prog:backend", "My content",
              "200103370@stu.sdu.edu.kz",
              ["200103370@stu.sdu.edu.kz", "nurikakhm@gmail.com"],
              fail_silently=False, html_message="<b>Если ты это читаешь то у тебя получилось</b><i>   Keep going!</i>")
    return render(request, 'kaz/success.html')






