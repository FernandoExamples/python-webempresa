from .models import Link


def add_social_links(request):
    links = Link.objects.all()
    context = {}
    for link in links:
        context[link.key] = link.url
        
    return context
