import graphene
from graphene_django.types import DjangoObjectType
from .models import Contact

class ContactType(DjangoObjectType):
	class Meta:
		model = Contact
		fields = "__all__"


class Query(graphene.ObjectType):
	all_contacts = graphene.List(ContactType)
	contact_by_id = graphene.Field(ContactType, id=graphene.Int(required=True))

	def resolve_all_contacts(self, info, **kwargs):
		return Contact.objects.all()
	
	def resolve_contacts_by_id(self, info, id):
		return Contact.objects.get(id = id)

class CreateContact(graphene.Mutation):
	class Arguments:
		first_name = graphene.String(required=True)
		second_name = graphene.String(required=True)
		email = graphene.String()
		post_code = graphene.String()
		contact_number= graphene.String()

	contact = graphene.Field(ContactType)

	def mutate(self, info, first_name, second_name,  email, post_code, contact_number ):
		contact = Contact.objects.create(
			first_name=first_name,
			second_name=second_name,
			email=email,
			post_code=post_code,
			contact_number=contact_number
		)
	
		return CreateContact(contact=contact)
	
class Mutation(graphene.ObjectType):
	create_contact = CreateContact.Field()
	
schema = graphene.Schema(query=Query, mutation=Mutation)