import random

class ParkingLot:
    def __init__(self, total_area, spot_length=8, spot_width=12):
        self.spot_area = spot_length * spot_width
        self.total_spots = total_area // self.spot_area
        self.spots = [None] * self.total_spots

    def is_full(self):
        return all(spot is not None for spot in self.spots)

    def park_car(self, car, spot_num):
        if spot_num < 0 or spot_num >= self.total_spots:
            return False, "Invalid spot number."
        if self.spots[spot_num] is None:
            self.spots[spot_num] = car
            return True, f"Car with license plate {car} parked successfully in spot {spot_num}."
        else:
            return False, f"Spot {spot_num} is already occupied."

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return self.license_plate

    def park(self, parking_lot, spot_num):
        return parking_lot.park_car(self, spot_num)

def generate_random_license_plate():
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=7))

def main():
    total_area = 2000  # Example total area in square feet
    parking_lot = ParkingLot(total_area)

    # Create an array of Car objects with random license plates
    num_cars = 25  # Example number of cars
    cars = [Car(generate_random_license_plate()) for _ in range(num_cars)]

    for car in cars:
        if parking_lot.is_full():
            print("Parking lot is full. Cannot park any more cars.")
            break
        
        parked = False
        while not parked:
            spot_num = random.randint(0, parking_lot.total_spots - 1)
            success, message = car.park(parking_lot, spot_num)
            if success:
                parked = True
            print(message)

if __name__ == "__main__":
    main()
