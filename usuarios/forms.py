from django import forms
from django.core.exceptions import ValidationError

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ex.: João Silva'
            }
        )
    )
    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome Completo',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ex.: João Silva'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com'
            }
        )
    )
    senha_1=forms.CharField(
        label='Senha',
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )
    senha_2=forms.CharField(
        label='Confirmação de Senha',
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Digite novamente sua senha'
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data['nome_cadastro']

        if nome:
            print('batata')
            nome = nome.strip()
            print(nome)
            if ' ' in nome:
                raise ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome
    
    def clean_senha_2(self):
        senha_1 = self.cleaned_data['senha_1']
        senha_2 = self.cleaned_data['senha_2']

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise ValidationError('Senhas não são iguais')
            else:
                return senha_2
