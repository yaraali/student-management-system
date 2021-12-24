from django import forms

class userRegister(forms.Form):
    firstName =  forms.CharField(required= True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    lastName= forms.CharField(required= True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    age = forms.FloatField(required= True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    birthDate = forms.CharField(required= True, widget=forms.TextInput(attrs={'class': 'form-control'}))
   
class userDegree(forms.Form):
    studentDegree =  forms.CharField(required= True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    

