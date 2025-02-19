from django.contrib.auth.forms import UserCreationForm

from catalog.forms import ProductForms
from users.models import User


class UserRegisterForm(ProductForms, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')