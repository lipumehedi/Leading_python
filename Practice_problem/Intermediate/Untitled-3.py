room_type = ["standard", "Delux"]
hotel = []
floor = 0
while floor <2:
    hotel.append([])
    r_type =0
    while r_type<2:
        hotel[floor].append([])
        room = 0
        while room<3:
            guests = input(f"Guest in floor {floor+1}, {room_type[r_type]}, Room {room+1}: ")
            hotel[floor][r_type].append(guests)
            room +=1
        r_type +=1
    floor+=1

floor = 0
while floor <2:
    r_type = 0
    while r_type<2:
        room = 0
        while room <3:
            print(f"Floor{floor+1} | {room_type[r_type]},| Room {room+1} -> {hotel[floor][r_type][room]} guest(s)")
            room +=1
        r_type +=1
    floor +=1

