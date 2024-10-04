from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crm/', include('crm.urls')),
    path('retail/', include('retail_pos.urls')),
    path('restaurant/', include('restaurant_pos.urls')),
    path('hotel/', include('hotel_pms.urls')),
    path('accounting/', include('accounting.urls')),
    path('invoicing/', include('invoicing.urls')),
    path('inventory/', include('inventory.urls')),
    path('film/', include('film_generator.urls')),
    path('music/', include('music_generator.urls')),
    path('video/', include('video_generator.urls')),
    path('app/', include('app_maker.urls')),
]
