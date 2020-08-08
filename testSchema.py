import graphene
import json

f = None
l = None


class Friends(graphene.ObjectType):
    id = graphene.ID()
    first_name = graphene.String()
    last_name = graphene.String()


class Query(graphene.ObjectType):
    name = graphene.String(
        firstName=graphene.String(default_value="Dr."),
        lastName=graphene.String(default_value="strange"),
    )
    age = graphene.Int(num=graphene.Int(default_value=20))
    friend = graphene.Field(Friends, first=graphene.String(), last=graphene.String())

    def resolve_friend(root, info, first, last):
        return Friends(first_name=first, last_name=last)

    def resolve_name(root, info, firstName, lastName):
        f = firstName
        l = lastName
        return f"hello {f} {l}"

    def resolve_age(root, info, num):
        x = num + 20
        return x


schema = graphene.Schema(query=Query)

result = schema.execute(
    """
{
    name(firstName:"m" , lastName:"k"),
    age(num:18),
    friend(first:"joey",last:"tribbiani"){
        firstName
        lastName
    }
        
    
}
"""
)

print(json.dumps(dict(result.data), indent=4))

