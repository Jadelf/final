from	django	import	forms
from	.models	import	Plato,Menu

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields	=	('nombre',	'precio', 'empleado', 'cliente','platos',)
        def __init__(self, *args, **kwargs):
            super(MenuForm,self).__init__(*args,**kwargs)
            self.fields["platos"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["platos"].queryset = Plato.objects.all()
