from django.contrib.syndication.views import Feed
from .models import Artical

class ArticalFeed(Feed):
    title = 'xfn的个人博客'
    description = '欢迎访问'
    link = '/'

    def items(self):
        return Artical.objects.all().order_by('-creat_time')[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:10]

    def item_link(self, item):
        return '/single/%s/'%(item.id,)