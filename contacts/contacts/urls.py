from django.contrib import admin
from django.urls import path, include
from api.views import contact_list

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/contacts', contact_list, name='contact_list'),
	path('app/', include("api.urls")),
]
