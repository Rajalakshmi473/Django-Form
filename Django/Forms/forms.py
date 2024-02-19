from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=10, required=True)
    pincode = forms.CharField(max_length=6, required=True)

    class Meta:
        model = Contact
        fields = ['username', 'phone_number', 'email', 'address', 'pincode', 'latitude', 'longitude']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise forms.ValidationError("Phone number must be 10 digits.")
        return phone_number

    def clean_pincode(self):
        pincode = self.cleaned_data.get('pincode')
        if not pincode.isdigit() or len(pincode) != 6:
            raise forms.ValidationError("Pincode must be 6 digits.")
        return pincode

class LocationField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        fields = (
            forms.FloatField(max_value=90, min_value=-90),
            forms.FloatField(max_value=180, min_value=-180)
        )
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return f"({data_list[0]}, {data_list[1]})"
        return None
