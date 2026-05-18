from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import CommentForm
from django.shortcuts import redirect
def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request, 'Jumbo/home.html',context)

class PostListView(ListView):
    model= Post
    template_name= 'Jumbo/home.html'#<app>/<model>_<viewtype>.html
    context_object_name= 'posts'
    ordering = ['-date_posted','title']
    paginate_by = 5

class UserPostListView(ListView):
    model= Post
    template_name= 'Jumbo/user_posts.html'#<app>/<model>_<viewtype>.html
    context_object_name= 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
            



class PostDetailView(DetailView):
    model= Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comment_form'] = CommentForm()

        context['comments'] = self.object.comments.filter(
            parent=None
        )

        return context
       
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user

            parent_id = request.POST.get('parent_id')

            if parent_id:
                comment.parent = Comment.objects.get(id=parent_id)

            comment.save()

        return redirect('post-detail', pk=post.pk)

class PostCreateView(LoginRequiredMixin,CreateView):
    model= Post
    fields= ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
     
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model= Post
    fields= ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model= Post
    success_url= reverse_lazy('Jumbo-home') 
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request,'Jumbo/about.html', {'title':'About'})




