from django.views.generic import TemplateView
from django.shortcuts import render

def home(request):
    return render(request, 'index.html',{})

class index_page(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("-----!!!!!!!!!---------!!!!!!!!!---------")
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


def receive_text(request):
    result = 'default'
    if request.method == "POST":
        result = 'POST request successfuly processed'
    else:
        result = request.method
    return result