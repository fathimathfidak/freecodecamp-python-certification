distance_mi=30
is_raining=False
has_bike=True
has_car=False
has_ride_share_app=True
if distance_mi==0:
    print(False)
elif distance_mi<=1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi<=6:
    if is_raining and has_bike==False:
        print(False)
    elif has_bike==False and not is_raining:
        print(False)
    else:
        print(True)
else:
     if has_ride_share_app or has_car:
        print(True)
     else:
        print(False)