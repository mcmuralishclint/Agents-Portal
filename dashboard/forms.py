from django import forms
from dashboard.models import Scholarship

class ScholarshipEditForm(forms.ModelForm):
	class Meta:
		model = Scholarship
		fields = ['university', 'tuition_after_schol', 'accomodation_after_schol', 'stipend', 'schol_type', 'service_charge']