from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def main_index(request):
    return render(request,"main_index.html")


def log(request):
    return render(request,"login.html")


def login_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    data = login.objects.filter(username=username,password=password)
    if data.exists():
        data = data[0]
        request.session['lid'] = data.id
        if data.usertype == 'admin':
            return HttpResponse("<script>alert('Login Success');window.location='/admin_home'</script>")
        elif data.usertype == 'user':
            return HttpResponse("<script>alert('Login Success');window.location='/user_home'</script>")
        else:
            return HttpResponse("<script>alert('Invalid Authentication');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('Not Found');window.location='/'</script>")


def admin_home(request):
    category_count = category.objects.all().count()
    request.session['category_count'] = category_count
    request.session['tutor_count'] = tutor.objects.all().count()
    request.session['batch_count'] = batch.objects.all().count()
    request.session['ornament_count'] = ornaments_and_costume.objects.all().count()
    return render(request,"admin/admin_index.html")


def user_home(request):
    category_count = category.objects.all().count()
    request.session['category_count'] = category_count
    request.session['tutor_count'] = tutor.objects.all().count()
    request.session['batch_count'] = batch.objects.all().count()
    request.session['ornament_count'] = ornaments_and_costume.objects.all().count()
    return render(request,"user/new_user_index.html")

def logout(request):
    return HttpResponse("<script>alert('Logout Success');window.location='/'</script>")


# ========================================= ADMIN ======================================================


# -- category management


def admin_add_category(request):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")

    return render(request,"admin/add_category.html")


def admin_add_category_post(request):
    name = request.POST['textfield']
    icon = request.FILES['fileField']
    import datetime
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs = FileSystemStorage()
    fs.save(r"C:\Users\OneTeam\Downloads\Kalakendra-main\Kalakendra-main\myapp\static\icon\\"+dt+'.jpg',icon)
    path = '/static/icon/'+dt+'.jpg'
    data = category.objects.filter(name=name,image=path)
    if data.exists():
        return HttpResponse("<script>alert('Already Added..Try another ');window.location='/admin_add_category#aaa'</script>")
    else:
        obj = category()
        obj.name = name
        obj.image = path
        obj.save()
        return HttpResponse("<script>alert('Successfully Added ');window.location='/admin_add_category#aaa'</script>")

def admin_view_category(request):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    data = category.objects.all().order_by('-id')
    return render(request,"admin/view_category.html",{"data":data})


def admin_delete_category(request):
    category.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Removed');window.location='/admin_view_category#aaa'</script>")


# --- Tutor management


def admin_add_tutor(request):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    return render(request,"admin/add_tutor.html")

def admin_add_tutor_post(request):
    name = request.POST['textfield']
    email = request.POST['textfield2']
    contact = request.POST['textfield3']
    image = request.FILES['fileField']
    import datetime
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs = FileSystemStorage()
    fs.save(r"C:\Users\OneTeam\Downloads\Kalakendra-main\Kalakendra-main\myapp\static\tutor\\" + dt + '.jpg', image)
    path = '/static/tutor/' + dt + '.jpg'
    place = request.POST['textfield4']
    landmark = request.POST['textfield5']

    data = tutor.objects.filter(email=email,image=path)
    if data.exists():
        return HttpResponse("<script>alert('Already Added ');window.location='/admin_add_tutor#aaa'</script>")
    else:
        obj = tutor()
        obj.name = name
        obj.email = email
        obj.contact = contact
        obj.place = place
        obj.image = path
        obj.landmark = landmark
        obj.save()
        return HttpResponse("<script>alert('Success');window.location='/admin_add_tutor#aaa'</script>")

def admin_view_tutors(request):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    res = tutor.objects.all().order_by('-id')
    return render(request,"admin/view_tutor.html",{"res":res})


def admin_edit_tutor(request,id):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    tutors = tutor.objects.get(id=id)
    return render(request,"admin/edit_tutor.html",{"tutors":tutors,"id":id})

