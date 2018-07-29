from django import forms

ACTION_CHOICES= [
    ('logout', 'Log Out'),
    ('open chat', 'Open Chatroom'),
    ('change survey', 'Change Survey Answers'),
    ]

QUESTION_CHOICES= [
    ('always','Always'),
    ('most of the time','Most of the Time'),
    ('sometimes', 'Sometimes'),
    ('never', 'Never'),
]

class profileForm(forms.Form):
    action = forms.CharField(label='Action:', widget=forms.RadioSelect(choices=ACTION_CHOICES))
    
    
class changeAnswersForm(forms.Form):
    answer_one = forms.CharField(label='Do you prefer to go to sleep late?',widget=forms.RadioSelect(choices=QUESTION_CHOICES))
    answer_two = forms.CharField(label='Do you prefer to wake up early?',widget=forms.RadioSelect(choices=QUESTION_CHOICES))
    answer_three = forms.CharField(label='Do you prefer to keep your room cold?',widget=forms.RadioSelect(choices=QUESTION_CHOICES))
    answer_four = forms.CharField(label='Do you prefer to go study in your room?',widget=forms.RadioSelect(choices=QUESTION_CHOICES))
    answer_five = forms.CharField(label='Do you prefer to listen to music in the room?',widget=forms.RadioSelect(choices=QUESTION_CHOICES))