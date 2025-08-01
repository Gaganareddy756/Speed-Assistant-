import random
import time

def get_vehicle_speed():
    """Simulates obtaining the current speed from a vehicle sensor."""
    return random.randint(20, 150)  # Speed in km/h

def get_speed_limit():
    """Simulates obtaining the speed limit from GPS mapping."""
    return random.choice([30, 50, 80, 100, 120, 130])  # Speed limit options in km/h

def get_road_condition():
    """Simulates detecting road conditions."""
    return random.choice(["dry", "wet", "icy", "foggy", "snowy"])

def get_traffic_density():
    """Simulates obtaining traffic density data."""
    return random.choice(["low", "moderate", "high", "very high"])

def calculate_recommended_speed(speed, limit, condition, traffic):
    """Determines the recommended speed based on multiple factors."""
    adjustment = 0
    
    # Adjustments based on road conditions
    if condition == "wet":
        adjustment = -10
    elif condition == "icy":
        adjustment = -20
    elif condition == "foggy":
        adjustment = -15
    elif condition == "snowy":
        adjustment = -25
    
    # Adjustments based on traffic conditions
    if traffic == "moderate":
        adjustment -= 5
    elif traffic == "high":
        adjustment -= 10
    elif traffic == "very high":
        adjustment -= 15
    
    recommended_speed = min(limit + adjustment, speed)
    return max(recommended_speed, 20)  # Ensure minimum speed of 20 km/h

def speed_assistant():
    """Main function that monitors and suggests speed adjustments in real-time."""
    while True:
        speed = get_vehicle_speed()
        limit = get_speed_limit()
        condition = get_road_condition()
        traffic = get_traffic_density()
        
        print("---------------------------")
        print(f"Current Speed: {speed} km/h")
        print(f"Speed Limit: {limit} km/h")
        print(f"Road Condition: {condition}")
        print(f"Traffic Density: {traffic}")
        
        recommended_speed = calculate_recommended_speed(speed, limit, condition, traffic)
        
        if speed > limit:
            print("Warning: Reduce Speed!")
        
        print(f"Recommended Speed: {recommended_speed} km/h")
        
        time.sleep(5)  # Simulate real-time monitoring every 5 seconds

if __name__ == "__main__":
    speed_assistant()