def admin_edit_tutor_post(request,id):
    try:
        name = request.POST['textfield']
        email = request.POST['textfield2']
        contact = request.POST['textfield3']
        image = request.FILES['fileField']
        import datetime
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\OneTeam\Downloads\Kalakendra-main\Kalakendra-main\myapp\static\tutor\\" + dt + '.jpg', image)
        path = '/static/tutor/' + dt + '.jpg'
        place = request.POST['textfield4']
        landmark = request.POST['textfield5']
        tutor.objects.filter(id=id).update(name=name,email=email,contact=contact,image=path,place=place,landmark=landmark)
        return HttpResponse("<script>alert('Updated');window.location='/admin_view_tutors#aaa'</script>")
    except Exception as e:
        name = request.POST['textfield']
        email = request.POST['textfield2']
        contact = request.POST['textfield3']

        place = request.POST['textfield4']
        landmark = request.POST['textfield5']
        tutor.objects.filter(id=id).update(name=name, email=email, contact=contact,place=place,
                                           landmark=landmark)
        return HttpResponse("<script>alert('Updated');window.location='/admin_view_tutors#aaa'</script>")

def admin_remove_tutor(request,id):
    tutor.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Removed');window.location='/admin_view_tutors#aaa'</script>")



def admin_view_user(request):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    users = user.objects.all().order_by('-id')
    return render(request,"admin/view_user.html",{"users":users})



def admin_view_tutor_request(request,id):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    res4 = tutor_request.objects.filter(TUTOR_id=id,status='pending')
    return render(request,"admin/view_tutor_request.html",{"res4":res4})


def accept_request(request,id):
    tutor_request.objects.filter(id=id).update(status='approved')
    return HttpResponse("<script>alert('Accepted');window.location='/admin_view_tutor_request/"+id+"#aaa'</script>")


def reject_request(request,id):
    tutor_request.objects.filter(id=id).update(status='rejected')
    return HttpResponse("<script>alert('Rejected');window.location='/admin_view_tutor_request/"+id+"#aaa'</script>")



# --- batch Management

def admin_add_batch(request):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    return render(request,"admin/add_batch.html")


def admin_add_batch_post(request):
    name = request.POST['textfield']
    description = request.POST['textarea']
    total_count = request.POST['textfield2']
    date = request.POST['textfield3']
    time = request.POST['textfield4']
    amount = request.POST['textfield5']

    data = batch.objects.filter(name=name,total_count=total_count,description=description)
    if data.exists():
        return HttpResponse("<script>alert('Already Added');window.location='/admin_add_batch#aaa'</script>")
    else:
        obj = batch()
        obj.name = name
        obj.description = description
        obj.total_count = total_count
        obj.date = date
        obj.time = time
        obj.amount = amount
        obj.save()
        return HttpResponse("<script>alert('Success');window.location='/admin_add_batch#aaa'</script>")

def admin_view_batch(request):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    data1 = batch.objects.all().order_by('-id')
    return render(request,"admin/view_batch.html",{"data1":data1})

def admin_edit_batch(request,id):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    batchs = batch.objects.get(id=id)
    return render(request,"admin/update_batch.html",{"batchs":batchs,"id":id})

def admin_edit_batch_post(request,id):
    name = request.POST['textfield']
    description = request.POST['textarea']
    total_count = request.POST['textfield2']
    date = request.POST['textfield3']
    time = request.POST['textfield4']
    amount = request.POST['textfield5']
    batch.objects.filter(id=id).update(name=name,description=description,total_count=total_count,date=date,time=time,amount=amount)
    return HttpResponse("<script>alert('Updated');window.location='/admin_view_batch#aaa'</script>")


def admin_remove_batch(request,id):
    batch.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Removed');window.location='/admin_view_batch#aaa'</script>")




# --- ornamnet and costume management


def admin_add_ornament_costume(request,id):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    return render(request,"admin/add_ornament_and_costume.html",{"id":id})

