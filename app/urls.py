from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  

    path('add/', views.add_worker, name='add_worker'),
    path('manage_workers', views.manage_workers, name='manage_workers'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addproduct/', views.add_product, name='add_product'),
    path('addproduct/', views.add_product, name='add_product'),
    path('manage_products/', views.manage_products, name='manage_products'),
    path('worker/<int:pk>/', views.worker_detail, name='worker_detail'),
    path('earnings/', views.dashboard_view, name='dashboard_view'),
     path('earning/', views.all_earnings_view, name='all_earning'),
     path('edit-worker/<int:worker_id>/', views.edit_worker, name='edit_worker'),
     path('edit-product/<int:id>/', views.edit_product, name='edit_product'), 
     path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ajax/get-workers/<int:group_id>/', views.get_workers_by_group, name='get_workers_by_group'),
     path('daily_summary/', views.daily_workerproduct_summary, name='daily_summary'),
path('group-product-summary/', views.group_product_summary_matrix, name='group_product_summary'),
path('export/daily/', views.export_daily_production, name='export_daily'),
    path('export/monthly/', views.export_monthly_summary, name='export_monthly'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

