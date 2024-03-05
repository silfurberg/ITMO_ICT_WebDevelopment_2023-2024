from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class OwnerCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'passport_number',
            'nationality',
            'address',
            'password1',
            'password2'
        ]