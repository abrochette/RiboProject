from django import forms

class CreateNewList(forms.Form):
    adapter = forms.CharField(label="Input adapter sequence to be trimmed", max_length=300, required=False)
    mouseGenome = forms.BooleanField(label="GRCm39", required=False)
    humanGenome = forms.BooleanField(label="GRCh38", required=False)
    sampleFile = forms.FileField(label="Upload text file containing sample data paths", required=False)
