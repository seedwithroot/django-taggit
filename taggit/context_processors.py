from models import *
from items.models import *

def trending_tags(request):
    return {'trending_tags':Item.tags.most_common()}
