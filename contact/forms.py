from django import forms

class ContactF(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Nombre',}
    ))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Correo',}
    ))
    content = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'placeholder':'Mensaje',}
    ))