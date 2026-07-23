def apply_discount(price,discount):
    if isinstance(price,(int,float))!=True:
        return("The price should be a number")
    elif isinstance(discount,(int,float))!=True:
        return("The discount should be a number") 
    elif price<=0:
        return("The price should be greater than 0")
    elif discount<0 or discount>100:
        return("The discount should be between 0 and 100")
    discount_amo unt=(price*discount)/100
    final_price=price-discount_amount
    return final_price
    apply_discount()