def admin_add_ornament_costume_post(request,id):
    name = request.POST['textfield']
    gender = request.POST['RadioGroup1']
    image = request.FILES['fileField']
    import datetime
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs = FileSystemStorage()
    fs.save(r"C:\Users\OneTeam\Downloads\Kalakendra-main\Kalakendra-main\myapp\static\ornament_costume\\" + dt + '.jpg', image)
    path = '/static/ornament_costume/' + dt + '.jpg'
    amount = request.POST['textfield2']
    quantity = request.POST['textfield3']
    details = request.POST['textarea']
    data = ornaments_and_costume.objects.filter(name=name,image=path)
    if data.exists():
        return HttpResponse("<script>alert('Already Exists');window.location='/admin_add_ornament_costume/"+id+"#aaa'</script>")
    else:
        obj = ornaments_and_costume()
        obj.name = name
        obj.image = path
        obj.amount = amount
        obj.quantity = quantity
        obj.gender = gender
        obj.details = details
        obj.CATEGORY_id = id
        obj.save()
        return HttpResponse("<script>alert('Success');window.location='/admin_add_ornament_costume/"+id+"#aaa'</script>")

def admin_view_ornaments_and_costume(request,id):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    res2 = ornaments_and_costume.objects.filter(CATEGORY_id=id).order_by('-id')
    return render(request,"admin/view_ornament_and_costume.html",{"res2":res2})



def admin_edit_ornaments_and_costume(request,id):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    ornaments = ornaments_and_costume.objects.get(id=id)
    return render(request,"admin/edit_ornament_and_costume.html",{"ornaments":ornaments,"id":id})

def admin_edit_ornaments_and_costume_post(request,id):
    try:
        name = request.POST['textfield']
        gender = request.POST['RadioGroup1']
        image = request.FILES['fileField']
        import datetime
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\OneTeam\Downloads\Kalakendra-main\Kalakendra-main\myapp\static\ornament_costume\\" + dt + '.jpg', image)
        path = '/static/ornament_costume/' + dt + '.jpg'
        amount = request.POST['textfield2']
        quantity = request.POST['textfield3']
        details = request.POST['textarea']
        ornaments_and_costume.objects.filter(id=id).update(name=name,image=path,details=details,gender=gender,amount=amount,quantity=quantity)
        return HttpResponse("<script>alert('Success');window.location='/admin_view_ornaments_and_costume/"+id+"#aaa'</script>")
    except Exception as e:
        name = request.POST['textfield']
        gender = request.POST['RadioGroup1']

        amount = request.POST['textfield2']
        quantity = request.POST['textfield3']
        details = request.POST['textarea']
        ornaments_and_costume.objects.filter(id=id).update(name=name, details=details, gender=gender,
                                                           amount=amount, quantity=quantity)
        return HttpResponse("<script>alert('Success');window.location='/admin_view_ornaments_and_costume/"+id+"#aaa'</script>")

def admin_remove_ornaments_and_costume(request,id):
    ornaments_and_costume.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Removed');window.location='/admin_view_ornaments_and_costume#aaa'</script>")


def admin_view_booking(request):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    res6 = costume_and_ornaments_booking.objects.filter(status='pending')
    return render(request,"admin/view_booking.html",{"res6":res6})


def update_return_status(request,id):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    return render(request,"admin/update_status.html",{"id":id})

def update_return_status_post(request,id):
    statuss = request.POST['select']
    costume_and_ornaments_booking.objects.filter(id=id).update(status=statuss)
    return HttpResponse("<script>alert('Updated');window.location='/admin_view_booking#aaa'</script>")


def admin_allocate_tutor(request,id):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    res1 = batch.objects.all()
    return render(request,"admin/allocate_tutor.html",{"id":id,"res1":res1})

def admin_allocate_tutor_post(request,id):
    batches = request.POST['select']
    data = allocate_tutor_to_batch.objects.filter(TUTOR_id = id,BATCH_id = batches)
    if data.exists():
        return HttpResponse("<script>alert('Already Allocated');window.location='/admin_allocate_tutor/"+id+"#aaa'</script>")
    else:

        obj = allocate_tutor_to_batch()
        obj.TUTOR_id = id
        obj.BATCH_id = batches
        obj.save()
        return HttpResponse("<script>alert('Updated');window.location='/admin_view_tutors#aaa'</script>")


def admin_view_feedback(request):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    data = feedback.objects.all().order_by('-id')
    return render(request,"admin/view_feedback.html",{"data":data})





