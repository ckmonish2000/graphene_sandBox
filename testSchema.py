import graphene
import json


class Query(graphene.ObjectType):
    name=graphene.String(firstName=graphene.String(default_value="Dr."),lastName=graphene.String(default_value="strange"))
    age=graphene.Int()

    def resolve_name(root,info,firstName,lastName):
        return f"hello {firstName} {lastName}"

    

