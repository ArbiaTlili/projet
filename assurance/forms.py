from django import forms  
from assurance.models import Produitassurance ,Assureur 
class ProduitassuranceForm(forms.ModelForm):  
   

    class Meta:  
        model = Produitassurance  
        fields = "__all__" 

class AssureurForm(forms.ModelForm):  
   

    class Meta:  
        model = Assureur  
        fields = "__all__" 


