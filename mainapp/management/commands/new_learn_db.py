# import PrettyTable as PrettyTable
from django.db.models import F, When, Case, DecimalField, IntegerField, Q
from datetime import timedelta

from ordersapp.models import OrderItem

...
ACTION_1 = 1
ACTION_2 = 2
ACTION_EXPIRED = 3

action_1__time_delta = timedelta(hours=12)
action_2__time_delta = timedelta(days=1)

action_1__discount = 0.3
action_2__discount = 0.15
action_expired__discount = 0.05

action_1__condition = Q(order__updated__lte=F('order__created') +\
                                            action_1__time_delta)

action_2__condition = Q(order__updated__gt=F('order__created') +\
                                           action_1__time_delta) &\
                      Q(order__updated__lte=F('order__created') +\
                                            action_2__time_delta)

action_expired__condition = Q(order__updated__gt=F('order__created') +\
                              action_2__time_delta)

action_1__order = When(action_1__condition, then=ACTION_1)
action_2__order = When(action_2__condition, then=ACTION_2)
action_expired__order = When(action_expired__condition, then=ACTION_EXPIRED)

action_1__price = When(action_1__condition,
          then=F('product__price') * F('quantity') * action_1__discount)

action_2__price = When(action_2__condition,
          then=F('product__price') * F('quantity') * -action_2__discount)

action_expired__price = When(action_expired__condition,
          then=F('product__price') * F('quantity') * action_expired__discount)

test_orderss = OrderItem.objects.annotate(
   action_order=Case(
       action_1__order,
       action_2__order,
       action_expired__order,
       output_field=IntegerField(),
   )).annotate(
   total_price=Case(
       action_1__price,
       action_2__price,
       action_expired__price,
       output_field=DecimalField(),
   )).order_by('action_order', 'total_price').select_related()

# t_list = PrettyTable(["Заказ", "Товар", "Скидка", "Разница во времени"])
# t_list.aligh = 'l'
#
# for orderitem in test_orderss:
#     t_list.add_row([f'{orderitem.action_order} звувз № {orderitem.pk:}', f'{orderitem.product.name: 15}',
#                     f'{abs(orderitem.total_price):6.2f} руб.',
#                     orderitem.order.update - orderitem.order.create])
#     print(t_list)


for orderitem in test_orderss:
   print(f'{orderitem.action_order:2}: заказ №{orderitem.pk:3}:\
           {orderitem.product.name:15}: скидка\
           {abs(orderitem.total_price):6.2f} руб. | \
           {orderitem.order.updated - orderitem.order.created}')