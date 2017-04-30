import os
from PIL import Image
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from huxianghui.settings.mybook import MEDIA_ROOT


@require_GET
def get_asstes(request,file_path):
    path = os.path.join(MEDIA_ROOT, file_path)
    img = Image.open(path)
    response = HttpResponse(content_type='image/jpeg')
    img.convert('RGB').save(response, 'jpeg')
    return response

