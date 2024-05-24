from albion_data import Var
t4leather = Var("T4_LEATHER","Fort Sterling","sell_price_min")
t4hide = Var("T4_HIDE","Fort Sterling","sell_price_min")
t3leather = Var("T3_LEATHER","Fort Sterling","sell_price_min")
if (2 * t4hide + t3leather) < t4leather: #triggers a single API call
    print("refine t4hide")
else:
    print("not worth it")
