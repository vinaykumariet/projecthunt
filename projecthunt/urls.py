
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
#from products import views
import products.views
urlpatterns = [
    path('admin/', admin.site.urls),
     #path('',views.home,name='home')
    path('',products.views.home,name='home'),
    path('accounts/',include('accounts.urls')),
    path('products/',include('products.urls')),
  path('oauth/',include('social_django.urls',namespace='social')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
