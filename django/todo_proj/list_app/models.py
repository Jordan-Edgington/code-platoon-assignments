from django.db import models

# Create your models here.


class List(models.Model):
    list_name = models.CharField()
# LIST CLASS

# ID - foreign key relationship to task - parent_list
# LIST_NAME - CHAR
