from django import template

from blogs.models import Post

register = template.Library()
@register.inclusion_tag('blogs/sidebars.html')
def sidebar_results():
    posts = Post.objects.all().order_by('-date')[:5]
    # context = {
    #     'new_post': post
    # }
    # return render(request, 'blogapp/sidebars.html', context)
    return {'posts': posts}
