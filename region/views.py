from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect , HttpResponse
from .forms import RegionForm
import xlwt
from .models import Region
from . import plot
import numpy as np

def index(request):

	
    if request.method == "POST":
        form = RegionForm(request.POST)
        if form.is_valid():
            region = form.save()
    else :
        form = RegionForm()
    
    #form = RegionForm()                    
    context = {"form":form}

    return render(request,"region/index.html",context=context)


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="test.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('region')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ["year","population","nb_lits_touristiques","chomage","activity","nb_medecin","nuitees_touristiques", 
    "nb_eleves_primaire","nb_eleves_college","nb_eleves_lycee","pop_pour_UN_med" ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Region.objects.all().values_list("year","population","nb_lits_touristiques","chomage",
    "activity","nb_medecin","nuitees_touristiques", "nb_eleves_primaire","nb_eleves_college","nb_eleves_lycee")
    for row in rows:
        row_num += 1
        for col_num in range(len(row)+1):
            if col_num == len(row) :
                ws.write(row_num, col_num, np.round(row[1]/row[5],2), font_style)
            else :
                ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    
    
    return response





def plot(request):
    
    return render( request, "dash/dash.html")
