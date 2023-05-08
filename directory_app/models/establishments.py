from django.db import models

class Establishments(models.Model):

    name=models.CharField("Название",max_length=50)
    description=models.CharField("Описание",max_length=250)
    category=models.ForeignKey("directory_app.category",on_delete=models.CASCADE,related_name="categories",verbose_name="Категория",null=False)
    adress=models.CharField("Адресс",max_length=250)
    city=models.ForeignKey("directory_app.city",on_delete=models.CASCADE,related_name="cities",verbose_name="Город",null=False)
    
    
 
    class Meta:
        ordering=["name"]
        verbose_name="Заведение"
        verbose_name_plural="Заведение"

    def __str__(self) -> str:
        return self.name