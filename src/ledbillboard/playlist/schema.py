import graphene
from graphene import relay
from graphene_django.filter.fields import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from ledbillboard.mediacontent.models import Media
from ledbillboard.playlist.models import Playlist
from ledbillboard.references.models import Schedule


class ScheduleType(DjangoObjectType):
    id = graphene.Int()

    class Meta:
        model = Schedule


class MediaType(DjangoObjectType):
    id = graphene.Int()
    url = graphene.String()

    def resolve_url(self: Media, args, context, info):
        return self.file.url

    class Meta:
        model = Media


class PlaylistType(DjangoObjectType):
    media = graphene.List(MediaType)
    base_id = graphene.Int()
    company = graphene.String()

    def resolve_media(self: Playlist, args, context, info):
        return Media.objects.filter(playlist=self, is_approve=True)

    def resolve_base_id(self: Playlist, args, context, info):
        return self.id

    def resolve_company(self: Playlist, args, context, info):
        return self.board.company.name

    class Meta:
        model = Playlist
        filter_fields = {
            'board__slug': ['exact']
        }
        interfaces = (relay.Node,)


class Query(graphene.AbstractType):
    all_playlist = DjangoFilterConnectionField(PlaylistType)
