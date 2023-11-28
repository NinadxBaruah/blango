from django import forms 
from blog.models import Comment
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ["content"] 

  def __int__(self, *args, **kwargs):
    super(CommentForm, self).__int__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.add_input(Submit('submit', 'Submit'))