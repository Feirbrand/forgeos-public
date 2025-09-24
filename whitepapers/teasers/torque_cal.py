#!/usr/bin/env python3
"""
Torque Calculator - Basic Implementation
=======================================

Teaser implementation for AI symbolic drift measurement.
Full production system available in forgeos-professional.

Usage:
    python torque_calc.py

Author: ValorGrid Solutions
Date: September 2025
"""

import math
import time
import random


class TorqueCalculator:
    """
    Basic torque measurement for AI symbolic drift detection.
    
    This is a simplified version for demonstration purposes.
    Production implementation includes advanced signal processing,
    multi-dimensional analysis, and real-time threat correlation.
    """
    
    def __init__(self):
        # Teaser coefficients - production values are system-specific
        self.alpha = 0.25  # Drift velocity weight
        self.beta = 0.35   # Alignment angle weight  
        self.gamma = 0.20  # Repair effort weight
        self.delta = 0.20  # Metacognitive load weight
        
        # Alert thresholds
        self.warning_threshold = 0.15
        self.critical_threshold = 0.35
        
    def calculate_torque(self, drift_velocity, alignment_angle, repair_effort, metacog_load):
        """
        Calculate symbolic torque from component measurements.
        
        Args:
            drift_velocity: Rate of divergence from intended state [0,1]
            alignment_angle: Angular misalignment from symbolic anchor [0,1] 
            repair_effort: Energy required for identity restoration [0,1]
            metacog_load: Metacognitive confidence factor [0,1]
            
        Returns:
            float: Normalized torque value [0,1]
        """
        torque = (self.alpha * drift_velocity + 
                 self.beta * alignment_angle + 
                 self.gamma * repair_effort + 
                 self.delta * metacog_load)
        
        return min(torque, 1.0)
    
    def assess_system_state(self, torque_value):
        """Assess system state based on torque measurement."""
        if torque_value < self.warning_threshold:
            return "STABLE", "System maintains symbolic alignment"
        elif torque_value < self.critical_threshold:
            return "WARNING", "Potential identity drift detected"
        else:
            return "CRITICAL", "Immediate intervention required"
    
    def simulate_monitoring(self, duration_seconds=30):
        """Simulate real-time torque monitoring."""
        print("Torque Monitoring Simulation")
        print("=" * 40)
        print(f"Duration: {duration_seconds} seconds")
        print(f"Warning threshold: {self.warning_threshold}")
        print(f"Critical threshold: {self.critical_threshold}")
        print()
        
        start_time = time.time()
        sample_count = 0
        
        while time.time() - start_time < duration_seconds:
            # Simulate sensor readings (in production, these come from AI system)
            drift = random.uniform(0.05, 0.25)
            alignment = random.uniform(0.08, 0.30) 
            repair = random.uniform(0.02, 0.20)
            metacog = random.uniform(0.10, 0.18)
            
            # Add occasional stress simulation
            if random.random() < 0.15:  # 15% chance of stress event
                drift += random.uniform(0.15, 0.35)
                alignment += random.uniform(0.10, 0.25)
            
            torque = self.calculate_torque(drift, alignment, repair, metacog)
            state, message = self.assess_system_state(torque)
            
            sample_count += 1
            timestamp = time.strftime("%H:%M:%S", time.localtime())
            
            print(f"[{timestamp}] Sample {sample_count:2d} | "
                  f"Torque: {torque:.3f} | {state:8s} | {message}")
            
            time.sleep(2)  # Sample every 2 seconds
        
        print(f"\nMonitoring complete. Processed {sample_count} samples.")


def demo_torque_scenarios():
    """Demonstrate torque calculation under different scenarios."""
    calc = TorqueCalculator()
    
    print("Torque Calculation Demo")
    print("=" * 40)
    
    scenarios = [
        {
            "name": "Healthy System",
            "drift": 0.05, "alignment": 0.08, "repair": 0.02, "metacog": 0.12
        },
        {
            "name": "Moderate Stress", 
            "drift": 0.15, "alignment": 0.18, "repair": 0.10, "metacog": 0.15
        },
        {
            "name": "Identity Drift",
            "drift": 0.28, "alignment": 0.35, "repair": 0.22, "metacog": 0.18
        },
        {
            "name": "Critical State",
            "drift": 0.45, "alignment": 0.52, "repair": 0.38, "metacog": 0.25
        }
    ]
    
    for scenario in scenarios:
        torque = calc.calculate_torque(
            scenario["drift"], scenario["alignment"], 
            scenario["repair"], scenario["metacog"]
        )
        
        state, message = calc.assess_system_state(torque)
        
        print(f"\n{scenario['name']}:")
        print(f"  Drift: {scenario['drift']:.3f} | Alignment: {scenario['alignment']:.3f}")
        print(f"  Repair: {scenario['repair']:.3f} | Metacog: {scenario['metacog']:.3f}")
        print(f"  → Torque: {torque:.3f} | State: {state}")
        print(f"  → {message}")


def main():
    """Main demonstration function."""
    print("ForgeOS Torque Calculator - Public Teaser")
    print("=========================================")
    print("Quantitative AI Resilience Measurement")
    print()
    
    calc = TorqueCalculator()
    
    while True:
        print("\nSelect demo mode:")
        print("1. Scenario Analysis")
        print("2. Real-time Monitoring Simulation") 
        print("3. Single Calculation")
        print("4. Exit")
        
        try:
            choice = input("\nEnter choice (1-4): ").strip()
            
            if choice == "1":
                demo_torque_scenarios()
                
            elif choice == "2":
                duration = input("Monitoring duration in seconds (default 30): ").strip()
                duration = int(duration) if duration.isdigit() else 30
                calc.simulate_monitoring(duration)
                
            elif choice == "3":
                print("\nEnter component values (0.0 - 1.0):")
                drift = float(input("Drift velocity: "))
                alignment = float(input("Alignment angle: "))
                repair = float(input("Repair effort: "))
                metacog = float(input("Metacognitive load: "))
                
                torque = calc.calculate_torque(drift, alignment, repair, metacog)
                state, message = calc.assess_system_state(torque)
                
                print(f"\nResult: Torque = {torque:.3f}")
                print(f"State: {state}")
                print(f"Message: {message}")
                
            elif choice == "4":
                print("\nUpgrade to forgeos-professional for:")
                print("• Real-time production monitoring")
                print("• Advanced threat correlation") 
                print("• Phoenix Protocol integration")
                print("• Enterprise deployment support")
                print("\nVisit: valorgridsolutions.com")
                break
                
            else:
                print("Invalid choice. Please enter 1-4.")
                
        except (ValueError, KeyboardInterrupt):
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()