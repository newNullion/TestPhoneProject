from django.shortcuts import render, redirect
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.views import View



class MainView(View):
    template_name = 'main.html'

    def get(self, request):
        return render(request=request, template_name=self.template_name, context={})



class RegView(View):
    template_name = 'registration/reg.html'

    def get(self, request):
        context = {
            'form': CustomUserCreationForm()
        }
        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=phone, password=password)
            login(request, user)

            return redirect('main')















