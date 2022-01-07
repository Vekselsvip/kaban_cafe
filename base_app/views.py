from django.shortcuts import render, redirect
from .models import Home, Service, Dish, CategoryDish, About, Chef, Feedback
from.forms import BookTableForm


def base_app_views(request):
    error = ''
    if request.method == 'POST':
        form = BookTableForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'форма не верна!'
    form = BookTableForm()
    home = Home.objects.all()
    service = Service.objects.all()
    about = About.objects.all()
    category = CategoryDish.objects.all().order_by('position')
    dish = Dish.objects.filter(is_visible=True).order_by('category_id')
    chef = Chef.objects.all()
    feedback = Feedback.objects.all()
    return render(request, 'base_app.html', context={
        'home': home,
        'service': service,
        'about': about,
        'dish': dish,
        'category': category,
        'form': form,
        'error': error,
        'chef': chef,
        'feedback': feedback,
    })


def contact_views(request):
    return render(request, 'contact.html', context={})