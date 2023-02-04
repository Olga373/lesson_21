from django.http import HttpResponseRedirect
from .models import TodoListItem


def add_item(request):
    text = request.POST.get("content")
    new_item = TodoListItem(content=text)
    new_item.save()

    return HttpResponseRedirect(redirect_to="/todo/")

def delete_item(request, object):
    item = TodoListItem.objects.get(pk=object)
    item.delete()
    return HttpResponseRedirect(redirect_to="/todo/")




