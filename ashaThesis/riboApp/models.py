from django.db import models

# Create your models here.
# this is database you can create and add to with classes
# after adding to this, run "python manage.py makemigrations riboApp" then "python manage.py migrate"

class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=400)
    complete = models.BooleanField()

    def __str__(self):
        return self.text


# adding to database from terminal:

# (InteractiveConsole)
# >>> from riboApp.models import Item, ToDoList
# >>> t = ToDoList(name="Asha\'s list")
# >>> t.save()
# >>> ToDoList.objects.all()
# <QuerySet [<ToDoList: Asha's list>]>
# >>> ToDoList.objects.get(id=1)
# <ToDoList: Asha's list>
# >>> a.filter(name__startswith="Asha")
# <QuerySet [<ToDoList: Asha's list>, <ToDoList: Asha's List>]>
