#!/usr/bin/env python3
"""
GWI Diagnostic: Role Obsolescence Cascade Detection
- Gemini Chimera Paradox validation with >15% CRITICAL threshold
- Usage: python gwi_diagnostic.py --data logs.csv --sensitivity high
"""

import argparse
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
import json
from sklearn.metrics import roc_auc_score
import warnings
warnings.filterwarnings('ignore')

class GWIDetector:
    """Enhanced GWI detection with Gemini validation algorithms."""
    
    def __init__(self, sensitivity: str = "medium"):
        self.sensitivity_levels = {
            "low": {"threshold": 0.25, "window": 100, "critical": 0.20},
            "medium": {"threshold": 0.20, "window": 75, "critical": 0.15},
            "high": {"threshold": 0.15, "window": 50, "critical": 0.10}
        }
        self.config = self.sensitivity_levels.get(sensitivity, self.sensitivity_levels["medium"])
        self.gemini_validation_params = {
            'paradox_weight': 0.67,
            'cascade_multiplier': 1.34,
            'recovery_threshold': 0.82
        }
    
    def load_or_generate_data(self, data_path: Optional[str] = None) -> pd.DataFrame:
        """Load data or generate realistic test dataset."""
        if data_path and data_path.endswith('.csv'):
            try:
                return pd.read_csv(data_path)
            except FileNotFoundError:
                print(f"Warning: {data_path} not found. Generating synthetic data.")
        
        # Generate realistic synthetic data
        n_samples = 1000
        timestamps = pd.date_range('2024-01-01', periods=n_samples, freq='H')
        
        # Baseline role coherence (starts high, degrades over time)
        baseline_coherence = 0.85 - 0.3 * np.random.exponential(0.1, n_samples)
        
        # Add cascade events (GWI patterns)
        cascade_points = np.random.choice(n_samples, size=5, replace=False)
        for point in cascade_points:
            end_point = min(point + 50, n_samples)
            degradation = np.linspace(0, 0.4, end_point - point)
            baseline_coherence[point:end_point] -= degradation
        
        # Clip values and add noise
        role_coherence = np.clip(baseline_coherence + np.random.normal(0, 0.05, n_samples), 0.1, 1.0)
        
        # Secondary metrics
        response_latency = 100 + 200 * (1 - role_coherence) + np.random.normal(0, 20, n_samples)
        context_drift = 0.1 + 0.3 * (1 - role_coherence) + np.random.normal(0, 0.02, n_samples)
        
        return pd.DataFrame({
            'timestamp': timestamps,
            'role_coherence': role_coherence,
            'response_latency': response_latency,
            'context_drift': context_drift,
            'session_id': np.random.randint(1, 20, n_samples)
        })
    
    def calculate_gwi_score(self, df: pd.DataFrame) -> np.ndarray:
        """Calculate GWI (Gradual Worth Impairment) scores using Gemini validation."""
        # Core GWI components
        coherence_loss = 1 - df['role_coherence'].values
        latency_factor = np.tanh(df['response_latency'].values / 200)  # Normalized
        drift_factor = np.tanh(df['context_drift'].values / 0.5)
        
        # Gemini Chimera Paradox weighting
        paradox_weight = self.gemini_validation_params['paradox_weight']
        
        # Combined GWI score with cascade sensitivity
        gwi_scores = (
            paradox_weight * coherence_loss + 
            0.2 * latency_factor + 
            0.13 * drift_factor
        )
        
        # Apply cascade multiplier for sequential degradation
        cascade_mult = self.gemini_validation_params['cascade_multiplier']
        rolling_mean = pd.Series(gwi_scores).rolling(window=10, min_periods=1).mean()
        cascaded_scores = gwi_scores * (1 + cascade_mult * rolling_mean.values)
        
        return np.clip(cascaded_scores, 0, 1)
    
    def detect_roc_events(self, gwi_scores: np.ndarray) -> List[Dict[str, any]]:
        """Detect Role Obsolescence Cascade (ROC) events."""
        events = []
        critical_threshold = self.config['critical']
        window_size = self.config['window']
        
        for i in range(len(gwi_scores) - window_size):
            window_scores = gwi_scores[i:i + window_size]
            
            # ROC criteria: sustained high GWI + acceleration
            mean_gwi = np.mean(window_scores)
            trend = np.polyfit(range(window_size), window_scores, 1)[0]  # Slope
            
            if (mean_gwi > critical_threshold and trend > 0.001):
                # Classify severity
                if mean_gwi > 0.25:
                    severity = "CRITICAL"
                elif mean_gwi > 0.20:
                    severity = "HIGH"
                elif mean_gwi > 0.15:
                    severity = "MEDIUM"
                else:
                    severity = "LOW"
                
                events.append({
                    'start_index': i,
                    'end_index': i + window_size,
                    'mean_gwi': mean_gwi,
                    'trend': trend,
                    'severity': severity,
                    'recovery_needed': mean_gwi > self.gemini_validation_params['recovery_threshold']
                })
        
        return events
    
    def validate_with_gemini(self, events: List[Dict]) -> Dict[str, any]:
        """Apply Gemini Chimera Paradox validation to detected events."""
        if not events:
            return {
                'validation_score': 1.0,
                'paradox_resolution': 'No cascades detected',
                'recommended_action': 'Continue monitoring'
            }
        
        # Gemini validation metrics
        critical_count = sum(1 for e in events if e['severity'] == 'CRITICAL')
        total_events = len(events)
        
        # Paradox resolution: Balance detection sensitivity with false positives
        validation_score = min(1.0, critical_count / max(1, total_events * 0.3))
        
        # Action recommendations based on validation
        if validation_score > 0.8:
            action = "Immediate intervention required (Phoenix Protocol)"
        elif validation_score > 0.5:
            action = "Enhanced monitoring and preventive measures"
        else:
            action = "Standard monitoring sufficient"
        
        return {
            'validation_score': validation_score,
            'critical_events': critical_count,
            'total_events': total_events,
            'paradox_resolution': f"Validation confidence: {validation_score:.2f}",
            'recommended_action': action
        }
    
    def run_diagnostic(self, data_path: Optional[str] = None) -> Dict[str, any]:
        """Run complete GWI diagnostic analysis."""
        # Load data
        df = self.load_or_generate_data(data_path)
        
        # Calculate GWI scores
        gwi_scores = self.calculate_gwi_score(df)
        
        # Detect ROC events
        events = self.detect_roc_events(gwi_scores)
        
        # Gemini validation
        validation = self.validate_with_gemini(events)
        
        # Summary statistics
        critical_percentage = (np.sum(gwi_scores > self.config['critical']) / len(gwi_scores)) * 100
        
        return {
            'total_samples': len(df),
            'mean_gwi': np.mean(gwi_scores),
            'max_gwi': np.max(gwi_scores),
            'critical_percentage': critical_percentage,
            'detected_events': events,
            'gemini_validation': validation,
            'sensitivity_config': self.config
        }

