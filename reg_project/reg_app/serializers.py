# from dataclasses import fields
# from operator import is_not
# from django.forms import ValidationError
# from rest_framework import serializers
# from reg_app.models import Register




# class RegisterSerializer(serializers.Serializer):
#     id = serializers.IntegerField
#     firstname = serializers.CharField(max_length=100)
#     lastname = serializers.CharField(max_length=100)
#     email = serializers.CharField(max_length=100)
#     phonenumber = serializers.CharField(max_length=100)
#     password = serializers.CharField(write_only=True)
#     confirmpassword = serializers.CharField(max_length=100)
#     # class meta:
#     #     model = Register
#     #     fields = "__all__"

#     def create(self, data):
#         return Register.objects.create(**data)  
  

#     def update(self,instance,data):

#         instance.firstname = data.get('firstname',instance.firstname)
#         instance.lastname = data.get('lastname',instance.lastname) 
#         instance.email = data.get('email',instance.email) 
#         instance.phonenumber = data.get('phonenumber',instance.phonenumber) 
#         instance.password = data.get('password',instance.password)    
#         instance.confirmpassword = data.get('confirmpassword',instance.confirmpassword)
        
#         instance.save()
        # return instance   


from django.forms import ValidationError
from rest_framework import serializers
from reg_app.models import Register
class RegisterSerializer(serializers.ModelSerializer):

    # description = serializers.SerializerMethodField()

    class Meta:
        
        model =  Register
        fields = '__all__'

    
    # def validate_firstname(self,value):
    #     if value == 'banana':
    #         raise ValidationError('no banana is there')

    #     return value
    
    # def  get_description(self,data):
    #     return "This user name is  " + data.firstname 





                    # instance.alternatephoneNumber = data.get('alternatephoneNumber',instance.alternatephoneNumber)
        # instance.addressline1 = data.get('addressline1',instance.addressline1) 
        # instance.addressline2 = data.get('addressline2',instance.addressline2) 
        # instance.countryorcity = data.get('countryorcity',instance.countryorcity)
        # instance.postalcode = data.get('postalcode',instance.postalcode)
        # instance.companyname = data.get('companyname',instance.companyname)
        # instance.companytype = data.get('companytype',instance.companytype)
        # instance.addressline1 = data.get('addressline1',instance.addressline1) 
        # instance.addressline2 = data.get('addressline2',instance.addressline2) 
        # instance.countryorcity = data.get('countryorcity',instance.countryorcity)
        # instance.postalcode = data.get('postalcode',instance.postalcode)
        