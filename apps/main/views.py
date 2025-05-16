# Create your views here.
from django.views.generic import TemplateView


class RobotView(TemplateView):
    template_name = 'robots.txt'
    content_type = "text/plain"
