from oscar.apps.checkout.apps import CheckoutConfig as OscarCheckoutConfig

class CheckoutConfig(OscarCheckoutConfig):

    def ready(self):
        super().ready()
        from sandbox.apps.checkout import views
        self.payment_details_view = views.PaymentDetailsView