from django.contrib.sites.shortcuts import get_current_site


def globalContext(request):
    return dict(
        current_site=get_current_site(request),
    )
