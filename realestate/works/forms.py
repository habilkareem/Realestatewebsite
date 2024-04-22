from django import forms
from works.models import UserInquiry,Realtor,Listing

class signinrealtor(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class UserInquiryForm(forms.ModelForm):
    class Meta:
        model = UserInquiry
        fields = ['full_name', 'realtor', 'email', 'phone_number', 'message']


class RealtorForm(forms.ModelForm):
    class Meta:
        model=Realtor
        fields = ['username', 'name', 'photo', 'description', 'phone', 'email', 'is_mvp', 'hire_date', 'password']


class ListingForm(forms.ModelForm):
    class Meta:
        model=Listing
        fields = ['realtor', 'category', 'title', 'address', 'city', 'state', 'zipcode', 'description', 'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'lot_size', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'is_published', 'list_date']