print "*" * 80

melon_prices = {"Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00}
melon_count_tracking = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0}


def revenue_of_melons(melon_order_report, melon_prices, melon_count_tracking):
    
    report = open(melon_order_report)
    
    for line in report:
        index, melon_type, melon_count = line.split("|")
        melon_count_tracking[melon_type] += int(melon_count)
        
    for melon_type in melon_prices:
        revenue = melon_prices[melon_type] * melon_count_tracking[melon_type]
        print "We sold {} {} melons at {:.2f} each for a total of {:.2f}".format(melon_count_tracking[melon_type], melon_type, melon_prices[melon_type], revenue)

    report.close()

revenue_of_melons("orders-by-type.txt", melon_prices, melon_count_tracking)
  
    
print "*" * 42


def sales_type_revenue(sales_type_report):
    
    report = open(sales_type_report)

    sales_people = 0
    internet_sales = 0
    
    for line in report:
        data = line.split("|")
        if data[1] == "0":
            internet_sales += float(data[3])
        else:
            sales_people += float(data[3])

    print "Salespeople generated ${:.2f} in revenue.".format(sales_people)
    print "Internet sales generated ${:.2f} in revenue.".format(internet_sales)

    if sales_people > internet_sales:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"

sales_type_revenue("orders-with-sales.txt")

print "*" * 42
