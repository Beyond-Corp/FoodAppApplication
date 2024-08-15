from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

class Item(models.Model):
    def __str__(self):
        return self.item_name

    # FK
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    item_name = models.CharField(max_length=200)
    item_describe = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=1000, default="https://cdn.dribbble.com/users/1012566/screenshots/4187820/media/985748436085f06bb2bd63686ff491a5.jpg?resize=400x300&vertical=center")

    #video 60 : attention a cette ligne car elle est base sur un code que je n'ai pas fait c'est au niveau de la classbaseview pour details  # # 🚩🚩🚩🚩🚩VIDEO 58🚩🚩🚩🚩🚩 # CLASS BASE URLS # -> for detail


def get_absolute_url(self):
    return reverse('food:detail', kwargs={"pk": self.pk})
