from django.db import models
from django.urls import reverse


class Dish(models.Model):
    dish_name = models.CharField(max_length=25,default='',blank=True,null=True)

    class Meta:
        verbose_name = ("Dish")
        verbose_name_plural = ("Dishes")

    def __str__(self):
        return self.dish_name

    def get_absolute_url(self):
        return reverse("dish_detail", kwargs={"pk": self.pk})

class Item(models.Model):
    name = models.CharField(max_length=55,default='')
    description = models.TextField(blank=True,null=True)
    dish = models.ForeignKey(Dish, related_name="item",on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Item")
        verbose_name_plural = ("Items")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})



class Breakfast(models.Model):
    name = models.CharField(max_length=35,default='')
    dish = models.ForeignKey(Dish, related_name="breakfast_dish",on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("breakfast")
        verbose_name_plural = ("BreakFasts")

    def __str__(self):
        return self.name +" "+"BreakFast"

    def get_absolute_url(self):
        return reverse("brakfast_detail", kwargs={"pk": self.pk})

class Lunch(models.Model):
    name = models.CharField(max_length=35,default='')
    dish = models.ForeignKey(Dish, related_name="lunch_dish",on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("Lunch")
        verbose_name_plural = ("Lunch")

    def __str__(self):
        return self.name +" "+"Lunch"

    def get_absolute_url(self):
        return reverse("lunch_detail", kwargs={"pk": self.pk})


class Dinner(models.Model):
    name = models.CharField(max_length=35,default='')
    dish = models.ForeignKey(Dish, related_name="dinner_dish",on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("dinner")
        verbose_name_plural = ("Dinner")

    def __str__(self):
        return self.name +" "+"Dinner"

    def get_absolute_url(self):
        return reverse("dinner_detail", kwargs={"pk": self.pk})

# Create your models here.
class Weekly(models.Model):
    WEEK_DAYS = (
        ("Monday","Monday"),
        ("Tuesday","Tuesday"),
        ("Wednesday","Wednesday"),
        ("Thursday","Thursday"),
        ("Friday","Friday"),
        ("Saturday","Saturday"),
        ("Sunday","Sunday"),
    )
    breakfast = models.ForeignKey(Breakfast, related_name="breakfast",on_delete=models.CASCADE,blank=True,null=True)
    lunch = models.ForeignKey(Lunch, related_name="lunch",on_delete=models.CASCADE,blank=True,null=True)
    dinner = models.ForeignKey(Dinner, related_name="dinner",on_delete=models.CASCADE,blank=True,null=True)
    day = models.CharField(max_length=20, choices=WEEK_DAYS,blank=True,null=True)

    class Meta:
            verbose_name = ("A Week diet")
            verbose_name_plural = ("Week Diet")

    def __str__(self):
        return str(self.day)

    def get_absolute_url(self):
        return reverse("monday_detail", kwargs={"pk": self.pk})

    

