from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Тіркеу view
def Объявление(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # тіркелген соң логин бетіне
    else:
        form = UserCreationForm()
    return render(request, 'main_templates/signup.html', {'form': form})

# Тек кірген қолданушы көре алатын бет
@login_required
def spisok_obyavleniy(request):
    return render(request, 'main_templates/spisok.html')