from django import forms
from django.forms import ModelForm
from operations.models import ProjectMaterialsEntry


class ProjectMaterialsInLineForm(ModelForm):
    """
    Custom form for inlining materials for a project.
    """
    material_cost = forms.DecimalField(max_digits=10, decimal_places=2, label="Costo", initial=0.0,
                                       widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = ProjectMaterialsEntry
        fields = "__all__"

    class Media:
        js = (
            'finances/scripts/materialCost.js',
            'operations/scripts/projectMaterialsInLineForm.js',
        )
