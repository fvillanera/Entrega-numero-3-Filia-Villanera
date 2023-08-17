from django import forms

class CursoForm(forms.Form):
    nombre= forms.CharField(max_length=50, required=True)
    comision= forms.IntegerField(required=True)
    duracion= forms.IntegerField(required=True)
    nivel= forms.IntegerField(label="niveles 1-3" , required=True)


class Profesorform (forms.Form):
     nombre= forms.CharField(max_length=50, required=True)
     apellido= forms.CharField(max_length=50, required=True)
     email= forms.EmailField(required=True)
     profesion= forms.CharField(max_length=50, required=True)

class Estudianteform (forms.Form):
     nombre= forms.CharField(max_length=50, required=True)
     apellido= forms.CharField(max_length=50, required=True)
     email= forms.EmailField(required=True)
     