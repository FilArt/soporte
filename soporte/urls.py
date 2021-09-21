from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from helpdesk.urls import base64_pattern

from .views import datatables_ticket_list, tickets

urlpatterns = [
    path("jet/", include("jet.urls", "jet")),
    path("jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),
    path("admin/", admin.site.urls),
    path("tickets/", tickets),
    re_path(
        r"^datatables_ticket_list/(?P<query>{})$".format(base64_pattern),
        datatables_ticket_list,
        name="datatables_ticket_list",
    ),
    path("", include("helpdesk.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
