from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'surname', 'email', 'adres', 'code', 'city']
        labels = {'name':'Imię','surname':'Nazwisko', 'email':'Adres E-mail','code':'Kod pocztowy', 'city':'Miasto'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Wpisz imię'}),
            'surname': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Wpisz nazwisko'}),
            'email': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Wpisz swój adres email np.sklepmeblowy@meble.pl'}),
            'adres': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Podaj adres zamieszkania'}),
            'code': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Kod pocztowy format XX-XXX'}),
            'city': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Podaj miejsce zamieszkania'}),
        }