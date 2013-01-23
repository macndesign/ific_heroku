from django import forms

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
