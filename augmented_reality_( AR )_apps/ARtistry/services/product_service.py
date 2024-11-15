from models import Product

class ProductService:
    @staticmethod
    def add_product(name, description, image, price, stock):
        product = Product(name=name, description=description, image=image, price=price, stock=stock)
        db.session.add(product)
        db.session.commit()
        return product
