


from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .models import ToDo

# Create your views here.


def index(request):
    todos = ToDo.objects.all()
    return render(request, 'todoapp/index.html', {'test_list': todos, 'title': 'Главная страница'})

@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    todo = ToDo(title=title)
    todo.save()
    return redirect('index')

def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complite
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')
                  

                                                   
                                                   
