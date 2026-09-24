product_price = int(input("Enter the price of the product: "))
final_product_price = 0
product_discount = 0

if product_price < 100:
    product_discount = product_price * 0.02
else:
    product_discount = product_price * 0.10

final_product_price = product_price - product_discount

print(f"The final price of the product is: {final_product_price} and the discount applied is: {product_discount}")