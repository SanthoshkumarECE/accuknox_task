import time
from django.http import HttpResponse
from .models import SimpleModel

def create_data(request):
    start = time.time()
    SimpleModel.objects.create(title="Hello")
    end = time.time()
    return HttpResponse(f"Time taken: {end - start:.2f} seconds")
