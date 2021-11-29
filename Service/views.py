import datetime
from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views import View
from Service.models import Pay


class Index(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'index.html')


class Sign_in(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('Start_path')
        return render(request, 'Sign_In.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email=username, password=password)
        if user:
            login(request, user)
            return redirect('Start_path')
        else:
            return render(request, 'Sign_In.html', {'error': True})


class Start(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'main.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        bank_account = request.POST['bank_account']
        card_number = request.POST['cardcode']
        validity = request.POST['validity']
        cvc = request.POST['CVC']
        amount_to_pay = request.POST['amount_to_pay']
        date = datetime.datetime.now()
        Pay.objects.get_or_create(bank_account=bank_account, card_number=card_number, validity=validity, cvc=cvc, amount_to_pay=amount_to_pay, date=date)
        return render(request, 'main.html')


class Sign_up(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('Start_path')
        return render(request, 'Sign_Up.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return render(request, 'Sign_Up.html', {'error': 'Passwords not confirmed'})
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('Start_path')


class History_payments(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        items = Pay.objects.all()
        return render(request, 'history payments.html', {'items': items})
