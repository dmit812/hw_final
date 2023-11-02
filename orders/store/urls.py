from django.urls import path
from django_rest_passwordreset.views import (
    reset_password_request_token,
    reset_password_confirm,
)


from .views import (
    PartnerUpdate,
    RegisterAccount,
    LoginAccount,
    CategoryView,
    ShopView,
    ProductInfoView,
    BasketView,
    AccountDetails,
    ContactView,
    OrderView,
    PartnerState,
    PartnerOrders,
    ConfirmAccount,
)

app_name = "store"
urlpatterns = [
    path("partner/update", PartnerUpdate.as_view(), name="partner_update"),
    path("partner/state", PartnerState.as_view(), name="partner_state"),
    path("partner/orders", PartnerOrders.as_view(), name="partner_orders"),
    path("user/register", RegisterAccount.as_view(), name="user_register"),
    path(
        "user/register/confirm", ConfirmAccount.as_view(), name="user_register_confirm"
    ),
    path("user/details", AccountDetails.as_view(), name="user_details"),
    path("user/contact", ContactView.as_view(), name="user_contact"),
    path("user/login", LoginAccount.as_view(), name="user_login"),
    path("user/password_reset", reset_password_request_token, name="password_reset"),
    path(
        "user/password_reset/confirm",
        reset_password_confirm,
        name="password_reset_confirm",
    ),
    path("categories", CategoryView.as_view(), name="categories"),
    path("shops", ShopView.as_view(), name="shops"),
    path("products", ProductInfoView.as_view(), name="shops"),
    path("basket", BasketView.as_view(), name="basket"),
    path("order", OrderView.as_view(), name="order"),
]
