"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'ledbillboard.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.children.append(modules.ModelList(
            title=_('Users'),
            column=1,
            models=(
                'ledbillboard.account.*',
            ),
        ))

        self.children.append(modules.ModelList(
            title=_('Billboards'),
            column=1,
            models=(
                'ledbillboard.board.*',
            ),
        ))

        self.children.append(modules.ModelList(
            title=_('Playlist and media items'),
            column=1,
            models=(
                'ledbillboard.playlist.*',
            ),
        ))
        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=10,
            column=2,
        ))
