from django.urls import path

from eshop_order.views import add_user_order,user_open_order,remove_order_detail

urlpatterns = [
    path("add_user_order", add_user_order),
    path("user-order", user_open_order),
    path("remove-detail/<detail_id>", remove_order_detail),

]
