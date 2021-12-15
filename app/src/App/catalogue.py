def bespeak_product(symbol, title, brand_name, price, discription):
    symbol = symbol
    title = "<b>" + title + "</b>"
    brand_name = "от <i>«" + brand_name + "»</i>"
    price = "<code>" + str(int(price)) + "₽</code> или <code>" + str(int(float(price) / 0.44)) + "¤</code>"
    discription = "\n<i>..." + discription + ".</i>"
    combination = str(symbol) + " " + str(title) + " " + brand_name + " = " + str(price) + str(discription)
    
    return(combination)
