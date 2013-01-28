from django import forms
from django.core.mail import send_mail

class FaleConoscoForm(forms.Form):
    subject = forms.CharField(
        label=u'Assunto',
        widget=forms.TextInput(attrs={'class': 'input-xlarge'})
    )
    from_email = forms.EmailField(
        label=u'Email',
        widget=forms.TextInput(attrs={'class': 'input-xlarge'})
    )
    message = forms.CharField(
        label=u'Mensagem',
        widget=forms.Textarea(attrs={'class': 'input-xlarge', 'rows': 5})
    )

    def send_mail(self):
        return send_mail(
            self.cleaned_data['subject'],
            self.cleaned_data['message'],
            self.cleaned_data['from_email'],
            ['macndesign@gmail.com'],
            fail_silently=False
        )
