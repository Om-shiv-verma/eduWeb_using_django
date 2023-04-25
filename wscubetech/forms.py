from django import forms


class usersForm(forms.Form):
    fname = forms.CharField(label="First Name",widget=forms.TextInput(attrs={'class':"select form-control"}))
    lname = forms.CharField(label="Last Name",widget=forms.TextInput(attrs={'class':"select form-control"}))
    fathname = forms.CharField(label="Father Name",widget=forms.TextInput(attrs={'class':"select form-control"}))
    email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'class':"select form-control"}))