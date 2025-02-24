
from django.urls import path
from payments.views import process_payment
from items.views import list_items, decrease_stock
from actions.views import block_ip, follow_ip, webdriver_alert, csp_alert, health_check

urlpatterns = [
    path('api/items/list/', list_items),
    path('api/items/decrease-stock/', decrease_stock),
    path('api/payments/process-payment/', process_payment),
    path('api/actions/health-check/', health_check),
    path('api/actions/block/ip/', block_ip),
    path('api/actions/follow/ip/', follow_ip),
    path('api/actions/notify-webdriver-detection/', webdriver_alert),
    path('api/actions/execute/cspalert/', csp_alert),
]
