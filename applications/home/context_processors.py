from .models import Publicity, Warp


def publicity_list(request):
    publicity_list = Publicity.objects.filter(active=True)
    return {'publicidades': publicity_list}

def warp_print(request):
    warp = Warp.objects.filter(active=True).last()
    return {'warp':warp}