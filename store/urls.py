from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.store,name='store'),
    path('category<slug:category_slug>',views.store,name='category_product'),
    path('category<slug:category_slug>/<slug:product_slug>',views.product_detail,name='product_details'),
    path('search',views.Search,name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
