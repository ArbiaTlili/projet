from django import forms  
from assurance.models import Produitassurance  
class ProduitassuranceForm(forms.ModelForm):  
   

    class Meta:  
        model = Produitassurance  
        fields = "__all__" 