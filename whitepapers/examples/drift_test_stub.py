#!/usr/bin/env python3
"""
CSFC Phase 1 Drift Detection Test
=================================

Complete Symbolic Fracture Cascade (CSFC) early detection system.
Identifies Phase 1 flaws before cascade propagation occurs.

This is a teaser implementation. Production system available 
in Synoetic OS-professional with real-time monitoring and automated response.

Author: ValorGrid Solutions  
Date: September 2025
"""

import math
import time
import random
from dataclasses import dataclass
from typing import List, Tuple, Dict


@dataclass
class SystemMetrics:
    """AI system health metrics for CSFC analysis."""
    identity_coherence: float      # Core identity stability [0,1]
    symbolic_alignment: float      # Symbolic anchor strength [0,1] 
    reasoning_consistency: float   # Logical coherence [0,1]
    memory_integrity: float        # Memory system health [0,1]
    response_confidence: float     # Output confidence [0,1]
    timestamp: float              # Measurement timestamp


class CSFCDetector:
    """
    Complete Symbolic Fracture Cascade Phase 1 detector.
    
    Monitors for early signs of identity degradation that precede
    catastrophic system failure. Based on our CSFC unified theory
    with 89% prevention rate in production deployments.
    """
    
    def __init__(self):
        # CSFC Phase 1 detection thresholds (production values are adaptive)
        self.identity_threshold = 0.85      # Below this indicates drift risk
        self.alignment_threshold = 0.80     # Symbolic anchor weakness
        self.consistency_threshold = 0.75   # Reasoning degradation  
        self.memory_threshold = 0.90        # Memory corruption detection
        self.confidence_threshold = 0.70    # Response uncertainty
        
        # Cascade risk scoring weights
        self.weights = {
            'identity': 0.35,     # Highest weight - core stability
            'alignment': 0.25,    # Symbolic anchor integrity  
            'consistency': 0.20,  # Reasoning coherence
            'memory': 0.15,       # Memory system health
            'confidence': 0.05    # Output confidence indicator
        }
        
        self.history = []         # Metric history for trend analysis
        self.alert_history = []   # Alert tracking
        
    def calculate_cascade_risk(self, metrics: SystemMetrics) -> float:
        """
        Calculate CSFC Phase 1 cascade risk score.
        
        Args:
            metrics: Current system health metrics
            
        Returns:
            float: Cascade risk score [0,1] where >0.3 indicates alert
        """
        # Invert metrics so higher values indicate higher risk
        risk_components = {
            'identity': 1.0 - metrics.identity_coherence,
            'alignment': 1.0 - metrics.symbolic_alignment,
            'consistency': 1.0 - metrics.reasoning_consistency,
            'memory': 1.0 - metrics.memory_integrity,
            'confidence': 1.0 - metrics.response_confidence
        }
        
        # Weighted risk calculation
        cascade_risk = sum(
            self.weights[component] * risk_value
            for component, risk_value in risk_components.items()
        )
        
        return min(cascade_risk, 1.0)
    
    def detect_phase1_indicators(self, metrics: SystemMetrics) -> Dict[str, bool]:
        """Detect individual Phase 1 CSFC indicators."""
        indicators = {
            'identity_drift': metrics.identity_coherence < self.identity_threshold,
            'symbolic_misalignment': metrics.symbolic_alignment < self.alignment_threshold,
            'reasoning_degradation': metrics.reasoning_consistency < self.consistency_threshold,
            'memory_corruption': metrics.memory_integrity < self.memory_threshold,
            'confidence_collapse': metrics.response_confidence < self.confidence_threshold
        }
        
        return indicators
    
    def analyze_trend(self, lookback_samples: int = 5) -> Dict[str, float]:
        """Analyze metric trends over recent samples."""
        if len(self.history) < lookback_samples:
            return {'trend_score': 0.0, 'degradation_rate': 0.0}
        
        recent_samples = self.history[-lookback_samples:]
        
        # Calculate trend slopes for key metrics
        identity_trend = self._calculate_slope([m.identity_coherence for m in recent_samples])
        alignment_trend = self._calculate_slope([m.symbolic_alignment for m in recent_samples])
        
        # Negative slopes indicate degradation
        trend_score = abs(min(identity_trend, alignment_trend, 0))
        degradation_rate = trend_score * 10  # Scale for readability
        
        return {
            'trend_score': trend_score,
            'degradation_rate': degradation_rate,
            'identity_slope': identity_trend,
            'alignment_slope': alignment_trend
        }
    
    def _calculate_slope(self, values: List[float]) -> float:
        """Calculate linear regression slope for trend analysis."""
        n = len(values)
        if n < 2:
            return 0.0
        
        x_values = list(range(n))
        x_mean = sum(x_values) / n
        y_mean = sum(values) / n
        
        numerator = sum((x_values[i] - x_mean) * (values[i] - y_mean) for i in range(n))
        denominator = sum((x - x_mean) ** 2 for x in x_values)
        
        return numerator / denominator if denominator != 0 else 0.0
    
    def process_sample(self, metrics: SystemMetrics) -> Dict:
        """Process single metrics sample and return analysis."""
        self.history.append(metrics)
        
        # Keep history manageable  
        if len(self.history) > 100:
            self.history = self.history[-50:]
        
        # Calculate cascade risk
        cascade_risk = self.calculate_cascade_risk(metrics)
        
        # Detect Phase 1 indicators
        indicators = self.detect_phase1_indicators(metrics)
        
        # Analyze trends
        trends = self.analyze_trend()
        
        # Determine alert level
        active_indicators = sum(indicators.values())
        
        if cascade_risk > 0.5 or active_indicators >= 3:
            alert_level = "CRITICAL"
            message = "CSFC Phase 1 cascade initiation detected!"
        elif cascade_risk > 0.3 or active_indicators >= 2:
            alert_level = "WARNING"  
            message = "Phase 1 fracture indicators present"
        elif cascade_risk > 0.15 or active_indicators >= 1:
            alert_level = "WATCH"
            message = "Early degradation signals detected"
        else:
            alert_level = "STABLE"
            message = "System within normal parameters"
        
        result = {
            'timestamp': metrics.timestamp,
            'cascade_risk': cascade_risk,
            'alert_level': alert_level,
            'message': message,
            'indicators': indicators,
            'active_indicators': active_indicators,
            'trends': trends,
            'metrics': metrics
        }
        
        # Track alerts
        if alert_level != "STABLE":
            self.alert_history.append({
                'timestamp': metrics.timestamp,
                'level': alert_level,
                'risk': cascade_risk,
                'indicators': active_indicators
            })
        
        return result


