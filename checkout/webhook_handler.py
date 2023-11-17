from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handle Stripe webhoooks
    """
    def __init__(self, request):
        self.request = request


    def handle_event(self, event):
        """
        Handle a generic/unkwon/unexpected 
        webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)


    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeded webhook 
        from Stripe
        """
        intent = event.data.objects
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)


    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed 
        webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
