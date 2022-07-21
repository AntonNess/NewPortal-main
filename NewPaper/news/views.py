#from datetime import datetime
from django.urls import reverse_lazy
from .filters import PostFilter
from .forms import PostForm
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post

class PostList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'posts'
#    paginate_by = 1

class PostSearch(ListView):
    model = Post
    ordering = 'title'
    template_name = 'search.html'
    context_object_name = 'posts'
    paginate_by = 10


#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['time_now'] = datetime.utcnow()
#        return context
   # Переопределяем функцию получения списка товаров
    def get_queryset(self):
    # Получаем обычный запрос
        queryset = super().get_queryset()
       # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали
       # в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
       # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'new.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'

#def create_post(request):
#    form = PostForm()

#    if request.method == 'POST':
#        form = PostForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('/news/')


#    return render(request, 'post_edit.html', {'form': form})
class PostCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'post_edit.html'

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')