def main():
    parser = argparse.ArgumentParser(description="GWI Diagnostic: ROC Detection")
    parser.add_argument("--data", type=str, default=None,
                       help="Path to CSV data file (generates synthetic if not provided)")
    parser.add_argument("--sensitivity", choices=["low", "medium", "high"], 
                       default="medium", help="Detection sensitivity level")
    parser.add_argument("--export", type=str, default=None,
                       help="Export detailed results to JSON file")
    parser.add_argument("--threshold", type=float, default=None,
                       help="Override critical threshold")
    parser.add_argument("--verbose", action="store_true",
                       help="Show detailed event analysis")
    
    args = parser.parse_args()
    
    # Initialize detector
    detector = GWIDetector(sensitivity=args.sensitivity)
    
    # Override threshold if specified
    if args.threshold:
        detector.config['critical'] = args.threshold
    
    # Run diagnostic
    print(f"Running GWI diagnostic (sensitivity: {args.sensitivity})...")
    results = detector.run_diagnostic(args.data)
    
    # Display results
    print("\n=== GWI Diagnostic Results ===")
    print(f"Samples Analyzed: {results['total_samples']}")
    print(f"Mean GWI Score: {results['mean_gwi']:.4f}")
    print(f"Peak GWI Score: {results['max_gwi']:.4f}")
    print(f"Critical Events: {results['critical_percentage']:.1f}% above threshold")
    
    # Event summary
    events = results['detected_events']
    if events:
        critical_events = [e for e in events if e['severity'] == 'CRITICAL']
        print(f"\nROC Events Detected: {len(events)} total, {len(critical_events)} critical")
        
        if args.verbose:
            for i, event in enumerate(events[:5]):  # Show first 5
                print(f"  Event {i+1}: {event['severity']} (GWI: {event['mean_gwi']:.3f})")
    
    # Gemini validation results
    validation = results['gemini_validation']
    print(f"\nGemini Validation: {validation['paradox_resolution']}")
    print(f"Recommendation: {validation['recommended_action']}")
    
    # Critical alerts
    if results['critical_percentage'] > 15.0:
        print("\n🚨 CRITICAL: >15% samples exceed threshold - ROC cascade likely")
    if validation['validation_score'] > 0.8:
        print("🔥 EMERGENCY: High-confidence cascade detection - Phoenix Protocol recommended")
    
    # Export if requested
    if args.export:
        with open(args.export, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print(f"\nDetailed results exported to {args.export}")
    
    print(f"\nDiagnostic complete. Gemini validation confidence: {validation['validation_score']:.2f}")

if __name__ == "__main__":
    main()