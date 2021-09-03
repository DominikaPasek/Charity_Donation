from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.views import View
from .forms import RegistrationForm

# Create your views here.


class LandingPage(View):
    def get(self, request):
        return render(request, "index.html")


class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")


class Login(View):
    def get(self, request):
        return render(request, "login.html")


class Register(View):
    def get(self, request):
        form = RegistrationForm()
        form.fields['first_name'].widget.attrs.update({
            'placeholder': 'Imię'})
        form.fields['last_name'].widget.attrs.update({
            'placeholder': 'Nazwisko'})
        form.fields['username'].widget.attrs.update({
            'placeholder': 'Email'})
        form.fields['password1'].widget.attrs.update({
            'placeholder': 'Hasło'})
        form.fields['password2'].widget.attrs.update({
            'placeholder': 'Powtórz hasło'})

        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
                user = form.save()
                user.refresh_from_db()
                user.save()

                # redirect user to login page
                return redirect('/login')
        else:
            try:
                username = form.cleaned_data['username']
                User.objects.get(username=username)
            except User.DoesNotExist:
                # raise ValidationError(u'Email "%s" już istnieje w bazie.' % username)
                messages.info(request, "Podany email jest już zarejestrowany w bazie")
                return redirect("/register")

            # raw_password = form.cleaned_data.get('password1')
            # # login user after signing up
            # user = authenticate(username=user.username, password=raw_password)
            # login(request, user)
