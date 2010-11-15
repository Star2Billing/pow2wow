# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="areski"
__date__ ="$Feb 18, 2010 7:46:20 PM$"

if __name__ == "__main__":
    print "Hello World"


from django import forms

class InviteForm(forms.Form):
    phonenumber = forms.CharField(max_length=50, label='#')
    

class loginForm(forms.Form):
    user = forms.CharField(max_length=40, label='Login', required=True, widget=forms.TextInput(attrs={'size':'10'}))
    password = forms.CharField(max_length=40, label='password', required=True, widget=forms.PasswordInput(attrs={'size':'10'}))