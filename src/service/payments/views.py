from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

@api_view(['POST'])
def process_payment(request):
    """
    Procesa pagos con Stripe.
    """
    print("call process_payment")
    print(request.data)
    token = request.data.get('token')
    amount = request.data.get('amount', 0)
    email = request.data.get('email')

    try:
        charge = stripe.Charge.create(
            amount=int(amount),  # Monto en centavos
            currency="eur",
            description="Pago de prueba",
            source=token,
            receipt_email=email
        )
        return Response({"success": True})
    except stripe.error.StripeError as e:
        return Response({"success": False, "error": str(e)}, status=400)
