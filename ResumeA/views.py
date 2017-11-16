from django.shortcuts import render
import ResumeA.Models.index as index_model


# Create your views here.
def index(request):
    return render(request, 'Index.html', index_model.context())
