from django.urls import path
from .views import FileList,FileDetail,FileCreate,FileUpdate,FileDelete,CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView
urlpatterns=[
    path('login/',CustomLoginView.as_view(),name='login'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('',FileList.as_view(),name='filelist'),
    path('file/<int:pk>',FileDetail.as_view(),name='filedetail'),
    path('filecreate',FileCreate.as_view(),name='filecreate'),
    path('fileupdate/<int:pk>',FileUpdate.as_view(),name='fileupdate'),
    path('filedelete/<int:pk>',FileDelete.as_view(),name='filedelete'),

]