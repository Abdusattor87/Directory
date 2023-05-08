from rest_framework import serializers
from directory_app.models import Establishments,Category,Contact,City

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = "__all__"
    
  

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        #fields = "__all__"
        fields = ("id","phone", "phone_add", "working_mode", "image","email")


    


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields =  "__all__"
    
class EstablishmentsListSerializer(serializers.ModelSerializer):
 
    
    class Meta:
        model = Establishments
        fields =("name",)


   

class EstablishmentsSerializer(serializers.ModelSerializer):


    contact = ContactSerializer()
    category = CategorySerializer()
    city = CitySerializer()
    
    class Meta:
        model = Establishments
        fields ="__all__"