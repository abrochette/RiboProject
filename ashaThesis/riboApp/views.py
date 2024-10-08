from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import ProcessingInput
from .forms import CreateNewList
import mimetypes
import os

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST, response.FILES)
        if form.is_valid():
            experimentName = form.cleaned_data["experimentName"]
            adapter = form.cleaned_data["adapter"]
            sampleFile = form.cleaned_data["sampleFile"]
            humanGenome = form.cleaned_data["humanGenome"]
            mouseGenome = form.cleaned_data["mouseGenome"]

            ProcessingInput.objects.create(
                experimentName=experimentName,
                adapter=adapter,
                sampleFile=sampleFile,
                humanGenome=humanGenome,
                mouseGenome=mouseGenome
            )

            return HttpResponseRedirect('/create/')
    else:
        form = CreateNewList()

    all_inputs = ProcessingInput.objects.all()

    return render(response, "riboApp/create.html", {"form": form, "all_inputs": all_inputs})

def download_file(response, file_name):
    file_path = os.path.join('media/uploads', file_name)

    if not os.path.exists(file_path):
        raise Http404("File not found")

    mime_type, _ = mimetypes.guess_type(file_path)
    with open(file_path, 'rb') as f:
        response = HttpResponse(f, content_type=mime_type or 'application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename={file_name}'
        return response
