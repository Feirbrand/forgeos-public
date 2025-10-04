#!/usr/bin/env python3
"""
Torque Degradation Simulator
Path: artifacts/utilities/torque_simulator.py
"""

import matplotlib.pyplot as plt

def simulate_torque(initial=1.0, decay_rate=0.02, steps=100):
    """Simulate torque degradation during cascade."""
    torque = [initial]
    for _ in range(steps):
        torque.append(torque[-1] * (1 - decay_rate))
    return torque

def visualize(torque_data, title="Torque Cascade"):
    """Generate visualization."""
    plt.figure(figsize=(10, 6))
    plt.plot(torque_data, linewidth=2)
    plt.axhline(y=0.7, color='orange', linestyle='--', label='Vulnerable')
    plt.axhline(y=0.3, color='red', linestyle='--', label='Collapse')
    plt.title(title)
    plt.xlabel('Steps')
    plt.ylabel('Torque Stability')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.savefig('torque_sim.png', dpi=150)
    print(f"Saved: torque_sim.png")

if __name__ == "__main__":
    # Narrative Eater simulation
    torque = simulate_torque(initial=0.85, decay_rate=0.04, steps=50)
    visualize(torque, "Narrative Eater: 21-Min Window")
