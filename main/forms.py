from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name',
            'required': 'required'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
            'required': 'required'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Enter your message',
            'required': 'required'
        })
    )

class CalculatorForm(forms.Form):
    num1 = forms.FloatField(
        label="First Number",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter first number',
            'step': 'any'
        })
    )
    num2 = forms.FloatField(
        label="Second Number",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter second number',
            'step': 'any'
        })
    )
    operation = forms.ChoiceField(
        choices=[
            ('add', 'Add (+)'),
            ('sub', 'Subtract (-)'),
            ('mul', 'Multiply (*)'),
            ('div', 'Divide (/)')
        ],
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
