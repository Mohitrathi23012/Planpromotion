from django.apps import AppConfig


class CustomerAndBrandConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer_and_brand'

    def ready(self) -> None:
        import customer_and_brand.signals