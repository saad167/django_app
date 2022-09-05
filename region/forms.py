from django.forms import ModelForm
from .models import Region 


class RegionForm(ModelForm):
		class Meta :
			model = Region
			fields = "__all__"




