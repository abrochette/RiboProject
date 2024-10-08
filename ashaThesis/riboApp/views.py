from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ProcessingInput
from .forms import CreateNewList


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST,
                             response.FILES)
        if form.is_valid():
            adapter = form.cleaned_data["adapter"]
            sampleFile = form.cleaned_data["sampleFile"]
            humanGenome = form.cleaned_data["humanGenome"]
            mouseGenome = form.cleaned_data["mouseGenome"]

            userInput = ProcessingInput.objects.create(
                adapter=adapter,
                sampleFile=sampleFile,
                humanGenome=humanGenome,
                mouseGenome=mouseGenome
            )

            return render(response, "riboApp/create.html",
                          {"form": form, "userInput": userInput})

    else:
        form = CreateNewList()

    return render(response, "riboApp/create.html", {"form": form})
