from .models import Publicity


def publicity_list(request):
    publicity_list = Publicity.objects.filter(active=True)
    return {'publicidades': publicity_list}