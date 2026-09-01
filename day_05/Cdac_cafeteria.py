def calculate_cafeteria_bill(base_price, *items, tax_rate=0.05, discount=0.0, delivery_fee=0.0):
    raw_subtotal=base_price+sum(items)
    discount_subtotal=raw_subtotal*(1-discount/100)
    tax_value=discount_subtotal*tax_rate
    discount_subtotal+=tax_value+delivery_fee
    print(round(discount_subtotal,2))
total2 = calculate_cafeteria_bill(100.0)
print(total2)