# ================ User =====================


def user_register(request):
    return render(request,"user/user_register.html")

def user_register_post(request):
    name = request.POST['textfield']
    email = request.POST['textfield2']
    contact = request.POST['textfield3']
    image = request.FILES['fileField']
    import datetime
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs = FileSystemStorage()
    fs.save(r"C:\Users\OneTeam\Downloads\Kalakendra-main\Kalakendra-main\myapp\static\users\\" + dt + '.jpg', image)
    path = '/static/users/' + dt + '.jpg'
    place = request.POST['textfield4']
    landmark = request.POST['textfield5']
    password = request.POST['password']
    ConfirmPassword = request.POST['ConfirmPassword']

    data = login.objects.filter(username=email)
    if data.exists():
        return HttpResponse("<script>alert('Already Exists');window.location='/user_register#aaa'</script>")
    elif password == ConfirmPassword:
        obj = login()
        obj.username = email
        obj.password = password
        obj.usertype = 'user'
        obj.save()

        obj1 = user()
        obj1.name = name
        obj1.email = email
        obj1.contact = contact
        obj1.place = place
        obj1.landmark = landmark
        obj1.image = path
        obj1.LOGIN = obj
        obj1.save()
        return HttpResponse("<script>alert('Success');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('Password Mismatch');history.back()</script>")


def manage_profile(request):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    res3 = user.objects.get(LOGIN=request.session['lid'])
    return render(request,"user/manage_profile.html",{"res3":res3})

def manage_profile_post(request):
    try:
        name = request.POST['textfield']
        email = request.POST['textfield2']
        contact = request.POST['textfield3']
        image = request.FILES['fileField']
        import datetime
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\OneTeam\Downloads\Kalakendra-main\Kalakendra-main\myapp\static\users\\" + dt + '.jpg', image)
        path = '/static/users/' + dt + '.jpg'
        place = request.POST['textfield4']
        landmark = request.POST['textfield5']
        user.objects.filter(LOGIN=request.session['lid']).update(name=name,email=email,contact=contact,image=path,place=place,landmark=landmark)
        return HttpResponse("<script>alert('Profile Updated');window.location='/manage_profile#aaa'</script>")
    except Exception as e:
        name = request.POST['textfield']
        email = request.POST['textfield2']
        contact = request.POST['textfield3']

        place = request.POST['textfield4']
        landmark = request.POST['textfield5']
        user.objects.filter(LOGIN=request.session['lid']).update(name=name, email=email, contact=contact,
                                                                 place=place, landmark=landmark)
        return HttpResponse("<script>alert('Profile Updated');window.location='/manage_profile#aaa'</script>")



def user_view_allocated_tutor(request):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    res4 = allocate_tutor_to_batch.objects.all()
    return render(request, "user/view_allocated_tutor.html",{"res4":res4})


def user_send_request(request,id):
    import datetime
    data = tutor_request.objects.filter(date = datetime.datetime.now().date(),TUTOR_id = id,USER = user.objects.get(LOGIN=request.session['lid']))
    if data.exists():
        return HttpResponse("<script>alert('Already Requested');window.location='/user_view_allocated_tutor#aaa'</script>")
    else:

        obj = tutor_request()
        obj.date = datetime.datetime.now().date()
        obj.status = 'pending'
        obj.payment_date = 'pending'
        obj.payment_status = 'pending'
        obj.TUTOR_id = id
        obj.USER = user.objects.get(LOGIN=request.session['lid'])
        obj.save()
        return HttpResponse("<script>alert('Requested');window.location='/user_view_allocated_tutor#aaa'</script>")


def user_view_verified_request(request):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    data = tutor_request.objects.filter(USER__LOGIN=request.session['lid'],status='approved')
    return render(request,"user/view_verified_tutor_request.html",{"data":data})


