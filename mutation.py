import graphene


class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()


class CreatePerson(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        age = graphene.Int()

    person = graphene.Field(Person)

    def mutate(root, info, name, age):
        person = Person(name=name, age=age)
        return CreatePerson(person=person)


class Mymutation(graphene.ObjectType):
    createPeople = CreatePerson.Field()


schema = graphene.Schema(mutation=Mymutation)


result = schema.execute(
    """
mutation Myfirst{
    createPeople(name:"dr.Strange",age:34){
        person{
            name
            age
        }
    }
}
"""
)


print(result.data)
