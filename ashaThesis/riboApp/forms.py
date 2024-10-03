from django import forms

class CreateNewList(forms.Form):
    adapter_sequence = forms.CharField(label="Input adapter sequence to be trimmed", max_length=300, required=False)

    GRCm39 = forms.BooleanField(label="GRCm39", required=False)
    GRCh38 = forms.BooleanField(label="GRCh38", required=False)

    sample_data_file = forms.FileField(label="Upload text file containing sample data paths", required=False)

    def as_p(self):
        return super().as_p() + '''
            <h3>Choose Organism</h3>
            <label for="id_GRCm39">GRCm39</label> {}<br>
            <label for="id_GRCh38">GRCh38</label> {}<br>
            <label for="id_sample_data_file">Upload text file containing sample data paths</label> {}
        '''.format(self['GRCm39'], self['GRCh38'], self['sample_data_file'])
