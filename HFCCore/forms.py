from django import forms
from .models import Community_Member
from ScreeningApp.models import *

EXPERIENCE=(
    ('No Experience', 'No Experience'),
    ('1+ years', '1+ years'),
    ('2+ years','2+ years'),
    ('3+ years','3+ years'),
    ('5+ years','5+ years'),
    ('10+ years','10+ years'),
    ('15+ years','15+ years'),
    ('20+ years','20+ years'),
)

class Mentor_form(forms.ModelForm):
    field_order=['name','email','contact_number','dob','gender','highest_education','coder_profile','current_occupation',
        'years_of_experience','profession','area_of_expertise']
    class Meta:
    	model  = Community_Member
    	exclude=('level_of_expertise','organization')
    def __init__(self, *args, **kwargs) :
    	super().__init__(*args, **kwargs)
    	self.fields['gender'].widget=forms.RadioSelect(choices=GENDER)
    	self.fields['highest_education'].widget=forms.RadioSelect(choices=EDUCATION)
    	self.fields['years_of_experience'].widget=forms.RadioSelect(choices=EXPERIENCE)
    	self.fields['area_of_expertise'].widget = forms.CheckboxSelectMultiple()
    	self.fields['area_of_expertise'].queryset=Expertise.objects.none()
    	if 'profession' in self.data:
    		try:
    			expertise_area_id = int(self.data.get('profession'))
    			self.fields['area_of_expertise'].queryset =Expertise.objects.filter(category_of_expertise=expertise_area_id)
    		except (ValueError, TypeError):
    			pass
    	elif self.instance.pk:
    		self.fields['area_of_expertise'].queryset = self.instance.expertise_area.expertise_set
