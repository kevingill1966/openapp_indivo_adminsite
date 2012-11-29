
from django import forms
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from indivo_server.indivo import models as indivo_models

class ImportForm(forms.Form):
    record_id = forms.CharField(max_length=100)
    document = forms.FileField()

# This is a simple form for importing an XML file. It is published via the Admin
# site for testing purposes. 
@staff_member_required
def import_document(request):
    assert request.user.is_superuser, "Super-user permissions required"

    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.files['document'].read()
            record_id = form.data['record_id']
            record = indivo_models.Record.objects.get(id=record_id)

            doc_args = {
                        'pha'         : None,
                        'record'      : record,
                        'creator'     : None,
                        'mime_type'   : None,
                        'external_id' : None,
                        'replaces'    : None,
                        'content'     : document,
                        'original_id' : None,
                    }
            new_doc = indivo_models.Document.objects.create(**doc_args)

    else:
        record_id = request.GET.get('record_id')
        form = ImportForm({'record_id': record_id}) 

    return render(request, 'indivo_server_admin/import_document.html', {'form': form})

