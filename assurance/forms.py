from django import forms  
from assurance.models import Produitassurance ,Assureur ,Baremedevoyage, Baremedecredit
class ProduitassuranceForm(forms.ModelForm):  

   

    class Meta:  
        model = Produitassurance  
        fields = "__all__" 

class AssureurForm(forms.ModelForm):  
   

    class Meta:  
        model = Assureur  
        fields = "__all__" 


class BaremeassurancevoyageForm(forms.ModelForm):  
   

    class Meta:  
        model = Baremedevoyage
        fields = "__all__" 

class BaremeassurancecreditForm(forms.ModelForm):  
   

    class Meta:  
        model = Baremedecredit
        fields = "__all__"          
