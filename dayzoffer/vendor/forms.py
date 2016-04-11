from django import forms
from .models import Product
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker', 'placeholder': 'Product validity', 'aria-describedby': 'validity'})


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			'name', 
			'offer', 
			'description', 
			'category', 
			'coupon_code',
			'link',
			'image',
			'validity'
		]
		widgets = {
			'validity': DateInput(),
			'name': forms.TextInput(attrs={
				'class': 'form-control', 
				'placeholder': 'Product Name',
				
			}),
			'offer': forms.TextInput(attrs={
				'class': 'form-control', 
				'placeholder': 'Offer Name',
				
			}),
			'description': forms.TextInput(attrs={
				'class': 'form-control', 
				'placeholder': 'Product Description',
			}),
			'category': forms.Select(attrs={
				'class': 'form-control', 
				
			}),
			'coupon_code': forms.TextInput(attrs={
				'class': 'form-control', 
				'placeholder': 'coupon code (optional)',
				
			}),
			'link': forms.TextInput(attrs={
				'class': 'form-control', 
				'placeholder': 'Product or website link',
				
			}),
		}


