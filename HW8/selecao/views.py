from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import ContactForm


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('selecao:post_list')
        else:
            return redirect('selecao:post_list')
    template = 'selecao/post/list.html'
    context = {
        'posts': posts,
        'form': form,
               }
    return render(request, template, context)


def post_detail(request, post):
    single_post = get_object_or_404(Post, slug=post)
    template = 'selecao/post/detail.html'
    return render(request, template, {'post': single_post})