def user_make_tutor_payment(request,id):
    t_request = tutor_request.objects.get(id=id)
    tutor_obj = t_request.TUTOR

    allocations = allocate_tutor_to_batch.objects.filter(TUTOR=tutor_obj)
    # data = allocations[0].BATCH.amount
    import razorpay

    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    amount = float(allocations[0].BATCH.amount) * 100
    # amount = float(amount)

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    # context = {
    #     'razorpay_api_key': razorpay_api_key,
    #     'amount': order_data['amount'],
    #     'currency': order_data['currency'],
    #     'order_id': order['id'],
    #     'rid': rid
    # }

    return render(request, 'User/UserPayProceed.html', {'razorpay_api_key': razorpay_api_key,
                                                        'amount': order_data['amount'],
                                                        'currency': order_data['currency'],
                                                        'order_id': order['id'],
                                                        'rid': id
                                                        })


def on_payment_success(request,id):
    import datetime
    dt = datetime.datetime.now().date()
    tutor_request.objects.filter(id=id).update(payment_status='online',payment_date=dt,status='paid')
    return HttpResponse("<script>alert('Success!');window.location='/user_view_verified_request'</script>")





# ---- ornament booking cart --

def get_ornaments_by_category(request, cat_id):
    ornaments = ornaments_and_costume.objects.filter(CATEGORY_id=cat_id)
    data = [{"id": o.id, "name": o.name} for o in ornaments]
    return JsonResponse(data, safe=False)


def user_book_ornament_and_costume(request):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    res1 = category.objects.all()

    return render(request,"user/costume_and_ornament_booking.html",{"res1":res1})


def user_book_ornament_and_costume_post(request):
    import datetime
    cate = request.POST['category']
    Quantity = request.POST['Quantity']
    ornaments = request.POST['ornament']
    from_date = request.POST['from_day']
    to_date = request.POST['to_day']

    # Convert dates
    from_date_obj = datetime.datetime.strptime(from_date, "%Y-%m-%d").date()
    to_date_obj = datetime.datetime.strptime(to_date, "%Y-%m-%d").date()
    date_diff = (to_date_obj - from_date_obj).days + 1

    # Get ornament/costume details
    ornament_obj = ornaments_and_costume.objects.get(id=ornaments)
    ornament_amount = int(ornament_obj.amount)

    # Calculate total amount
    total_amount = int(Quantity) * int(ornament_amount / 3) * date_diff

    # Create booking entry
    obj = costume_and_ornaments_booking()
    obj.date = datetime.datetime.now().date()
    obj.status = 'pending'
    obj.USER = user.objects.get(LOGIN=request.session['lid'])
    obj.from_day = from_date
    obj.to_day = to_date
    obj.payment_status = 'pending'
    obj.payment_date = 'pending'
    obj.ORNAMENTS_AND_COSTUME_id = ornaments
    obj.total_amount = total_amount
    obj.save()

    # Check available stock
    if int(ornament_obj.quantity) > 0:
        # Check if the same ornament already exists in cart
        res = cart.objects.filter(USER__LOGIN=request.session['lid'], ORNAMENTS_AND_COSTUME_id=ornaments)

        if res.exists():
            qn = res[0].quantity
            quanti = int(qn) + int(Quantity)
            cart.objects.filter(USER__LOGIN=request.session['lid'], ORNAMENTS_AND_COSTUME_id=ornaments).update(quantity=quanti)
        else:
            obj1 = cart()
            obj1.ORNAMENTS_AND_COSTUME_id = ornaments
            obj1.USER = user.objects.get(LOGIN=request.session['lid'])
            obj1.quantity = Quantity
            obj1.save()

        return HttpResponse("<script>alert('Success!');window.location='/user_view_cart#aaa'</script>")
    else:
        return HttpResponse("<script>alert('No available stock found!');window.location='/user_book_ornament_and_costume#aaa'</script>")


def user_view_cart(request):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    data = cart.objects.filter(USER__LOGIN=request.session['lid'])
    cart_items = cart.objects.filter(USER__LOGIN=request.session['lid'])

    total = sum(float(item.ORNAMENTS_AND_COSTUME.amount) * int(item.quantity) for item in cart_items)

    return render(request,"user/view_cart.html",{"data":data,"total":total})


def cancel_cart(request,id):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    cart.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Removed!');window.location='/user_view_cart#aaa'</script>")


