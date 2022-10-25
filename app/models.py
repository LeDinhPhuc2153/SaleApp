from sqlalchemy import Column, Integer, String, Float, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from app import db, app


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(20), nullable=False)
    products = relationship('Product', backref='category', lazy=False)

    def __str__(self):
        return self.name


class Product(BaseModel):
    __tablename__ = 'product'

    name = Column(String(50), nullable=False)
    description = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():

        # db.create_all()

        # c1 = Category(name='Điện thoại')
        # c2 = Category(name='Máy tính bảng')
        # c3 = Category(name='Phụ kiện')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        # db.session.commit()

        p1 = Product(name='Redmi', description='Android, 128GB', price=23000000,
                 image='https://cdn.tgdd.vn/Products/Images/42/272668/xiaomi-redmi-note-11s-5g-%20thumb-600x600.jpg',
                 category_id=1)
        p2 = Product(name='Iphone 13 Pro', description='Apple, 128GB', price=28000000,
                     image='https://cdn.tgdd.vn/Products/Images/42/230529/iphone-13-pro-max-sierra-blue-600x600.jpg',
                     category_id=1)
        p3 = Product(name='Ipad', description='Samsung, 128GB', price=10000000,
                     image='https://cdn.tgdd.vn/Products/Images/522/237325/samsung-galaxy-tab-a7-lite-gray-600x600.jpg',
                     category_id=2)
        p4 = Product(name='Iphone', description='Apple, 128GB', price=25000000,
                     image='https://cdn.tgdd.vn/Products/Images/42/153856/iphone-xi-xanhla-600x600.jpg',
                     category_id=2)
        p5 = Product(name='Reno Pro', description='Android, 128GB', price=28000000,
                     image='https://cdn.tgdd.vn/Products/Images/42/260546/oppo-reno8-pro-thumb-xanh-1-600x600.jpg',
                     category_id=3)
        p6 = Product(name='Iphone 14', description='Apple, 128GB', price=23000000,
                     image='https://cdn.tgdd.vn/Products/Images/42/247508/iphone-14-pro-den-thumb-600x600.jpg',
                     category_id=3)

        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.add(p5)
        db.session.add(p6)

        db.session.commit()
