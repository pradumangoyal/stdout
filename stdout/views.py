import os
import subprocess
from urllib.parse import unquote

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        if 'stdout' in request.path:
            subprocess.run(["lpr", unquote(settings.BASE_DIR+uploaded_file_url)])
        return render(request, 'stdout.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'stdout.html')
