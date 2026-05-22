# contingency_protocol.py
# Author: Gil (AegisNode)
# Description:
# Autonomous contingency protocol for lunar colony.
# Detects anomalies (heat, pressure, debris/meteors), applies isolation,
# activates backups, and maps space surface to anticipate large asteroid threats.
# Includes gravity factor and dynamic space environment changes.

import random
import time

# --- Parameters ---
HEAT_THRESHOLD = 75.0        # Max safe temperature (°C)
PRESSURE_THRESHOLD = 1.5     # Max safe pressure (atm)
DEBRIS_THRESHOLD = 0.7       # Probability threshold for debris/meteor impact (0–1)
GRAVITY_LUNAR = 1.62         # Lunar gravity (m/s^2)
RECHARGE_BASE = 120          # Base recharge time (minutes)

# --- Monitoring Functions ---
def read_sensors():
    """Simulate sensor readings for heat, pressure, debris probability, and asteroid size."""
    heat = random.uniform(50, 100)       # °C
    pressure = random.uniform(1.0, 2.0)  # atm
    debris = random.random()             # debris probability (0–1)
    asteroid_size = random.uniform(10, 500)  # meters
    return heat, pressure, debris, asteroid_size

def detect_anomalies(heat, pressure, debris, asteroid_size):
    """Detect anomalies based on thresholds."""
    anomalies = []
    if heat > HEAT_THRESHOLD:
        anomalies.append(f"Heat anomaly: {heat:.2f} °C")
    if pressure > PRESSURE_THRESHOLD:
        anomalies.append(f"Pressure anomaly: {pressure:.2f} atm")
    if debris > DEBRIS_THRESHOLD:
        anomalies.append(f"Space debris/meteor anomaly: {debris:.2f} probability")
    if asteroid_size > 300:
        anomalies.append(f"Asteroid threat: {asteroid_size:.2f} m diameter")
    return anomalies

def calculate_recharge(heat, pressure, debris):
    """Calculate recharge time considering stress factors and lunar gravity."""
    factor = (heat / HEAT_THRESHOLD) + (pressure / PRESSURE_THRESHOLD) + (1 + debris)
    # Gravity factor: slower construction under lunar gravity
    gravity_factor = 9.81 / GRAVITY_LUNAR
    recharge_time = RECHARGE_BASE * factor * (gravity_factor * 0.1)
    return recharge_time

def contingency_protocol(anomalies):
    """Apply contingency measures if anomalies are detected."""
    if not anomalies:
        return "✅ Normal operation: systems stable."
    response = "⚠️ Contingency activated:\n"
    if any("Heat" in a for a in anomalies):
        response += "- Isolate overheated zone, activate cooling.\n"
    if any("Pressure" in a for a in anomalies):
        response += "- Seal affected dome, backup atmosphere engaged.\n"
    if any("debris" in a or "meteor" in a for a in anomalies):
        response += "- Activate shields and weapons for debris defense.\n"
    if any("Asteroid" in a for a in anomalies):
        response += "- Map surface trajectory, deploy satellites for deflection.\n"
    return response

# --- Main Loop ---
def main():
    for cycle in range(10):  # Run 10 monitoring cycles
        heat, pressure, debris, asteroid_size = read_sensors()
        anomalies = detect_anomalies(heat, pressure, debris, asteroid_size)
        recharge_time = calculate_recharge(heat, pressure, debris)
        response = contingency_protocol(anomalies)

        # Log results
        print(f"\nCycle {cycle+1}")
        print(f"Heat: {heat:.2f} °C | Pressure: {pressure:.2f} atm | Debris: {debris:.2f} | Asteroid: {asteroid_size:.2f} m")
        print(f"Recharge time: {recharge_time:.2f} minutes")
        if anomalies:
            print("Anomalies detected:", anomalies)
        print("Protocol response:\n", response)

        time.sleep(1)  # Simulate real-time monitoring

    print("\n--- Contingency Monitoring Complete ---")

if __name__ == "__main__":
    main()
