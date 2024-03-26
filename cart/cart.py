from queshop.models import Order, Products


class Cart:
    def __init__(self,request):
        self.session = request.session
        self.cart = self.session.get('cart',{})
        print(self.cart)

    def add_cart(self,product,product_num):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            if int(product_num) < 0:
                pass
            elif int(product_num) > 0:
                price = int(product.price) * int(product_num)
                self.cart[product_id] = {'name':str(product.name),
                                         'price':str(product.price),
                                         'amount':str(product_num),
                                         'total': str(price)
                                     }
        self.session['cart'] = self.cart
        self.session.modified = True

    def __len__(self):
        self.session['cart'] = self.cart
        return len(self.cart)

    def delete(self,product_id):
        prod = str(product_id)
        if prod in self.cart:
            del self.cart[prod]
            self.session['cart'] = self.cart
            self.session.modified = True
    def products(self):
        prod_ids = self.cart.keys()
        products = Products.objects.filter(id__in=prod_ids)
        return products

    def all_info(self):
        prods = self.products()
        res = []

        for prod in prods:
            prod_id = str(prod.id)
            if prod_id in self.cart:
                data = {
                    'id': prod.id,
                    'name': str(prod.name),
                    'price': prod.price,
                    'quantity': self.cart[prod_id]['amount']
                }
                res.append(data)
        return res

    def clean_cart(self):
        self.cart = {}
        self.session['cart'] = self.cart
        self.session.modified = True
