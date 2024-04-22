from django.urls import path
from works import views 



urlpatterns=[
    path('home/',views.home.as_view(),name="home"),
    path('about/',views.about.as_view(),name="about"),
    path('register/',views.Signup.as_view(),name="reg"),
    # # path('cat/',views.collections.as_view(),name="categories")
    path('prod/<int:pk>',views.catego.as_view(),name="product"),
    path('prodview/<int:pk>',views.productView.as_view(),name="productview"),
    path('login/',views.Signin.as_view(),name="login"),
    path('enquiry/',views.enquirenow.as_view(),name="enquire"),
    path('logout/',views.Signout.as_view(),name="logout"),
    path('dashboard/',views.DashboardView.as_view(),name='dashboard'),
    path('listing/',views.Listingview.as_view(),name='listing'),
    # path('realtor/',views.Realtorview.as_view(),name="realtor"),
    # path('enquiryview/',views.Realtorview.as_view(),name="realtor"),
    # path('search/', views.SearchListingsView.as_view(), name='search_listings'),
]