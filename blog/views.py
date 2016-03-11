from django.shortcuts import render
from django.utils import timezone
from .models import Wpis

def wpis_list(request):
    wpisy = Wpis.objects.filter(data_publikacji__lte=timezone.now()).order_by('data_publikacji')
    return render(request, 'blog/wpis_list.html', {'wpisy': wpisy})
