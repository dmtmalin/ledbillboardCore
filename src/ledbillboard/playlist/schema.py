import graphene
from graphene import relay
from graphene_django.filter.fields import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from ledbillboard.mediacontent.models import Media
from ledbillboard.playlist.models import Playlist
from ledbillboard.references.models import Schedule


class ScheduleType(DjangoObjectType):
    class Meta:
        model = Schedule


class MediaType(DjangoObjectType):
    url = graphene.String()

    def resolve_url(self: Media, args, context, info):
        return self.file.url

    class Meta:
        model = Media


class PlaylistType(DjangoObjectType):
    media = graphene.List(MediaType)

    def resolve_media(self: Playlist, args, context, info):
        return Media.objects.filter(playlist=self, is_approve=True)

    class Meta:
        model = Playlist
        filter_fields = {
            'board__slug': ['exact']
        }
        interfaces = (relay.Node,)


class Query(graphene.AbstractType):
    all_playlist = DjangoFilterConnectionField(PlaylistType)
