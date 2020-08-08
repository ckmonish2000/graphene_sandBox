import graphene
import json

f=None
l=None

class Friends(graphene.ObjectType):
    id=graphene.ID()
    first_name=graphene.String()
    last_name = graphene.String()

class Query(graphene.ObjectType):
    name=graphene.String(firstName=graphene.String(default_value="Dr."),lastName=graphene.String(default_value="strange"))
    age=graphene.Int(num=graphene.Int(default_value=20))
    friend=Friends

    def resolve_friend(root,info):
        return[
            Friends(first_name="rahul",last_name="jain"),
            Friends(first_name="md.",last_name="saquib"),
            Friends(first_name="B",last_name="P"),
            
        ]

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
    age(num:18),
    
}
'''
)

print(result.data)



    

