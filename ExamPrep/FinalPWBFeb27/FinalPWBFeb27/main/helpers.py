from django.shortcuts import render, redirect

from FinalPWBFeb27.main.models import Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def form_view(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)
    ctx = {
        'instance': instance,
        'form': form
    }
    return render(request, template_name, ctx)


class DisabledFormMixin:

    def _init_disabled(self):
        for _, field in self.fields.items():
            setattr(field, 'disabled', 'disabled')
