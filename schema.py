import graphene
import json
from datetime import datetime


class user(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    last_login = graphene.DateTime(required=False)


class Query(graphene.ObjectType):
    isstaff = graphene.Boolean(name="is_staff")
    users = graphene.List(user, first=graphene.Int())

    def resolve_users(self, info, first):
        return [
            user(name="mk", last_login=datetime.now()),
            user(name="jk", last_login=datetime.now()),
            user(name="ck", last_login=datetime.now()),
            user(name="sk", last_login=datetime.now()),
        ][first:]

    def resolve_isstaff(self, info):
        return True


schema = graphene.Schema(query=Query)

result = schema.execute(
    """
{
    is_staff,
    people:users(first:2){
        name
    }
    
}
"""
)


print(json.dumps(dict(result.data.items()), indent=2))