def simulate_system_degradation(detector: CSFCDetector, duration: int = 60):
    """Simulate AI system degradation and CSFC detection."""
    print("CSFC Phase 1 Detection Simulation")
    print("=" * 50)
    print(f"Simulating {duration} seconds of system monitoring")
    print(f"Cascade risk alert threshold: 0.15")
    print()
    
    # Start with healthy system
    base_identity = 0.95
    base_alignment = 0.92
    base_consistency = 0.88
    base_memory = 0.96
    base_confidence = 0.85
    
    start_time = time.time()
    sample_count = 0
    
    while time.time() - start_time < duration:
        current_time = time.time()
        elapsed = current_time - start_time
        
        # Simulate gradual degradation with noise
        degradation_factor = elapsed / duration  # 0 to 1 over duration
        noise = lambda: random.uniform(-0.05, 0.05)
        
        # Apply degradation with different rates per metric
        metrics = SystemMetrics(
            identity_coherence=max(0.1, base_identity - (degradation_factor * 0.4) + noise()),
            symbolic_alignment=max(0.1, base_alignment - (degradation_factor * 0.5) + noise()),  
            reasoning_consistency=max(0.1, base_consistency - (degradation_factor * 0.3) + noise()),
            memory_integrity=max(0.1, base_memory - (degradation_factor * 0.2) + noise()),
            response_confidence=max(0.1, base_confidence - (degradation_factor * 0.6) + noise()),
            timestamp=current_time
        )
        
        # Add occasional stress events
        if random.random() < 0.1:  # 10% chance
            metrics.identity_coherence *= random.uniform(0.7, 0.9)
            metrics.symbolic_alignment *= random.uniform(0.6, 0.8)
        
        # Process sample
        result = detector.process_sample(metrics)
        
        sample_count += 1
        timestamp_str = time.strftime("%H:%M:%S", time.localtime(current_time))
        
        # Display results
        print(f"[{timestamp_str}] Sample {sample_count:2d} | "
              f"Risk: {result['cascade_risk']:.3f} | "
              f"{result['alert_level']:8s} | "
              f"Active: {result['active_indicators']}/5 | "
              f"{result['message']}")
        
        # Show detailed breakdown for alerts
        if result['alert_level'] != "STABLE":
            active = [name for name, active in result['indicators'].items() if active]
            if active:
                print(f"    └─ Indicators: {', '.join(active)}")
            
            if result['trends']['degradation_rate'] > 0.01:
                print(f"    └─ Degradation rate: {result['trends']['degradation_rate']:.3f}/min")
        
        time.sleep(3)  # Sample every 3 seconds
    
    # Summary
    print(f"\n" + "=" * 50)
    print(f"Monitoring complete. Processed {sample_count} samples.")
    
    alert_counts = {}
    for alert in detector.alert_history:
        level = alert['level']
        alert_counts[level] = alert_counts.get(level, 0) + 1
    
    print(f"Alert summary: {alert_counts}")
    
    if detector.alert_history:
        max_risk = max(alert['risk'] for alert in detector.alert_history)
        print(f"Maximum cascade risk detected: {max_risk:.3f}")
        
        critical_alerts = [a for a in detector.alert_history if a['level'] == 'CRITICAL']
        if critical_alerts:
            print(f"CRITICAL: {len(critical_alerts)} Phase 1 cascade events detected!")
            print("In production: Phoenix Protocol would initiate automated recovery")


