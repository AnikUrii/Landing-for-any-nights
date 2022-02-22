from multiprocessing import context
from django.shortcuts import redirect, render

from .models import Hero, Works, OurAvesome, DescriptionOur, WhoAreWe, OurProc, OurTeam, Button, Feedback,CompanyData
from .forms import contactForm
# Create your views here.
def index(request):
    feedback = Feedback.objects.filter(is_active=True)[:6]
    buttons_d = Button.objects.filter(is_active=True)[:1]
    who_are_we = WhoAreWe.objects.all()[:1]
    ourproc = OurProc.objects.all()[:4]
    awesome = OurAvesome.objects.all()[:1]
    descriptionOur = DescriptionOur.objects.filter(is_active=True)[:6]
    hero_sliders_text= Hero.objects.filter(is_active=True)[:3]
    works_portfolio= Works.objects.filter(is_active=True)[:8]
    our_team = OurTeam.objects.filter(is_active=True)[:4]
    num = CompanyData.objects.get(num=1)
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = contactForm()
    context = {'hero_sliders_text': hero_sliders_text, 'works':works_portfolio,'awesome': awesome, 'descriptionOur':descriptionOur,
        'who':who_are_we, 'ourproc':ourproc, 'our_team': our_team, 'button':buttons_d, 'feedback':feedback, 'form':form, 'num':num}
    return render(request, 'index.html', context)