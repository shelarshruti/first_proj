#from django import forms

#class ProductForm(forms.Form):
    #name = forms.CharField(max_length=200, label='enter name')
    #price = forms.IntegerField()
    #quantity = forms.IntegerField()



from django import forms
from django.forms import ModelForm
from utility.models import Products
 
 
# creating a form
class ProductForm(ModelForm):
    class Meta:
        # specify model to be used
        model = Products
 
        # specify fields to be used
        fields = [
            'name',
            'price',
            'quantity',
            'img'
        ]



'''
fields = [
            "name",
            "price",
        ]
'''
