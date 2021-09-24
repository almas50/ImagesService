from django.views.generic import CreateView, ListView
from .models import Image
from .response import JSONResponse


class ImageCreateView(CreateView):
    model = Image
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        response = JSONResponse({'post': 'true'})
        return response


class ImageView(ListView):
    model = Image
    fields = '__all__'
