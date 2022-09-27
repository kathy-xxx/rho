from django.shortcuts import render
from .models import Dji, DjiChart,Ixic,Ndx
from django.http import JsonResponse

# Create your views here.
def home(request):
  return render(request, "visualization/home.html")

def sample_view(request):
    return render(request,'visualization/sample.html')

def sample2_view(request):
    return render(request,'visualization/sample2.html')

def sample3_view(request):
    return render(request,'visualization/sample3.html')

def dji_view(request):
    return render(request,'visualization/dji.html')

#返回dji
def get_dji_data(request):
    dji_time = DjiChart.objects.values_list('time',flat=True)
    dji_close = DjiChart.objects.values_list('close',flat=True)
    dji_clmov = DjiChart.objects.values_list('clmov',flat=True)
    dji_bsmov = DjiChart.objects.values_list('bsmov',flat=True)
    dji_rho_sigma = DjiChart.objects.values_list('rho_sigma',flat=True)
    dji_s_mov = DjiChart.objects.values_list('s_mov',flat=True)
    dji_rho_trend = DjiChart.objects.values_list('rho_trend',flat=True)
    dji_rho_trend2 = DjiChart.objects.values_list('rho_trend2',flat=True)
    dji_month = DjiChart.objects.values_list('month',flat=True)
    dji_day = DjiChart.objects.values_list('day',flat=True)
    dji_bsadf_mi = DjiChart.objects.values_list('bsadf_mi',flat=True)
    dji_rho_45 = DjiChart.objects.values_list('rho_45',flat=True)
    jsondata = {
        "time": list(dji_time),
        "close": list(dji_close),
        "clmov": list(dji_clmov),
        'bsmov': list(dji_bsmov),
        'rho_sigma': list(dji_rho_sigma),
        's_mov': list(dji_s_mov),
        'rho_trend': list(dji_rho_trend),
        'rho_trend2': list(dji_rho_trend2),
        'month': list(dji_month),
        'day': list(dji_day),
        "bsadf_mi": list(dji_bsadf_mi),
        "rho_45": list(dji_rho_45),
    }
    return JsonResponse(jsondata)



#以下为测试
def get_test(request):
    jsondata = {
        "x": [1, 2, 3],
        "y": [4, 5, 6]
    }
    return JsonResponse(jsondata)


