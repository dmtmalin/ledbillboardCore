import graphene
from graphene_django.types import DjangoObjectType

from ledbillboard.playlist.models import Playlist


class PlaylistType(DjangoObjectType):
    class Meta:
        model = Playlist


class Query(graphene.AbstractType):
    all_playlists = graphene.List(PlaylistType)

    def resolve_all_playlists(self, args, context, info):
        if context.user.is_authenticated():
            return Playlist.objects.all()
        else:
            return Playlist.objects.none()
