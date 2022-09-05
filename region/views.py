from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect , HttpResponse
from .forms import RegionForm
import xlwt
from .models import Region
from .plot import plotly_plot


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
    response['Content-Disposition'] = 'attachment; filename="test.csv"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('region')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ["year","population","nb_lits_touristiques","chomage","activity","nb_medecin","nuitees_touristiques", 
    "nb_eleves_primaire","nb_eleves_college","nb_eleves_lycee"  ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Region.objects.all().values_list("year","population","nb_lits_touristiques","chomage",
    "activity","nb_medecin","nuitees_touristiques", "nb_eleves_primaire","nb_eleves_college","nb_eleves_lycee")
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    
    
    return response




#def root(request,id):

#    context = {"id":id}
#    return render(request,"index.html",context=context)

def plot(request):



    #Plotly visualizations
    target_plot1 , target_plot2 = plotly_plot("chomage")
    ...
    #Return context to home page view
    context = {'target_plot1': target_plot1,
        'target_plot2': target_plot2 }
        
    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'dash/dash.html',
        context= context)
