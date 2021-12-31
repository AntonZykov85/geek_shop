window.onload = function () {

    let quantity, price, orderitem_num, delta_quantity, orderitem_quantity, delta_cost;

    let quantity_arr = []
    let price_arr = []
<<<<<<< HEAD
    let total_forms = parseInt($('input[name=orderitems-TOTAL_FORMS]').val())
    // console.log(total_forms)

    let order_total_quantity = parseInt($('.order_total_quantity').text()) || 0;
    let order_total_cost = parseInt($('.order_total_cost').text().replace(',', '.')) || 0;
=======
    let total_forms = parseFloat($('input[name=orderitems-TOTAL_FORMS]').val())
    // console.log(total_forms)

    let order_total_quantity = parseFloat($('.order_total_quantity').text()) || 0;
    let order_total_cost = parseFloat($('.order_total_cost').text().replace(',', '.')) || 0;
>>>>>>> lesson_2_part2

    // console.log(order_total_quantity)
   //  console.log(order_total_cost)

    for (let i = 0; i < total_forms; i++) {
<<<<<<< HEAD
        quantity = parseInt($('input[name=orderitems-' + i + '-quantity]').val())
        price = parseInt($('.orderitems-' + i + '-price').text().replace(',', '.'))
=======
        quantity = parseFloat($('input[name=orderitems-' + i + '-quantity]').val())
        price = parseFloat($('.orderitems-' + i + '-price').text().replace(',', '.'))
>>>>>>> lesson_2_part2

        quantity_arr[i] = quantity;
        if (price) {
            price_arr[i] = price
        } else {
            price_arr[i] = 0;
        }
    }
    console.info('QUANTITY', quantity_arr)
    console.info('PRICE', price_arr)
    //
    //  1 метод (изменение колличества)
    $('.order_form').on('click', 'input[type=number]', function () {

        let target = event.target;
<<<<<<< HEAD
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-quantity', ''));
        if (price_arr[orderitem_num]) {
            orderitem_quantity = parseInt(target.value);
=======
        orderitem_num = parseFloat(target.name.replace('orderitems-', '').replace('-quantity', ''));
        if (price_arr[orderitem_num]) {
            orderitem_quantity = parseFloat(target.value);
>>>>>>> lesson_2_part2
            delta_quantity = orderitem_quantity - quantity_arr[orderitem_num];
            quantity_arr[orderitem_num] = orderitem_quantity;
            orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
        }
    });

    // 2 метод (при нажатие на чек-бокс - удалить все данные)
    $('.order_form').on('click', 'input[type=checkbox]', function () {

        let target = event.target;
<<<<<<< HEAD
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-DELETE', ''));
=======
        orderitem_num = parseFloat(target.name.replace('orderitems-', '').replace('-DELETE', ''));
>>>>>>> lesson_2_part2
        if (target.checked) {
            delta_quantity = -quantity_arr[orderitem_num]
        } else {
            delta_quantity = quantity_arr[orderitem_num];
        }
        orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
    });


   function orderSummaryUpdate(orderitem_price, delta_quantity) {
        delta_cost = orderitem_price * delta_quantity;
        order_total_cost = Number((order_total_cost + delta_cost).toFixed(2));
        order_total_quantity = order_total_quantity + delta_quantity;
        $('.order_total_quantity').html(order_total_quantity.toString());
<<<<<<< HEAD
        $('.order_total_cost').html(order_total_cost.toString() + ',00');
=======
        $('.order_total_cost').html(order_total_cost.toString());
>>>>>>> lesson_2_part2
    }

    $('.formset_row').formset({
        addText: 'добавить продукт',
        deleteText: 'удалить',
        prefix: 'orderitems',
        removed: deleteOrderItem,

    });

    function deleteOrderItem(row) {
        let target_name = row[0].querySelector('input[type="number"]').name
<<<<<<< HEAD
        orderitem_num = parseInt(target_name.replace('orderitems-', '').replace('-quantity', ''))
=======
        orderitem_num = parseFloat(target_name.replace('orderitems-', '').replace('-quantity', ''))
>>>>>>> lesson_2_part2
        delta_quantity = -quantity_arr[orderitem_num]
        orderSummaryUpdate(price_arr[orderitem_num], delta_quantity)
    }

    $('.order_form select').change(function () {

        let target = event.target;
<<<<<<< HEAD
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-product', ''));
=======
        orderitem_num = parseFloat(target.name.replace('orderitems-', '').replace('-product', ''));
>>>>>>> lesson_2_part2
        let orderitem_product_pk = target.options[target.selectedIndex].value;

        console.log(orderitem_num)
        console.log(orderitem_product_pk)

        if (orderitem_product_pk) {
            $.ajax({
                url: '/orders/product/' + orderitem_product_pk + '/price/',
                success: function (data) {
                    if (data.price) {
                        price_arr[orderitem_num] = parseFloat(data.price)
                        if (isNaN(quantity_arr[orderitem_num])) {
                            quantity_arr[orderitem_num] = 0;
                        }
                        let price_html = '<span class="orderitems-' + orderitem_num + '-price">'
                            + data.price.toString().replace('.', ',') + '</span> руб';
                        let current_tr = $('.order_form table').find('tr:eq('+(orderitem_num+1)+')');
                        current_tr.find('td:eq(2)').html(price_html)
                    }
                }


            })
        }

    })


}

 $('.order_form select').change(function () {

        let target = event.target;
<<<<<<< HEAD
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-product', ''));
=======
        orderitem_num = parseFloat(target.name.replace('orderitems-', '').replace('-product', ''));
>>>>>>> lesson_2_part2
        let orderitem_product_pk = target.options[target.selectedIndex].value;

        console.log(orderitem_num)
        console.log(orderitem_product_pk)

        if (orderitem_product_pk) {
            $.ajax({
                url: '/orders/product/' + orderitem_product_pk + '/price/',
                success: function (data) {
                    if (data.price) {
                        price_arr[orderitem_num] = parseFloat(data.price)
                        if (isNaN(quantity_arr[orderitem_num])) {
                            quantity_arr[orderitem_num] = 0;
                        }
                        let price_html = '<span class="orderitems-' + orderitem_num + '-price">'
                            + data.price.toString().replace('.', ',') + '</span> руб';
                        let current_tr = $('.order_form table').find('tr:eq('+(orderitem_num+1)+')');
                        current_tr.find('td:eq(2)').html(price_html)
                    }
                }


            })
        }

    })

window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        var t_href = event.target;

        $.ajax({
            url: '/baskets/edit/' + t_href.name + '/' + t_href.value + '/',
            success: function (data) {
                $('.basket_list').html(data.result);
            },
        })
    });
}
console.log()