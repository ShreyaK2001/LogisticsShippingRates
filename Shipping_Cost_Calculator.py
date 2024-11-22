#Shipping Cost Calculator

##Input Package weight and shipping rate
weight = float(input("Enter the package rate in kilograms: "))
rate = float(input("Enter the shipping rate per kilograms: "))

##Calculate shipping cost
shipping_cost = weight * rate

##Display the result
print(f"Shipping cost: {shipping_cost}USD")
