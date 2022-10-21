from django.shortcuts import render
from .models import Dji, DjiChart,Ixic,Ndx,IxicChart,NdxChart,NdxFutureChart,NdxFutureChart3
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

def ixic_view(request):
    return render(request,'visualization/ixic.html')

def ndx_view(request):
    return render(request,'visualization/ndx.html')

def ndx_future_view(request):
    return render(request,'visualization/ndx-future.html')

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
    dji_day_points = DjiChart.objects.values_list('day_points', flat=True)
    dji_mid_points = DjiChart.objects.values_list('mid_points', flat=True)
    dji_down1 = DjiChart.objects.values_list('down1', flat=True)
    dji_up1 = DjiChart.objects.values_list('up1', flat=True)
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
        "day_points": list(dji_day_points),
        "mid_points": list(dji_mid_points),
        "down1": list(dji_down1),
        "up1": list(dji_up1),
    }
    return JsonResponse(jsondata)

#返回ixic
def get_ixic_data(request):
    ixic_time = IxicChart.objects.values_list('time',flat=True)
    ixic_close = IxicChart.objects.values_list('close',flat=True)
    ixic_clmov = IxicChart.objects.values_list('clmov',flat=True)
    ixic_bsmov = IxicChart.objects.values_list('bsmov',flat=True)
    ixic_rho_sigma = IxicChart.objects.values_list('rho_sigma',flat=True)
    ixic_s_mov = IxicChart.objects.values_list('s_mov',flat=True)
    ixic_rho_trend = IxicChart.objects.values_list('rho_trend',flat=True)
    ixic_rho_trend2 = IxicChart.objects.values_list('rho_trend2',flat=True)
    ixic_month = IxicChart.objects.values_list('month',flat=True)
    ixic_day = IxicChart.objects.values_list('day',flat=True)
    ixic_bsadf_mi = IxicChart.objects.values_list('bsadf_mi',flat=True)
    ixic_rho_45 = IxicChart.objects.values_list('rho_45',flat=True)
    ixic_day_points = IxicChart.objects.values_list('day_points', flat=True)
    ixic_mid_points = IxicChart.objects.values_list('mid_points', flat=True)
    ixic_down1 = IxicChart.objects.values_list('down1', flat=True)
    ixic_up1 = IxicChart.objects.values_list('up1', flat=True)
    jsondata = {
        "time": list(ixic_time),
        "close": list(ixic_close),
        "clmov": list(ixic_clmov),
        'bsmov': list(ixic_bsmov),
        'rho_sigma': list(ixic_rho_sigma),
        's_mov': list(ixic_s_mov),
        'rho_trend': list(ixic_rho_trend),
        'rho_trend2': list(ixic_rho_trend2),
        'month': list(ixic_month),
        'day': list(ixic_day),
        "bsadf_mi": list(ixic_bsadf_mi),
        "rho_45": list(ixic_rho_45),
        "day_points": list(ixic_day_points),
        "mid_points": list(ixic_mid_points),
        "down1": list(ixic_down1),
        "up1": list(ixic_up1),
    }
    return JsonResponse(jsondata)

