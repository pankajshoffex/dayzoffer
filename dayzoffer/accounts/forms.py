from django import forms
from .models import UserProfile, SellerUser

class UserRegisterForm(forms.ModelForm):
	full_name = forms.CharField(
		required=True, 
		label ='Full Name', 
		widget=forms.TextInput(attrs={
			'class': 'form-control', 
			'placeholder': 'Full Name', 
			'aria-describedby': 'full_name'}))
	password1 = forms.CharField(widget=forms.PasswordInput(
		attrs={
			'class': 'form-control', 
			'placeholder': 'Password', 
			'aria-describedby': 'password1'
		})
	)
	password2 = forms.CharField(widget=forms.PasswordInput(
		attrs={
			'class': 'form-control', 
			'placeholder': 'Confirm Password', 
			'aria-describedby': 'password2'
		})
	)
	email = forms.CharField(required=True, label='Email',
		widget=forms.EmailInput(
		attrs={
			'class': 'form-control', 
			'placeholder': 'Email Address', 
			'aria-describedby': 'email'
		})
		)
	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
			self.error_messages['password_mismatch'],
			code='password_mismatch',
			)
		return password2

	class Meta:
		model = UserProfile
		fields = [
			"city",
			"location_aria",
			"mobile_no"
		]
		widgets = {
		'location_aria': forms.TextInput(attrs={
			'class': 'form-control', 
			'placeholder': 'Location Area',
			'aria-describedby': 'location_aria'
			}),
		'mobile_no': forms.TextInput(attrs={
			'class': 'form-control', 
			'placeholder': 'Mobile No',
			'aria-describedby': 'mobile_no'
			}),
		'city': forms.Select(attrs={
			'class': 'form-control', 
			'aria-describedby': 'city'
			}),
		}
	def __init__(self, *args, **kwargs):
		super(UserRegisterForm, self).__init__(*args, **kwargs)
		self.fields['city'].empty_label = None


class SellerRegistration(forms.ModelForm):
	email = forms.CharField(required=True, label='Email',
		widget=forms.EmailInput(
		attrs={
			'class': 'form-control', 
			'placeholder': 'Email Address', 
			'aria-describedby': 'email'
		})
		)
	password1 = forms.CharField(widget=forms.PasswordInput(
		attrs={
			'class': 'form-control', 
			'placeholder': 'Password', 
			'aria-describedby': 'password1'
		})
	)
	password2 = forms.CharField(widget=forms.PasswordInput(
		attrs={
			'class': 'form-control', 
			'placeholder': 'Confirm Password', 
			'aria-describedby': 'password2'
		})
	)
	class Meta:
		model = SellerUser
		fields = [
			"firm_name",
			"address",
			"location_aria",
			"country",
			"state",
			"city",
			"pincode",
			"lattitude",
			"longitute",
			"mobile"
		]
		widgets = {
		'firm_name': forms.TextInput(attrs={
			'class': 'form-control', 
			'placeholder': 'Store or Firm Name',
			'aria-describedby': 'firm_name'
			}),
		'address': forms.TextInput(attrs={
			'class': 'form-control', 
			'placeholder': 'Address',
			'aria-describedby': 'address'
			}),
		'location_aria': forms.TextInput(attrs={
			'class': 'form-control', 
			'placeholder': 'Location',
			'aria-describedby': 'location_aria'
			}),
		'pincode': forms.TextInput(attrs={
			'class': 'form-control', 
			'placeholder': 'Pincode',
			'aria-describedby': 'pincode'
			}),
		'lattitude': forms.TextInput(attrs={
			'class': 'form-control', 
			'placeholder': 'Lattitude',
			'aria-describedby': 'lattitude'
			}),
		'longitute': forms.TextInput(attrs={
			'class': 'form-control', 
			'placeholder': 'Longitute',
			'aria-describedby': 'longitute'
			}),
		'mobile': forms.TextInput(attrs={
			'class': 'form-control', 
			'placeholder': 'Mobile No',
			'aria-describedby': 'mobile'
			}),
		'city': forms.Select(attrs={
			'class': 'form-control', 
			'aria-describedby': 'city'
			}),
		'country': forms.Select(attrs={
			'class': 'form-control', 
			'aria-describedby': 'country'
			}),
		'state': forms.Select(attrs={
			'class': 'form-control', 
			'aria-describedby': 'state'
			}),
		}

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
			self.error_messages['password_mismatch'],
			code='password_mismatch',
			)
		return password2

	def __init__(self, *args, **kwargs):
		super(SellerRegistration, self).__init__(*args, **kwargs)
		self.fields['city'].empty_label = None
		self.fields['country'].empty_label = None
		self.fields['state'].empty_label = None



