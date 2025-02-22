from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact
from django.shortcuts import get_object_or_404


class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = "__all__"

def contact_page(request):
	return render(request, "api/contact_page.html")

@api_view(['POST'])
def create_contact(request):
	serializer = ContactSerializer(data= request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def contact_list(request):
	contacts = Contact.objects.all()
	serializer = ContactSerializer(contacts, many=True)
	return JsonResponse({'contacts': serializer.data})

@api_view(['GET'])
def get_contact_by_id(request, id):

	try:
		contact = Contact.objects.get(id=id)
	except Contact.DoesNotExist:
		raise Http404("Contact not found")
	
	serializer = ContactSerializer(contact)
	return JsonResponse(serializer.data, safe=True)

@csrf_exempt
@api_view(['PATCH'])
def update_contact(request, id):

	try:

		contact = get_object_or_404(Contact, id=id)
		data = json.loads(request.body)
		
		
		for key, value in data.items():
			if hasattr(contact, key):
				setattr(contact, key, value)

		contact.save()
		return JsonResponse({"message": "Contact update successfuly"}, status=201)
	except Exception as e:
		return JsonResponse({"error": str(e)}, status=400)
	

@api_view(['DELETE'])
def delete_contact(request, id):
    try:
        contact = get_object_or_404(Contact, id=id)
        contact.delete()  # This will delete the contact
        return Response({"message": "Contact deleted successfully"}, status=204)
    except Exception as e:
        return Response({"error": str(e)}, status=400)