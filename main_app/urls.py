from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('pens/', views.pens_index, name='index'),
	path('pens/<int:pen_id>/', views.pens_detail, name='detail'),
	path('pens/create/', views.PenCreate.as_view(), name='pens_create'),
	path('pens/<int:pk>/update/', views.PenUpdate.as_view(), name='pens_update'),
	path('pens/<int:pk>/delete/', views.PenDelete.as_view(), name='pens_delete'),
	path('pens/<int:pen_id>/add_refill/', views.add_refill, name='add_refill'),
	path('pens/<int:pen_id>/assoc_ink/<int:ink_id>/', views.assoc_ink, name='assoc_ink'),
	path('inks/', views.InkList.as_view(), name='inks_index'),
	path('inks/<int:pk>/', views.InkDetail.as_view(), name='inks_detail'),
	path('inks/create/', views.InkCreate.as_view(), name='inks_create'),
	path('inks/<int:pk>/update/', views.InkUpdate.as_view(), name='inks_update'),
	path('inks/<int:pk>/delete/', views.InkDelete.as_view(), name='inks_delete'),
]