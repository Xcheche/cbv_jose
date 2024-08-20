from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Your name",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form",
                "placeholder": "Please enter your name",
                "required": "True",
            }
        ),
    )
    email = forms.EmailField(
        label="Your email",
        widget=forms.TextInput(
            attrs={"class": "form", "placeholder": "Please enter your email"}
        ),
    )
    message = forms.CharField(
        label="Your message",
        widget=forms.Textarea(
            attrs={
                "class": "form",
                "placeholder": "Please enter your message...",
                "rows": 5,
                "cols": 30,
            }
        ),
    )