def user_place_order(request):
    user_obj = user.objects.get(LOGIN=request.session['lid'])

    cart_items = cart.objects.filter(USER=user_obj)

    if not cart_items.exists():
        return HttpResponse("<script>alert('Cart is empty');window.location='/user_view_cart#aaa'</script>")

    import datetime
    obj = order_tb()
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")  # Changed to match your CharField
    obj.status = "pending"
    obj.amount = "0"
    obj.USER = user_obj
    obj.payment_date = 'pending'
    obj.payment_status = 'pending'
    obj.save()

    total_amount = 0

    for item in cart_items:
        ornament_costume = item.ORNAMENTS_AND_COSTUME

        # if int(item.quantity) > int(ornament_costume.quantity):
        #     obj.delete()
        #     return HttpResponse(f"<script>alert('Insufficient quantity for {ornament_costume.name}');window.location='/user_view_cart#aaa'</script>")

        subtotal = float(item.quantity) * float(ornament_costume.amount)
        total_amount += subtotal

        print("total_amount",total_amount)

        obj1 = order_sub()
        obj1.quantity = item.quantity
        obj1.ORNAMENTS_AND_COSTUME = ornament_costume
        obj1.ORDER = obj
        obj1.save()

        new_quantity = int(ornament_costume.quantity) - int(item.quantity)
        ornaments_and_costume.objects.filter(id=ornament_costume.id).update(quantity=str(new_quantity))

    order_tb.objects.filter(id=obj.id).update(amount=str(total_amount))

    cart.objects.filter(USER=user_obj).delete()
    order_id = obj.id

    return redirect(f'/user_payment_mode/{order_id}#aaa')


def user_payment_mode(request,order_id):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = order_tb.objects.get(id=order_id)
    request.session['orginalamount'] = data.amount
    request.session['requestid'] = order_id
    return render(request,"user/payment_mode.html",{"rid":order_id})




def user_costume_and_ornament_pay(request,rid):
    mode = request.POST['RadioGroup1']
    data1 = order_tb.objects.filter(id=rid)
    if mode == 'offline':
        import datetime
        data1.update(payment_status=mode,payment_date = datetime.datetime.now().date())
        return HttpResponse("<script>alert('Offline Payment');window.location='/user_view_cart#aaa'</script>")
    else:
        import razorpay

        razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
        razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

        razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

        amount = float(data1[0].amount) * 100
        print("amount",amount)
        # amount = float(amount)

        # Create a Razorpay order (you need to implement this based on your logic)
        order_data = {
            'amount': amount,
            'currency': 'INR',
            'receipt': 'order_rcptid_11',
            'payment_capture': '1',  # Auto-capture payment
        }

        # Create an order
        order = razorpay_client.order.create(data=order_data)

        # context = {
        #     'razorpay_api_key': razorpay_api_key,
        #     'amount': order_data['amount'],
        #     'currency': order_data['currency'],
        #     'order_id': order['id'],
        #     'rid': rid
        # }

        return render(request, 'user/costume_and_ornament_pay.html', {'razorpay_api_key': razorpay_api_key,
                                                            'amount': order_data['amount'],
                                                            'currency': order_data['currency'],
                                                            'order_id': order['id'],
                                                            'rid': rid
        })


def costume_and_ornament_pay(request,id):
    import datetime
    dt = datetime.datetime.now().date()
    order_tb.objects.filter(id=id).update(payment_status='online',payment_date=dt,status='paid')
    return HttpResponse("<script>alert('Success!');window.location='/user_view_cart#aaa'</script>")



def user_send_feedback(request):
    if 'lid' not in request.session:
        return HttpResponse("<script>alert('Session Expired..Login Again');window.location='/'</script>")
    return render(request,"user/send_feedback.html")


def user_send_feedback_post(request):
    import datetime
    feedbacks = request.POST['textarea']
    obj = feedback()
    obj.feedbacks = feedbacks
    obj.date = datetime.datetime.now().date()
    obj.USER = user.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse("<script>alert('Success!');window.location='/user_send_feedback#aaa'</script>")


