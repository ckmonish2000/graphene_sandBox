import graphene
import json

class Query(graphene.ObjectType):
    isstaff=graphene.Boolean(name="is_staff")

    def resolve_isstaff(self,info):
        return True

schema=graphene.Schema(query=Query)

result=schema.execute('''
{
    is_staff
}
'''
)


print(json.dumps(dict(result.data.items()),indent=2))
