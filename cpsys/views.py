from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import TeamRecord
from django.views.generic import View
from django.http import HttpResponseRedirect



@csrf_protect
def records(request):
    all_records = TeamRecord.objects.all()
    return render(
        request,
        "cpsys/records.html",
        context={"records": all_records},
    )


# class UploadView(View):
#     form_class = UploadFileForm
#     template_name = "cpsys/upload.html"
#     initial = {'key': 'value'}

#     @method_decorator(login_required)
#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST, request.FILES)
#         if form.is_valid():

#         return render(request, self.template_name, {'form': form})


# def file_upload(request):
#     save_path = os.path.join(settings.MEDIA_ROOT, "uploads", request,
#                              FILES['file'])
#     path = default_storage.save(save_path, request.FILES['file'])
#     return default_storage.path(path)