from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crm/', include('crm.urls')),
    path('retail_pos/', include('retail_pos.urls')),
    path('restaurant_pos/', include('restaurant_pos.urls')),
    path('hotel_pms/', include('hotel_pms.urls')),
    path('accounting/', include('accounting.urls')),
    path('invoicing/', include('invoicing.urls')),
    path('inventory/', include('inventory.urls')),
    path('film_generator/', include('film_generator.urls')),
    path('music_generator/', include('music_generator.urls')),
    path('video_generator/', include('video_generator.urls')),
    path('app_maker/', include('app_maker.urls')),
]
