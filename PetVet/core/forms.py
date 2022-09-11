from django import forms
from .models import PhysicalExam
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div


class PhysicalExamForm(forms.ModelForm):
    class Meta:
        model = PhysicalExam
        fields = ['medical_care', 'diag_differ', 'diag_final']

    def __init__(self, *args, **kwargs):
        super(PhysicalExamForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_physical_exam_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Div('medical_care', css_class='col-md-6'),
                Div('diag_differ', 'diag_final', css_class='col-md-6'), css_class='row'
            ),
            Div(
                Div(Submit('save', 'Save'), css_class='col-md-12'), css_class='row'
            )
        )
