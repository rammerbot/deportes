from .models import Sports, SportCategories

def sports_list(request):
    sports = Sports.objects.filter()
    return {'sports_list': sports}

def sport_categories(request):
    sport_categories = SportCategories.objects.filter()
    return {'sport_categories': sport_categories}