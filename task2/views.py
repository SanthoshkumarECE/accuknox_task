import threading
from django.http import HttpResponse
from .models import ThreadModel

def check_thread_view(request):
    print(f"Main thread ID: {threading.get_ident()}")
    ThreadModel.objects.create(name="Thread check")
    return HttpResponse("Done")
