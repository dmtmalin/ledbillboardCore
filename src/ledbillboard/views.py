from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from ledbillboard.decorators import login_required_forbidden


@method_decorator([csrf_exempt, login_required_forbidden], name='dispatch')
class PrivateGraphQLView(GraphQLView):
    pass
