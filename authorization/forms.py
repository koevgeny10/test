from django.contrib.auth.forms import UserCreationForm


class UserCreation_Form(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)  # Добавил почту в регистрацию
