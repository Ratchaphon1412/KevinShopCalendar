# Installations

ติดตั้ง poetry ลงในเครื่อง

```bash
pip install poetry
```

ใช้ poetry install ในการติดตั้ง package ที่ต้องใช้ ใน project

```bash
poetry install
```

ใช้ poetry สร้าง database SQLite และสร้าง table ต่างๆ ที่ต้องใช้ใน project

```bash
poetry run python manage.py migrate
```

ใช้ poetry รัน seed ข้อมูลเข้าไปใน database
-- number คือ จำนวนข้อมูลที่ต้องการ seed เข้าไปใน database

```bash
poetry run python3 manage.py seed product --number=15
```

ใช้ poetry รัน server ขึ้นมา
เปิด port 8000 ให้เรียกใช้งานได้

```bash
poetry run python manage.py runserver 0.0.0.0:8000
```

### api ที่ใช้ในการทดสอบ

#### GET All Products

```bash
http://localhost:8000/api/products/
```

#### GET Product By ID

```bash
http://localhost:8000/api/products/1/
```

#### GET All Cart

```bash
http://localhost:8000/api/cart/
```

#### POST Save to Cart

```bash
http://localhost:8000/api/cart/
```

body

```bash
{
    "product": 1,
    "quantity":2 ,
    "total" : 500
}
```

#### Delete Product in Cart

```bash
http://localhost:8000/api/cart/
```

body

```bash
{
    "product_id" : 1
}

```

### แก้ไขข้อมูลใน Database

ใช้ DataGrip หรือ UI อื่นๆ ในการเข้าถึง database และแก้ไขข้อมูลใน database
db.sqlite3
