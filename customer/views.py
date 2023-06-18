from typing import Any
from django.db import models
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView,ListView,UpdateView,DetailView
from customer.forms import User,RegistrationForm,LoginForm,BillingForm
from cam.models import Camera,Cart,Orders,CameraDetails,SpecialCart,SpecialProduct,SpecialOrders,Billing
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


class SignUpView(CreateView):
    
    model=User
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("login")
    
    
class LoginView(FormView):
    template_name="login.html"
    form_class=LoginForm
    
    def post(self,request,*args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index-camera")
            else:
                return render(request,"login.html",{"form":self.form_class})
        
class IndexView(View):
    def get(self,request,*args, **kwargs):
        qs=Camera.objects.all()
        return render(request,"index.html",{"products":qs})

class ProfileView(TemplateView):
    template_name="profil-view.html"

    
class CameraDetailsView(View):
    def get(self, request,*args, **kwargs):
        id=kwargs.get("id")
        qs=Camera.objects.filter(id=id)
        return render (request,"products.detail.html",{"carts":qs})
    
class CartView(View):
    def get(self,request,*args, **kwargs): 
        qs=Cart.objects.filter(user=request.user,status="in-cart")
        return render(request,"cart.html",{"cart":qs})

class CartAddProductView(View):
    def post(self,request,*args, **kwargs):
        qty=request.POST.get("qty")
        user=request.user
        id=kwargs.get("id")
        product=Camera.objects.get(id=id)
        Cart.objects.create(product=product,user=user,qty=qty)
        messages.success(request,"Hey! product Will be add on Your Cart")
        return redirect("Order-cart")

class CartRemoveView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("id")
        Cart.objects.filter(id=id).update(status="cancelled")
        messages.success(request,"Product Remove Cart")
        return redirect("Order-cart")

class MakeOrderView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("id")
        qs=Cart.objects.get(id=id)
        return render(request,"checkout.html",{"cart":qs})
    def post(self,request,*args, **kwargs):
        user=request.user
        address=request.POST.get("address")
        id=kwargs.get("id")
        cart=Cart.objects.get(id=id)
        product=cart.product
        Orders.objects.create(product=product,user=user,address=address)
        cart.status="Order-placed"
        cart.save()
        messages.success(request," Placed Your Order successfully")
        return redirect("Order-cart")
    
class MyOrderView(View):
    def get(self,request,*args, **kwargs):
        qs=Orders.objects.filter(user=request.user).exclude(status="cancelled")
        return render(request,"order-list.html",{"order":qs})
    
class  OrderCancelView(View):
    def get (self,request,*args, **kwargs):
        id=kwargs.get("id")
        Orders.objects.filter(id=id).update(status="cancelled")
        messages.success(request,"Oder Remove")
        return redirect("my-order")
    
        
    
class SpecialOfferView(CreateView):
    def get(self,request,*args, **kwargs):
        qs=SpecialProduct.objects.all()
        return render(request,"offer.html",{"off":qs})
    
    
class SpecialCartView(View):
    def get(self,request,*args, **kwargs): 
        qs=SpecialCart.objects.filter(user=request.user,status="in-cart")
        return render(request,"Specialcart.html",{"spl":qs})

    
class CartAddOfferView(View):
    def post(self,request,*args, **kwargs):
        qty=request.POST.get("qty")
        user=request.user
        id=kwargs.get("id")
        product=SpecialProduct.objects.get(id=id)
        SpecialCart.objects.create(product=product,user=user,qty=qty)
        messages.success(request,"Hey! Special offer product Will be add on Your Cart successfully")
        return redirect("special/cart")
    
    
class SpecialOrderView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("id")
        qs=SpecialCart.objects.get(id=id)
        return render(request,"checkout.html",{"cart":qs})
    def post(self,request,*args, **kwargs):
        user=request.user
        address=request.POST.get("address")
        id=kwargs.get("id")
        cart=SpecialCart.objects.get(id=id)
        product=cart.product
        SpecialOrders.objects.create(product=product,user=user,address=address)
        cart.status="Order-placed"
        cart.save()
        messages.success(request,"Placed Your Order successfully")
        return redirect("special/cart")
    
class OfferOrderView(View):
    def get(self,request,*args, **kwargs):
        qs=SpecialOrders.objects.filter(user=request.user).exclude(status="cancelled")
        return render(request,"special-order-list.html",{"order":qs})
    
    
class CartCancellView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("id")
        messages.success(request,"Oder Will be Cancelled")
        SpecialCart.objects.filter(id=id).update(status="cancelled")
        return redirect("special/cart")
    
    
class OderProductCancellView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("id")
        messages.success(request,"Special Oder Product Will be Cancelled")
        SpecialOrders.objects.filter(id=id).update(status="cancelled")
        return redirect("offer")
    
    
class CamerarSearchView(ListView,View):
    model=Camera
    template_name="serach.html"
    context_object_name="serach"
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Camera.objects.filter(camera_name__icontains=query).order_by('-camera_name')
    
class SignOutView(View):
    def get(self,request,*args, **kwargs):
        logout(request)
        return redirect("login")


class BilingView(CreateView):
    model=Billing
    form_class=BillingForm
    template_name="checkout.html"