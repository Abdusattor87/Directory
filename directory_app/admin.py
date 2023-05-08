from django.contrib import admin
from directory_app.models import Establishments,City,Category,Contact
from django.contrib.auth.models import Group

admin.site.unregister(Group)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    list_display=("name","category_counts")
    search_fields=("name",)

    def  category_counts(self,instance):
        return instance.categories.count()
    category_counts.short_description="Кол заведений"

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

 
@admin.register(Establishments)
class Establishments(admin.ModelAdmin):

    model=Establishments
    list_display=("id","name","description","category","adress","city")
    list_filter=("category","city")
    search_fields=("name",)
    list_display_links=("id","name")
    list_per_page = 10
  
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass