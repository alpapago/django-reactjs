from django.apps import AppConfig


class DirectMessagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "direct_messages"
    # admin 페이지에 보이는 이름 바꾸기
    verbose_name = "Direct Messages"
