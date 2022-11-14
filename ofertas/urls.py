from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('oferta',views.OfertasView.as_view(),name='ofertas'),
    path('oferta/<int:oferta_id>',views.OfertasDetailView.as_view())
]