from django import forms
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

from project import weather, weather_info, forecast

class ApiKeyForm(forms.Form):
    """
    form for asking API key
    """
    key = forms.CharField(label = "OpenWeatherMap Api Key", widget = forms.PasswordInput)

class CityForm(forms.Form):
    """
    form for asking requested city
    """
    city = forms.CharField(label = "City Name")

def index(request):
    if "key" not in request.session:
        message = "Please provide the Open Weather API key"
        return HttpResponseRedirect(reverse("information:key") + "?message= " + message)
    if "city" not in request.session:
        request.session["city"] = "North York"
    data = weather_info(request.session["key"], request.session["city"])
    if "key" in request.session and data != None:
        return render(request, "information/index.html", {
            "key": request.session["key"],
            "data": [data]
        })
    else:
        message = "Incorrect API key. Please enter a valid API key."
        return HttpResponseRedirect(reverse("information:key") + "?message= " + message)

def getForecast(request):
    if "city" not in request.session:
        request.session["city"] = "North York"
    data = forecast(request.session["key"], city = request.session["city"])
    if "key" in request.session and data != None:
        return render(request, "information/index.html", {
            "key": request.session["key"],
            "data": data
        })
    else:
        message = "Incorrect API key. Please enter a valid API key."
        return HttpResponseRedirect(reverse("information:getKey") + "?message= " + message)

def getKey(request):
    if request.method == "POST":
        form = ApiKeyForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data["key"]

            request.session["key"] = key

            return HttpResponseRedirect(reverse("information:index"))

        else:
            return render (request, "information/getKey.html", {
                "form": form
            })

    return render(request, "information/getKey.html", {
        "message": request.GET.get('message'),
        "form": ApiKeyForm()
    })

def getCity(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]

            request.session["city"] = city

            return HttpResponseRedirect(reverse("information:index"))

        else:
            return render (request, "information/getCity.html", {
                "form": form
            })

    return render(request, "information/getCity.html", {
        "message": request.GET.get('message'),
        "form": CityForm()
    })

from django.core.mail import send_mail



