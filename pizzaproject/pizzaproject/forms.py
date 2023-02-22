from django import forms
class pizzafrom(forms.form):
    Topping_1 = forms.CharField(label="Topping 1",max_length=100)
    Topping_2= forms.CharField(label="Topping 2",max_length=100)
    Size = forms.choiceField(label="Size",choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])