#返回ndx
def get_ndx_data(request):
    ndx_time = NdxChart.objects.values_list('time',flat=True)
    ndx_close = NdxChart.objects.values_list('close',flat=True)
    ndx_clmov = NdxChart.objects.values_list('clmov',flat=True)
    ndx_bsmov = NdxChart.objects.values_list('bsmov',flat=True)
    ndx_rho_sigma = NdxChart.objects.values_list('rho_sigma',flat=True)
    ndx_s_mov = NdxChart.objects.values_list('s_mov',flat=True)
    ndx_rho_trend = NdxChart.objects.values_list('rho_trend',flat=True)
    ndx_rho_trend2 = NdxChart.objects.values_list('rho_trend2',flat=True)
    ndx_month = NdxChart.objects.values_list('month',flat=True)
    ndx_day = NdxChart.objects.values_list('day',flat=True)
    ndx_bsadf_mi = NdxChart.objects.values_list('bsadf_mi',flat=True)
    ndx_rho_45 = NdxChart.objects.values_list('rho_45',flat=True)
    ndx_day_points = NdxChart.objects.values_list('day_points', flat=True)
    ndx_mid_points = NdxChart.objects.values_list('mid_points', flat=True)
    ndx_down1 = NdxChart.objects.values_list('down1', flat=True)
    ndx_up1 = NdxChart.objects.values_list('up1', flat=True)
    jsondata = {
        "time": list(ndx_time),
        "close": list(ndx_close),
        "clmov": list(ndx_clmov),
        'bsmov': list(ndx_bsmov),
        'rho_sigma': list(ndx_rho_sigma),
        's_mov': list(ndx_s_mov),
        'rho_trend': list(ndx_rho_trend),
        'rho_trend2': list(ndx_rho_trend2),
        'month': list(ndx_month),
        'day': list(ndx_day),
        "bsadf_mi": list(ndx_bsadf_mi),
        "rho_45": list(ndx_rho_45),
        "day_points": list(ndx_day_points),
        "mid_points": list(ndx_mid_points),
        "down1": list(ndx_down1),
        "up1": list(ndx_up1),
    }
    return JsonResponse(jsondata)

#返回ndx-future
def get_ndx_future_data(request):
    ndx_future_time = NdxFutureChart.objects.values_list('time',flat=True)
    ndx_future_close = NdxFutureChart.objects.values_list('close',flat=True)
    ndx_future_clmov = NdxFutureChart.objects.values_list('clmov',flat=True)
    ndx_future_bsmov = NdxFutureChart.objects.values_list('bsmov',flat=True)
    ndx_future_rho_sigma = NdxFutureChart.objects.values_list('rho_sigma',flat=True)
    ndx_future_s_mov = NdxFutureChart.objects.values_list('s_mov',flat=True)
    ndx_future_rho_trend = NdxFutureChart.objects.values_list('rho_trend',flat=True)
    ndx_future_rho_trend2 = NdxFutureChart.objects.values_list('rho_trend2',flat=True)
    ndx_future_month = NdxFutureChart.objects.values_list('month',flat=True)
    ndx_future_day = NdxFutureChart.objects.values_list('day',flat=True)
    ndx_future_bsadf_mi = NdxFutureChart.objects.values_list('bsadf_mi',flat=True)
    ndx_future_rho_45 = NdxFutureChart.objects.values_list('rho_45',flat=True)
    ndx_future_day_points = NdxFutureChart.objects.values_list('day_points', flat=True)
    ndx_future_mid_points = NdxFutureChart.objects.values_list('mid_points', flat=True)
    ndx_future_down1 = NdxFutureChart.objects.values_list('down1', flat=True)
    ndx_future_up1 = NdxFutureChart.objects.values_list('up1', flat=True)
    jsondata = {
        "time": list(ndx_future_time),
        "close": list(ndx_future_close),
        "clmov": list(ndx_future_clmov),
        'bsmov': list(ndx_future_bsmov),
        'rho_sigma': list(ndx_future_rho_sigma),
        's_mov': list(ndx_future_s_mov),
        'rho_trend': list(ndx_future_rho_trend),
        'rho_trend2': list(ndx_future_rho_trend2),
        'month': list(ndx_future_month),
        'day': list(ndx_future_day),
        "bsadf_mi": list(ndx_future_bsadf_mi),
        "rho_45": list(ndx_future_rho_45),
        "day_points": list(ndx_future_day_points),
        "mid_points": list(ndx_future_mid_points),
        "down1": list(ndx_future_down1),
        "up1": list(ndx_future_up1),
    }
    return JsonResponse(jsondata)



#以下为测试
def get_test(request):
    jsondata = {
        "x": [1, 2, 3],
        "y": [4, 5, 6]
    }
    return JsonResponse(jsondata)


