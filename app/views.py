



## for user creation or register, sign-in and sign-out.
from django.shortcuts import render, redirect
from app.forms import CreateUserForm 

from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required 



def register(request):	
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Your Account has been created for '+ user)
			return redirect('app:login_reg')


	context = { 'form': form }
	return render (request, 'signin/register.html', context)


def login_reg(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('app:index')
		else:
			messages.info(request, "Username Or password is incorrect.")


	context = {}
	return render (request, 'signin/login.html', context)

def logoutuser(request):
	logout(request)
	# return redirect('app:login_reg')
	return redirect('app:home')


@login_required(login_url = 'app:login_reg')
def index(request):
	return render (request,"signin/index.html", context = {})




from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def product(request):
    return render(request, 'product.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def aboutus(request):
    return render(request, 'aboutus.html')



from app.models import Student

	
#Class based views


from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

class StudentReg(CreateView):
	model = Student
	fields = '__all__'
	template_name = 'CBV/studentreg.html'
	success_url ="/"

class Studentlist(ListView):
	model = Student
	template_name = 'CBV/studentlist.html'

class Studentdetail(DetailView):
	model =Student
	template_name = 'CBV/studentdetail.html'

class StudentUpdate(UpdateView):
	model = Student
	fields = "__all__"
	template_name = 'CBV/studentupdate.html'
	success_url ="/"


class StudentDelete(DeleteView):
	model = Student
	template_name = 'CBV/studentdelete.html'
	success_url ="/"



# for get and post

def dhana(request):
	return render(request,'formmet/dhana.html')

def get1(request):
	a = int(request.GET['num1'])
	b = int(request.GET['num2'])
	c = a+b
	context = {'c': c }
	return render(request,'formmet/get.html',context)

def post1(request):
	a = int(request.POST['num1'])
	b = int(request.POST['num2'])
	c = a+b
	context = {'c': c }
	return render(request,'formmet/post.html',context)

	#### For Function based view

from django.shortcuts import render , redirect, get_object_or_404

from .models import Student
from .forms import StudentForm

### for studentlistview
def students(request):
    student = Student.objects.all()
    context = {'student':student}
    return render(request, 'student.html', context)

## for detail view
def detail(request, id):
	data = Student.objects.get(id = id)	
	context = {'data':data}
	return render(request,'FBV/detail.html', context)

##for update view
def update(request, id):
	obj = get_object_or_404(Student, id =id)
	form = StudentForm(request.POST or None, instance = obj)
	data = Student.objects.get(id = id)
	if form.is_valid():
		form.save()
		return redirect('app:students')

	context = {'form':form, 'data':data}
	return render(request,'FBV/update.html', context )

## for delete view
def delete(request, id):
	data = Student.objects.get(id = id)
	context = {'data':data}
	if request.method =='POST':
		data.delete()
		return redirect('app:form')
	return render(request,'FBV/delete.html', context )

## for student list and create or registration
def form(request):
    stu = Student.objects.all() 

    form = StudentForm
    if request.method =="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:students')  

    context = {'stu': stu, 'form': form}
    return render(request, 'FBV/form.html', context) 





from django.shortcuts import render

# Create your views here.
def categories(request):
    return render(request, 'categories.html')

def base(request):
    return render(request, 'base.html')

def base1(request):
    return render(request, 'base1.html')

def contact(request):
    return render(request, 'contact.html')

def community(request):
    return render(request, 'community.html')

def index(request):
    return render(request, 'index.html')

def review(request):
    return render(request, 'review.html')

def single_blog(request):
    return render(request, 'single_blog.html')


from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def product(request):
    return render(request, 'product.html')

def products(request):
    return render(request, 'products.html')

def image(request):
    return render(request, 'image.html')

def images(request):
    return render(request, 'images.html')

def kart(request):
    return render(request, 'kart.html')

def order(request):
    return render(request, 'order.html')



from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'imageapp\home.html')

# from imageapp.forms import UserImageForm    
# from .models import UploadImage  


# def image(request):  
#     if request.method == 'POST':  
#         form = UserImageForm(request.POST, request.FILES)  
#         if form.is_valid():  
#             form.save()  
#             img_object = form.instance                
#             return render(request, 'image_form.html', {'form': form, 'img_obj': img_object})  
#     else:  
#         form = UserImageForm()  

#     return render(request, 'imageapp\imageupload.html', {'form': form}) 
#
# for uploading images. 

from django.shortcuts import render
from .forms import ImageForm
from .models import Image


def image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'imageapp\image.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'imageapp\image.html', {'form': form})

def images(request):
    all_images=Image.objects.all()
    context={'all_images':all_images}
    return render(request, 'imageapp\images.html', context)


from .forms import ProductForm, OrderForm
from .models import Product


def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'imageapp\product.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ProductForm()
    return render(request, 'imageapp\product.html', {'form': form})

def products(request):
    all_products=Product.objects.all()
    context={'all_products':all_products}
    return render(request, 'imageapp\products.html', context)

def order(request, id):
    obj = get_object_or_404(Product, id =id)
    form = OrderForm(request.POST or None, instance = obj)
    data = Product.objects.get(id = id)
    if form.is_valid():
        form.save()
        return redirect('products')
    context = {'form':form, 'data':data}
    return render(request, 'imageapp/order.html', context)

def kart(request):
    Ordered_items = Product.objects.filter(order_status = True)
    print("Ordered Items :", Ordered_items)
    price = Product.objects.values('price')[0]
    total = 0
    total_value = 0
    for price in Ordered_items:
        print(price.price)
        print(price.items)
        total = price.price*price.items
        total_value = total_value+total
        print(total)

    print(total_value)
    context = {'Ordered_items':Ordered_items, 'total':total_value}
    return render(request, 'imageapp/kart.html', context)

