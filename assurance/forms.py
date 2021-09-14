from django import forms 
  
from assurance.models import Produitassurance ,Assureur ,Baremedevoyage, Baremedecredit, Souscriptiondecredit, Souscriptiondevoyage, Beneficiaire
class BuzCustomField(forms.CharField):
    
    def clean(self, value):
        """
        Validates the given value and returns its "cleaned" value as an
        appropriate Python object.

        Raises ValidationError for any errors.
        """
        value = self.to_python(value)
        value = Buz.objects.get(value)
        self.validate(value)
        self.run_validators(value)
        return value

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



class SouscriptioncreditForm(forms.ModelForm):  
   

    class Meta:  
        model = Souscriptiondecredit
        fields = "__all__"          


class SouscriptionvoyageForm(forms.ModelForm):  
    class Meta:  
        model = Souscriptiondevoyage
        fields = "__all__"         


class beneficiaireForm(forms.ModelForm):  
   

    class Meta:  
        model = Beneficiaire
        fields = "__all__"  
