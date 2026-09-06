from django.shortcuts import render
import pyshorteners
from django.contrib import messages


def index(request):

    short_url = ""
    url = ""

    if request.method == "POST":

        url = request.POST.get("url")

        print("URL RECEIVED:", url)

        s = pyshorteners.Shortener()

        short_url = s.tinyurl.short(url)

        messages.success(request, "URL Shortened Successfully")

    context = {
        "short_url": short_url,
        "url": url
    }

    return render(request, "index.html", context)