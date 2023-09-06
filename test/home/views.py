from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/index.html'

class GuatemalaView(TemplateView):
    template_name = 'home/guatemala.html'
