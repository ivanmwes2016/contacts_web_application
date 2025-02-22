
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from api.schema import schema
from api.views import contact_list

urlpatterns = [
	path('admin/', admin.site.urls),
	path('graphql/', GraphQLView.as_view(graphiql = True, schema = schema)),
	path('api/contacts', contact_list, name='contact_list'),
	path('app/', include("api.urls")),
]
