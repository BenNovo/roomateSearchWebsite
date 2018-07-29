from django import forms

class sendMessageForm(forms.Form):
	message = forms.CharField(label="Enter a Message ")
	#Method to clean the message data
	
