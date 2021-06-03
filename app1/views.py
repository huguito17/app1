from django.shortcuts import render
from django.http import HttpResponse

vista = [
    {
        'monto': '100000',
        'tasa': '18',
        'plazo': '120',
        'cuota': '1801',
        'total': '216222',
    },
    
]

def index(request):
    if request.method == 'POST':
        monto = int(request.POST.get('monto'))
        tasa = int(request.POST.get('tasa'))
        plazo = int(request.POST.get('plazo'))

        tasaD = tasa / 100 / 12
        plazo = plazo * 12
        cuota = (monto * tasaD) / ( 1- (1 + tasaD) ** -plazo)
        total = cuota * plazo

        vista.append({
            'monto': monto,
            'tasa': tasa,
            'plazo': plazo,
            'cuota': cuota,
            'total': total
        })
        ctx = {
            'vista': vista
        }
        return render(request, 'app1/index.html', ctx)
    else:
        
        ctx = {
            'vista': vista 
        }
        return render(request, 'app1/index.html', ctx)
