from django.views.generic import TemplateView

# TemplateView este o clasa de Django  folosita pentru randarea a unui template in interfata.

class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'
