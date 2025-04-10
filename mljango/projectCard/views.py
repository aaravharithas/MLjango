# from django.shortcuts import render
from .models import Project
from django.views.generic import ListView

'''
def home(request):
    projects = Project.objects.order_by('-date_created')
    context = {
        'title' : 'Portfoliohub',
        'projects': projects
    }
    return render(request, 'index.html',context)
'''

class ProjectList(ListView):
    model = Project
    template_name = 'index.html'
    context_object_name = 'projects'
    paginate_by = 6

    def get_queryset(self):
        return Project.objects.order_by('-date_created')