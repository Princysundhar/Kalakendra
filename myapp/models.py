from django.db import models

# Create your models here.


class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)


class category(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)


class tutor(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    image = models.CharField(max_length=500)

class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE)


class tutor_request(models.Model):
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    payment_date = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    TUTOR = models.ForeignKey(tutor, on_delete=models.CASCADE)
    USER = models.ForeignKey(user,on_delete=models.CASCADE)


class batch(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    total_count = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)

class allocate_tutor_to_batch(models.Model):
    TUTOR = models.ForeignKey(tutor, on_delete=models.CASCADE)
    BATCH = models.ForeignKey(batch, on_delete=models.CASCADE)


class ornaments_and_costume(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    gender = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    CATEGORY = models.ForeignKey(category, on_delete=models.CASCADE)


# class costume(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.CharField(max_length=200)
#     gender = models.CharField(max_length=100)
#     amount = models.CharField(max_length=100)
#     count = models.CharField(max_length=100)
#     size = models.CharField(max_length=100)


class costume_and_ornaments_booking(models.Model):
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    from_day = models.CharField(max_length=100)
    to_day = models.CharField(max_length=100)
    payment_date = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    total_amount = models.CharField(max_length=100)
    ORNAMENTS_AND_COSTUME = models.ForeignKey(ornaments_and_costume, on_delete=models.CASCADE)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)

class cart(models.Model):
    quantity = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    ORNAMENTS_AND_COSTUME = models.ForeignKey(ornaments_and_costume, on_delete=models.CASCADE)

class order_tb(models.Model):
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    payment_date = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    # ORNAMENTS_AND_COSTUME = models.ForeignKey(ornaments_and_costume, on_delete=models.CASCADE)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)


class order_sub(models.Model):
    quantity = models.CharField(max_length=100)
    ORNAMENTS_AND_COSTUME = models.ForeignKey(ornaments_and_costume, on_delete=models.CASCADE)
    ORDER = models.ForeignKey(order_tb, on_delete=models.CASCADE)


class feedback(models.Model):
    feedbacks = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)




