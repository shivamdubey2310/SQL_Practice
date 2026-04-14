import random
import uuid
from faker import Faker
import pandas as pd
from tqdm import tqdm

fake = Faker()

# ========================
# CONFIG (adjust for size)
# ========================
NUM_USERS = 100_000
NUM_PRODUCTS = 20_000
NUM_ORDERS = 300_000
MAX_ITEMS_PER_ORDER = 5

# ========================
# USERS
# ========================
def generate_users(n):
    users = []
    for _ in tqdm(range(n), desc="Generating Users"):
        users.append({
            "user_id": str(uuid.uuid4()),
            "name": fake.name(),
            "email": fake.unique.email(),
            "phone": fake.phone_number(),
            "city": fake.city(),
            "country": fake.country(),
            "created_at": fake.date_time_this_decade()
        })
    return pd.DataFrame(users)

# ========================
# PRODUCTS
# ========================
def generate_products(n):
    categories = ["Electronics", "Clothing", "Home", "Sports", "Books"]
    products = []
    
    for _ in tqdm(range(n), desc="Generating Products"):
        products.append({
            "product_id": str(uuid.uuid4()),
            "name": fake.word().capitalize(),
            "category": random.choice(categories),
            "price": round(random.uniform(5, 5000), 2),
            "stock": random.randint(0, 1000)
        })
    return pd.DataFrame(products)

# ========================
# ORDERS + ORDER ITEMS
# ========================
def generate_orders(users, products, n_orders):
    orders = []
    order_items = []
    
    user_ids = users["user_id"].tolist()
    product_ids = products["product_id"].tolist()
    
    for _ in tqdm(range(n_orders), desc="Generating Orders"):
        order_id = str(uuid.uuid4())
        user_id = random.choice(user_ids)
        order_date = fake.date_time_this_year()
        
        orders.append({
            "order_id": order_id,
            "user_id": user_id,
            "order_date": order_date,
            "status": random.choice(["placed", "shipped", "delivered", "cancelled"])
        })
        
        num_items = random.randint(1, MAX_ITEMS_PER_ORDER)
        chosen_products = random.sample(product_ids, num_items)
        
        for product_id in chosen_products:
            quantity = random.randint(1, 5)
            order_items.append({
                "order_item_id": str(uuid.uuid4()),
                "order_id": order_id,
                "product_id": product_id,
                "quantity": quantity
            })
    
    return pd.DataFrame(orders), pd.DataFrame(order_items)

# ========================
# PAYMENTS
# ========================
def generate_payments(orders):
    payments = []
    
    for _, row in tqdm(orders.iterrows(), total=len(orders), desc="Generating Payments"):
        payments.append({
            "payment_id": str(uuid.uuid4()),
            "order_id": row["order_id"],
            "amount": round(random.uniform(10, 5000), 2),
            "payment_method": random.choice(["card", "upi", "netbanking", "wallet"]),
            "payment_status": random.choice(["success", "failed", "pending"]),
            "payment_date": fake.date_time_this_year()
        })
    
    return pd.DataFrame(payments)

# ========================
# MAIN
# ========================
def main():
    print("🚀 Generating data...")

    users = generate_users(NUM_USERS)
    products = generate_products(NUM_PRODUCTS)
    orders, order_items = generate_orders(users, products, NUM_ORDERS)
    payments = generate_payments(orders)

    print("💾 Saving to CSV...")

    users.to_csv("users.csv", index=False)
    products.to_csv("products.csv", index=False)
    orders.to_csv("orders.csv", index=False)
    order_items.to_csv("order_items.csv", index=False)
    payments.to_csv("payments.csv", index=False)

    print("✅ Done!")

if __name__ == "__main__":
    main()