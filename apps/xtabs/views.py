from django.views.generic.base import TemplateView
 
 
class OnePageAppView(TemplateView):
    template_name = 'one_page_app.html'