from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit

from .models import Page

class CreatePageForm(ModelForm):
    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'post'
    helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Page
