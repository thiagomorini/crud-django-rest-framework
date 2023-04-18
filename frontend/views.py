from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.forms import ModelForm
from .models import Module

class ModuleForm(ModelForm):
    class Meta:
        model = Module
        fields = ['id', 'serial_number', 'name', 'description']

class ModuleListView(ListView):
    model = Module
    template_name = 'module_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modules'] = Module.objects.all()
        return context

class ModuleCreateView(CreateView):
    model = Module
    form_class = ModuleForm
    template_name = 'module_form.html'
    success_url = reverse_lazy('module_list')

class ModuleUpdateView(UpdateView):
    model = Module
    form_class = ModuleForm
    template_name = 'module_form.html'
    success_url = reverse_lazy('module_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module'] = self.object
        return context

class ModuleDeleteView(DeleteView):
    model = Module
    success_url = reverse_lazy('module_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module'] = self.object
        return context