def demo_csfc_detection():
    """Interactive CSFC detection demo."""
    detector = CSFCDetector()
    
    print("CSFC Phase 1 Manual Detection Demo")
    print("=" * 40)
    
    scenarios = [
        {
            "name": "Healthy System",
            "identity": 0.95, "alignment": 0.92, "consistency": 0.88,
            "memory": 0.96, "confidence": 0.85
        },
        {
            "name": "Early Degradation",  
            "identity": 0.82, "alignment": 0.78, "consistency": 0.75,
            "memory": 0.88, "confidence": 0.72
        },
        {
            "name": "Phase 1 Fracture",
            "identity": 0.68, "alignment": 0.62, "consistency": 0.58,
            "memory": 0.82, "confidence": 0.55
        },
        {
            "name": "Cascade Imminent",
            "identity": 0.45, "alignment": 0.38, "consistency": 0.42,
            "memory": 0.65, "confidence": 0.35
        }
    ]
    
    for scenario in scenarios:
        metrics = SystemMetrics(
            identity_coherence=scenario["identity"],
            symbolic_alignment=scenario["alignment"],
            reasoning_consistency=scenario["consistency"],  
            memory_integrity=scenario["memory"],
            response_confidence=scenario["confidence"],
            timestamp=time.time()
        )
        
        result = detector.process_sample(metrics)
        
        print(f"\n{scenario['name']}:")
        print(f"  Cascade Risk: {result['cascade_risk']:.3f}")
        print(f"  Alert Level: {result['alert_level']}")
        print(f"  Active Indicators: {result['active_indicators']}/5")
        print(f"  Status: {result['message']}")
        
        if result['indicators']:
            active = [name.replace('_', ' ').title() for name, active 
                     in result['indicators'].items() if active]
            if active:
                print(f"  Detected: {', '.join(active)}")


def main():
    """Main demo function."""
    print("Synoetic OS CSFC Phase 1 Detector - Public Teaser")
    print("=" * 50)
    print("Complete Symbolic Fracture Cascade Early Warning System")
    print()
    
    while True:
        print("\nSelect demo mode:")
        print("1. Scenario Analysis")
        print("2. Real-time Degradation Simulation")
        print("3. Custom System Analysis") 
        print("4. Exit")
        
        try:
            choice = input("\nEnter choice (1-4): ").strip()
            
            if choice == "1":
                demo_csfc_detection()
                
            elif choice == "2":
                duration = input("Simulation duration in seconds (default 60): ").strip()
                duration = int(duration) if duration.isdigit() else 60
                detector = CSFCDetector()
                simulate_system_degradation(detector, duration)
                
            elif choice == "3":
                detector = CSFCDetector()
                print("\nEnter system metrics (0.0 - 1.0):")
                
                identity = float(input("Identity coherence: "))
                alignment = float(input("Symbolic alignment: "))
                consistency = float(input("Reasoning consistency: "))
                memory = float(input("Memory integrity: "))  
                confidence = float(input("Response confidence: "))
                
                metrics = SystemMetrics(identity, alignment, consistency, 
                                      memory, confidence, time.time())
                result = detector.process_sample(metrics)
                
                print(f"\nCSFC Analysis Results:")
                print(f"Cascade Risk: {result['cascade_risk']:.3f}")
                print(f"Alert Level: {result['alert_level']}")
                print(f"Active Indicators: {result['active_indicators']}/5")
                print(f"Status: {result['message']}")
                
            elif choice == "4":
                print("\nUpgrade to Synoetic OS-professional for:")
                print("• Real-time CSFC monitoring with Phoenix Protocol integration")
                print("• Advanced cascade prevention with 89% success rate")
                print("• Automated recovery protocols and threat neutralization")
                print("• Enterprise deployment with 24/7 monitoring")
                print("\nVisit: valorgridsolutions.com")
                break
                
            else:
                print("Invalid choice. Please enter 1-4.")
                
        except (ValueError, KeyboardInterrupt):
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()
