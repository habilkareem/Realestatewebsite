from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView,TemplateView,FormView,DetailView
from django.shortcuts import get_object_or_404
from works.models import Realtor,Category,UserInquiry,Listing
# from store.forms import Register,log,orderform
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from works.forms import signinrealtor,UserInquiryForm,RealtorForm,ListingForm
from django.contrib.auth.hashers import check_password
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

class home(ListView):
    model=Category
    template_name="works\index.html"
    context_object_name="categories"

class catego(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Listing.objects.filter(category_id=id)
        name=Category.objects.get(id=id)
        return render(request,"works\category_detail.html",{"data":data,"name":name})
    
class productView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Listing.objects.filter(id=id)
        name=Realtor.objects.filter(id=id)
        return render(request,"works\productview.html",{"data":data,"name":name})
    
class about(View):
    def get(self,request,*args,**kwargs):
        return render(request,"works/about.html")
    
class Signup(CreateView):
    form_class=RealtorForm
    template_name="works/Realtor.html"
    model=Realtor
    success_url=reverse_lazy('login')
    


class Signin(View):
    def get(self, request):
        return render(request, 'works\login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Retrieve the Realtor object from the database based on the provided username
        try:
            realtor = Realtor.objects.get(username=username)
        except Realtor.DoesNotExist:
            realtor = None

        if realtor is not None:
            # Check if the provided password matches the password in the database
            if password == realtor.password:
                # Password matches, so log in the realtor
                request.session['logged_in'] = True
                request.session['realtor_id'] = realtor.id
                return redirect('home')  # Redirect to dashboard or any other page
            else:
                # Password does not match
                messages.error(request, 'Invalid password.')
        else:
            # Realtor does not exist
            messages.error(request, 'Realtor does not exist.')

        return redirect('login')
   
    



#     def get(self,request,*args,**kwargs):
#          form=signinrealtor()
#          return render(request,"store/login.html",{"data":form})
    
#     def post(self,request,*args,**kwargs):
#         form=signinrealtor(request.POST)
#         if form.is_valid():
#             u_name=form.cleaned_data.get("username")
#             pwd=form.cleaned_data.get("password")
#             user_obj=authenticate(request,username=u_name,password=pwd)
#             if user_obj:
#                 print("valid")
#                 login(request,user_obj)
#                 return redirect("home")
#             else:
#                 print("invalid")
#             return render(request,"store/login.html",{"data":form})
        
class Signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("home")
   

    
class enquirenow(CreateView):
    template_name="works\enquire.html"
    form_class=UserInquiryForm
    model=UserInquiry
    success_url=reverse_lazy("home")

    def form_valid(self, form):
        # Save the form and get the instance
        self.object = form.save()

        # Customize the email content
        subject = 'enquiry successfull'
        message = 'Hello, Your Enquiry message is successfully done, our realtor will contact you soon'
        from_email = 'habilkareem90@gmail.com'
        to_email = [form.cleaned_data['email']]  # Replace with your recipient email(s)

        # Send email
        send_mail(subject, message, from_email, to_email, fail_silently=False)

        # Redirect to success_url
        return super().form_valid(form)

# class SellerDashboardView(View):
#     def get(self,request,*args,**kwargs):
#         data=UserInquiry.objects.filter(user=request.user)
#         return render(request,"store/cart.html",{"data":data})

# class SellerDashboardView(ListView):
#     template_name = 'works\sellerdetails.html'
#     model = UserInquiry
#     context_object_name = 'enquiries'

#     def get_queryset(self):
#         return UserInquiry.objects.all()



class DashboardView(TemplateView):
    template_name = 'works\sellerdetails.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logged_in'):
            # Redirect to login page if user is not logged in
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        realtor_id = self.request.session.get('realtor_id')
        
        # Query UserInquiry objects for the logged-in realtor
        inquiries = UserInquiry.objects.filter(realtor_id=realtor_id)
        
        # Get the realtor object
        try:
            realtor = Realtor.objects.get(id=realtor_id)
        except Realtor.DoesNotExist:
            realtor = None
        
        context['inquiries'] = inquiries
        context['realtor'] = realtor
        return context
    

class Listingview(CreateView):
    template_name="works/listing.html"
    form_class=ListingForm
    model=Listing
    success_url=reverse_lazy("home")





        
