# anomaly_detection_extended.py
# Author: Gil (AegisNode)
# Description:
# Continuous monitoring script for lunar colony systems.
# Detects anomalies in heat, pressure, and space debris/meteors.
# Calculates construction recharge time and optimizes processes to prevent contingencies.

import random
import time
import statistics

# --- Parameters ---
HEAT_THRESHOLD = 75.0        # Max safe temperature (°C)
PRESSURE_THRESHOLD = 1.5     # Max safe pressure (atm)
DEBRIS_THRESHOLD = 0.7       # Probability threshold for debris/meteor impact (0–1 scale)
RECHARGE_BASE = 120          # Base recharge time (minutes)

# --- Monitoring Functions ---
def read_sensors():
    """Simulate sensor readings for heat, pressure, and debris probability."""
    heat = random.uniform(50, 100)       # Simulated °C
    pressure = random.uniform(1.0, 2.0)  # Simulated atm
    debris = random.random()             # Simulated debris probability (0–1)
    return heat, pressure, debris

def detect_anomalies(heat, pressure, debris):
    """Detect anomalies based on thresholds."""
    anomalies = []
    if heat > HEAT_THRESHOLD:
        anomalies.append(f"Heat anomaly: {heat:.2f} °C")
    if pressure > PRESSURE_THRESHOLD:
        anomalies.append(f"Pressure anomaly: {pressure:.2f} atm")
    if debris > DEBRIS_THRESHOLD:
        anomalies.append(f"Space debris/meteor anomaly: {debris:.2f} probability")
    return anomalies

def calculate_recharge(heat, pressure, debris):
    """Calculate recharge time based on stress factors."""
    factor = (heat / HEAT_THRESHOLD) + (pressure / PRESSURE_THRESHOLD) + (1 + debris)
    recharge_time = RECHARGE_BASE * factor
    return recharge_time

def optimize_process(recharge_time, anomalies):
    """Suggest optimization strategies."""
    if anomalies:
        return "⚠️ Contingency mode: activate shields, cooling, and debris defense."
    elif recharge_time > RECHARGE_BASE * 2:
        return "🔧 Optimization: deploy extra robots, satellites, and emergency materials."
    else:
        return "✅ Normal operation: systems stable."

# --- Main Loop ---
def main():
    history = []
    for cycle in range(10):  # Run 10 monitoring cycles
        heat, pressure, debris = read_sensors()
        anomalies = detect_anomalies(heat, pressure, debris)
        recharge_time = calculate_recharge(heat, pressure, debris)
        optimization = optimize_process(recharge_time, anomalies)

        # Log results
        print(f"\nCycle {cycle+1}")
        print(f"Heat: {heat:.2f} °C | Pressure: {pressure:.2f} atm | Debris: {debris:.2f}")
        print(f"Recharge time: {recharge_time:.2f} minutes")
        if anomalies:
            print("Anomalies detected:", anomalies)
        print("Optimization advice:", optimization)

        history.append(recharge_time)
        time.sleep(1)  # Simulate real-time monitoring

    # Summary
    avg_recharge = statistics.mean(history)
    print("\n--- Monitoring Summary ---")
    print(f"Average recharge time: {avg_recharge:.2f} minutes")
    print("System analysis complete.")

if __name__ == "__main__":
    main()
