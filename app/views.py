from django.shortcuts import render
from .classes.cards import cards_list
from .classes.devs import dev_list
from .classes.tencologias import lista_tecnologia
import subprocess



def index(request):
    return render(request, 'index.html', {'cards': cards_list})

def lh_simulator(request):
    if request.method == 'POST':
        subprocess.Popen(['python', 'app/services/pygame-lh-simulator.py'])
    return render(request, 'simulators/lh.html')


def lo_simulator(request):
    if request.method == 'POST':
        subprocess.Popen(['python', 'app/services/pygame-lo-simulator.py'])
    return render(request, 'simulators/lo.html')


def calculator(request):
    return render(request, 'services/calculator.html')

def coders(request):
    return render(request, 'coders.html', {'devs': dev_list , 'tecnologias': lista_tecnologia})
