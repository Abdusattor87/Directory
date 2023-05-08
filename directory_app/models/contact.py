from django.db import models

class Contact(models.Model):

    phone = models.CharField("Номер телефона",max_length=12)
    phone_add = models.CharField("Доп. номер телефона",max_length=12)
    email=models.CharField("Почта",max_length=50)
    working_mode=models.CharField("Режим работы",max_length=50)
    image = models.ImageField(upload_to="Photos/")

    establishments =models.OneToOneField("directory_app.establishments",related_name="contact",verbose_name="Заведения", on_delete=models.CASCADE)

    class Meta:
        verbose_name="Контакт"
        verbose_name_plural="Контакты"

    def __str__(self) -> str:
        return f"Контакты {self.establishments}"