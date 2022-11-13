from django.forms import ModelForm
from newapp.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["business_name", "business_type",
                  "phone_number", "email", "message"]
