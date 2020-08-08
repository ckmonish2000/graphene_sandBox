import graphene
import json

f=None
l=None


class Query(graphene.ObjectType):
    name=graphene.String(firstName=graphene.String(default_value="Dr."),lastName=graphene.String(default_value="strange"))
    age=graphene.Int(num=graphene.Int(default_value=20))

    def resolve_name(root,info,firstName,lastName):
        f=firstName
        l=lastName
        return f"hello {f} {l}"

    def resolve_age(root,info,num):
        x=num+20
        return x


schema=graphene.Schema(query=Query)

result=schema.execute('''
{
    name(firstName:"m" , lastName:"k"),
    age(num:18)
}
'''
)

print(result.data)



    

