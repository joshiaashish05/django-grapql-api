import graphene
import apiapp.schema


class Query(apiapp.schema.Query, graphene.ObjectType):
    pass


class Mutation(apiapp.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
