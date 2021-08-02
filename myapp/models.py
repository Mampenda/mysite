from django.db import models
from django.forms import model_to_dict
from django.utils.timezone import now

class Item(models.Model):
    title = models.CharField(max_length=200)  # Short description of the item
    datetime_found = models.DateTimeField(default=now, blank=True)  # Date and time of when the item was found


def items():
    res = []
    for i in Item.objects.all():
        res.append(model_to_dict(i))
    return res


class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def __int__(self):
        return self.id


class ListItem(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)  # related to ToDoList
    text = models.CharField(max_length=300)
    complete = models.BooleanField()  # Boolean says if we're completed list item

    def __str__(self):
        return self.text