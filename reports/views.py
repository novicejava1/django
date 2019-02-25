from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
from django.conf import settings

from json2html import *
import json
import os

from django.http import HttpResponseRedirect
from .forms import NameForm
from .forms import ChartForm
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from fusioncharts import FusionCharts

def myFirstChart(request):

    myfile = request.FILES['myfile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    document_root = settings.MEDIA_ROOT
    docfile = document_root + "/" + filename
    #file = open("/home/admin1/pythonDjango/mysite/%s" % uploaded_file_url, "r")
    file = open("%s" % docfile, "r")
    mydata = json.load(file)
    dataSource = json.dumps(mydata)

    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)

    return render(request, 'reports/myFirstChart.html', {
        'output': column2D.render()
    })


def mySecondChart(request):

    myfile = request.FILES['myfile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    document_root = settings.MEDIA_ROOT
    docfile = document_root + "/" + filename
    file = open("%s" % docfile, "r")
    #file = open("/home/admin1/pythonDjango/mysite/%s" % uploaded_file_url, "r")
    data = json.load(file)
    response = json2html.convert(json = data)
    #context = {'response': response}
    #return render(request, 'reports/mySecondChart.html', context)
    return HttpResponse(response)


def myThirdChart(request):

    myfile = request.FILES['myfile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    document_root = settings.MEDIA_ROOT
    docfile = document_root + "/" + filename
    file = open("%s" % docfile, "r")
    #file = open("/home/admin1/pythonDjango/mysite/%s" % uploaded_file_url, "r")
    mydata = json.load(file)
    dataSource = json.dumps(mydata)

    pie3d = FusionCharts("pie3d", "myThirdChart" , "100%", "400", "myThirdChart-container", "json", dataSource)
    return render(request, 'reports/myThirdChart.html', {
    'output': pie3d.render()
    })


def myFourthChart(request):

    myfile = request.FILES['myfile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    document_root = settings.MEDIA_ROOT
    docfile = document_root + "/" + filename
    file = open("%s" % docfile, "r")
    #file = open("/home/admin1/pythonDjango/mysite/%s" % uploaded_file_url, "r")
    mydata = json.load(file)
    dataSource = json.dumps(mydata)

    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    line2d = FusionCharts("line", "myFourthChart", "600", "400", "myFourthChart-container", "json", dataSource)

    return render(request, 'reports/myFourthChart.html', {
        'output': line2d.render()
    })

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        name = request.POST.get('your_name')
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')
            return HttpResponse("Hi %s " % name)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'reports/name.html', {'form': form})

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'reports/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'reports/simple_upload.html')

def select_chart(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        form = ChartForm(request.POST)
        chartName = request.POST.get('chartName')
        if form.is_valid():
            if chartName == "tablechart":
                return mySecondChart(request)
            elif chartName == "piechart":
                return myThirdChart(request)
            elif chartName == "barchart":
                return myFirstChart(request)
            else:
                return myFourthChart(request)
            return HttpResponse("Valid Chart is uploaded : %s " % chartName)
    else:
        form = ChartForm()

    return render(request, 'reports/chart.html', {'form': form})


