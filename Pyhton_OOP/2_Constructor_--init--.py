class Airplane:
    def __init__(self, name, model, capacity, max_speed):
        self.name = name
        self.model = model
        self.capacity = capacity
        self.max_speed = max_speed
Thai = Airplane("TG661", "747",  416, 624)
Us_Banla = Airplane("BS107", "A380",  853, 614)
Air_china = Airplane("CA", "747", 610, 614)

print(Air_china.capacity)