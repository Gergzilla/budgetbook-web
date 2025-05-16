from django.shortcuts import render, HttpResponse

from .forms import BudgetImportForm

from django.core.files.storage import FileSystemStorage
import csv

# This code does nothing, dont use it just read it
def importer_app_check(request):
    return HttpResponse("This is the default importer_app_chec() function in importer/views.py")

def import_page(request):
    return render(request, "import.html")

def import_expense_file(request):
    form = BudgetImportForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.date = "Jan2024" #default for test should be a var
        obj.save()


#dont use this at all, just here for reference
def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        
        # Open and parse the file based on its type
        if filename.endswith('.csv'):
            with open(fs.path(filename), 'r') as file:
                reader = csv.reader(file)
                data = list(reader)
        elif filename.endswith('.txt'):
            with open(fs.path(filename), 'r') as file:
                data = file.readlines()
        else:
            data = ["Unsupported file type"]
        
        return render(request, 'preview.html', {
            'uploaded_file_url': uploaded_file_url,
            'data': data
        })
    return render(request, 'preview.html')