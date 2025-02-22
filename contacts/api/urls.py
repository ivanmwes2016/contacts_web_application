from django.urls import path
from .views import contact_page, get_contact_by_id, update_contact, delete_contact, create_contact

urlpatterns = [
	path('', contact_page, name="contact_page"),
	path('contact/create', create_contact, name='create-contact'),
	path('contact/<int:id>', get_contact_by_id, name='contact_detail'),
	path('contact/<int:id>/update', update_contact, name='update_contact'),
	path('contact/<int:id>/delete', delete_contact, name='delete_contact'),
]