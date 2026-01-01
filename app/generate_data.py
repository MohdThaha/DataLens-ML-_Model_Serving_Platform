import pandas as pd
import random
from datetime import datetime, timedelta
import uuid

# --------------------
# Configuration
# --------------------
NUM_ROWS = 10000
START_DATE = datetime(2024, 1, 1)

products = [
    ("A", "Electronics", 300, 800),
    ("B", "Electronics", 250, 600),
    ("C", "Furniture", 600, 1500),
    ("D", "Furniture", 800, 2000),
    ("E", "Clothing", 100, 400),
    ("F", "Clothing", 80, 300),
    ("G", "Electronics", 350, 900),
]

regions = ["North", "South", "East", "West"]
sales_channels = ["Online", "Retail", "Distributor"]
payment_methods = ["Card", "UPI", "Cash", "NetBanking"]
customer_types = ["New", "Returning"]

data = []

for _ in range(NUM_ROWS):
    product, category, min_price, max_price = random.choice(products)

    date = START_DATE + timedelta(days=random.randint(0, 365))
    price = round(random.uniform(min_price, max_price), 2)
    cost_price = round(price * random.uniform(0.55, 0.75), 2)
    quantity = random.randint(1, 10)

    discount_pct = random.choice([0, 5, 10, 15])
    discount_amount = price * (discount_pct / 100)

    final_price = price - discount_amount
    total_sales = round(final_price * quantity, 2)
    profit = round((final_price - cost_price) * quantity, 2)

    region = random.choice(regions)
    sales_channel = random.choice(sales_channels)
    payment_method = random.choice(payment_methods)
    customer_type = random.choice(customer_types)

    order_id = str(uuid.uuid4())[:8]
    is_weekend = 1 if date.weekday() >= 5 else 0

    # Introduce missing values (realistic)
    if random.random() < 0.03:
        discount_pct = None
    if random.random() < 0.03:
        payment_method = None

    data.append([
        date.strftime("%Y-%m-%d"),
        order_id,
        product,
        category,
        price,
        cost_price,
        quantity,
        discount_pct,
        total_sales,
        profit,
        region,
        sales_channel,
        payment_method,
        customer_type,
        is_weekend
    ])

df = pd.DataFrame(
    data,
    columns=[
        "date",
        "order_id",
        "product",
        "category",
        "price",
        "cost_price",
        "quantity",
        "discount_pct",
        "total_sales",
        "profit",
        "region",
        "sales_channel",
        "payment_method",
        "customer_type",
        "is_weekend"
    ]
)

df.to_csv("data/sales.csv", index=False)

print("✅ Advanced dataset generated")
print(df.head())
print(f"Rows: {len(df)}")
