from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FilesData
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm



class CustomLoginView(LoginView):
    template_name='core/login.html'
    fields='__all__'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('filelist')

class RegisterPage(FormView):
    template_name='core/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('filelist')

    def form_valid(self,form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('filelist')
        return super(RegisterPage,self).get(*args,**kwargs)

class FileList(LoginRequiredMixin,ListView):
    model= FilesData
    context_object_name='file_list'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['file_list']=context['file_list'].filter(user=self.request.user)
        return context

class FileDetail(LoginRequiredMixin,DetailView):
    model=FilesData
    context_object_name='file_detail'

class FileCreate(LoginRequiredMixin,CreateView):
    model=FilesData
    fields=['title','descreption','document']
    success_url=reverse_lazy('filelist')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(FileCreate,self).form_valid(form)

class FileUpdate(LoginRequiredMixin,UpdateView):
    model=FilesData
    fields=['title','descreption','document']
    success_url=reverse_lazy('filelist')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(FileCreate,self).form_valid(form)


class FileDelete(LoginRequiredMixin,DeleteView):
    model=FilesData
    context_object_name='file'
    success_url=reverse_lazy('filelist')

