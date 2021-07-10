from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from core.models import Solicitud

# Create your views here.
class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context.update({
            "solicitudes": Solicitud.objects.filter(user=self.request.user)
        })
        return context


class HomeView(generic.TemplateView):
    template_name = 'index.html'

class UserDetailView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'solicitud.html'
    queryset = Solicitud.objects.all()
    context_object_name = 'solicitud'

class AprobarView(generic.View):
    def get(self, request, *args, **kwargs):
        solicitud = get_object_or_404(Solicitud, id=kwargs['pk'])
        solicitud.estado = 'A'
        solicitud.save()

        return redirect("profile") 

class RechazarView(generic.View):
    def get(self, request, *args, **kwargs):
        solicitud = get_object_or_404(Solicitud, id=kwargs['pk'])
        solicitud.estado = 'N'
        solicitud.save()
        return redirect("profile") 

