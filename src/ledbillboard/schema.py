import graphene
import ledbillboard.playlist.schema


class Query(ledbillboard.playlist.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
