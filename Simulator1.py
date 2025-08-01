import random

def get_vehicle_speed():
    """Simulates obtaining the current speed from a vehicle sensor."""
    return random.randint(20, 120)  # Speed in km/h

def get_speed_limit():
    """Simulates obtaining the speed limit from GPS mapping."""
    return random.choice([30, 50, 80, 100, 120])  # Speed limit options in km/h

def get_road_condition():
    """Simulates detecting road conditions."""
    return random.choice(["dry", "wet", "icy"])

def speed_assistant():
    speed = get_vehicle_speed()
    limit = get_speed_limit()
    condition = get_road_condition()
    
    print(f"Current Speed: {speed} km/h")
    print(f"Speed Limit: {limit} km/h")
    print(f"Road Condition: {condition}")
    
    adjustment = 0
    if condition == "wet":
        adjustment = -10
    elif condition == "icy":
        adjustment = -20
    
    recommended_speed = min(limit + adjustment, speed)
    
    if speed > limit:
        print("Warning: Reduce Speed!")
    
    print(f"Recommended Speed: {recommended_speed} km/h")

if __name__ == "__main__":
    speed_assistant()
