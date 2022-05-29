"""[apps file]"""
from django.apps import AppConfig
# pylint: disable=unused-import, import-outside-toplevel


class CheckoutConfig(AppConfig):
    """[checkout config]"""
    name = 'checkout'

    def ready(self):
        import checkout.signals # noqa
