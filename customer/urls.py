from django.urls import path

from customer import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("index",views.LoginView.as_view(),name="login"),
    path("register",views.SignUpView.as_view(),name="register-accoiunt"),
    path("",views.IndexView.as_view(),name="index-camera"),
    path("profile",views.ProfileView.as_view(),name="profile-view"),
    path("camera/details/<int:id>",views.CameraDetailsView.as_view(),name="Camera-details"),
    path("Camer/cart",views.CartView.as_view(),name="Order-cart"),
    path("Camer/add/<int:id>",views.CartAddProductView.as_view(),name="cart"),
    path("product/<int:id>/cancell",views.CartRemoveView.as_view(),name="cancell"),
    path("orders/add/<int:id>",views.MakeOrderView.as_view(),name="created-order"),
    path("orders/all",views.MyOrderView.as_view(),name="my-order"),
    path("orders/<int:id>/change",views.OrderCancelView.as_view(),name="order-cancel"),
    path("product/offer",views.SpecialOfferView.as_view(),name="offer"),
    path("Camer/offer/<int:pk>",views.CartAddOfferView.as_view(),name="cart-offer"),
    path("Special/offer/cart",views.SpecialCartView.as_view(),name="special/cart"),
    path("Offer/<int:id>",views.CartAddOfferView.as_view(),name="Offer/cart"),
    path("orders/Special/offer/<int:id>",views.SpecialOrderView.as_view(),name="special-order"),
    path("Special/order",views.OfferOrderView.as_view(),name="Special/order"),
    path("product/cancell/<int:id>",views.CartCancellView.as_view(),name="Product/Cancell"),
    path("order/product/cancell/<int:id>",views.OderProductCancellView.as_view(),name="order/Cancell"),
    path("camera/serach",views.CamerarSearchView.as_view(),name="camera/sreach"),
    path("biling/section",views.BilingView.as_view(),name="biling"),
    path("signout",views.SignOutView.as_view(),name="remove")
    
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
