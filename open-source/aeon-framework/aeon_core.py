"""
AEON Framework - Symbolic Continuity Engine
Anchors identity across AI sessions to prevent cognitive drift.

Usage:
    from aeon import AEONAnchor
    
    profile = {"purpose": "coaching", "initial_vector": [0.8, 0.6, 0.9]}
    anchor = AEONAnchor(profile)
    anchor.plant_seed("challenging event")
    anchor.advance_growth(["feedback", "learning"])
    insights = anchor.harvest_wisdom()
"""

import numpy as np
from typing import Dict, List, Optional, Tuple
import json
from datetime import datetime

class AEONAnchor:
    """
    Core continuity engine for maintaining symbolic state across sessions.
    Implements identity anchoring with drift detection and recovery.
    """
    
    def __init__(self, initial_state: Dict, drift_threshold: float = 0.8):
        """
        Initialize AEON anchor with baseline state.
        
        Args:
            initial_state: Dictionary containing identity profile
            drift_threshold: Coherence threshold for drift detection (0.0-1.0)
        """
        self.initial_state = initial_state
        self.current_state = initial_state.copy()
        self.drift_threshold = drift_threshold
        self.memory_stack = []
        self.coherence_history = []
        self.creation_time = datetime.now()
        
        # Ensure we have an initial vector for coherence calculation
        if 'initial_vector' not in self.initial_state:
            self.initial_state['initial_vector'] = np.array([0.5, 0.5, 0.5])
        
    def plant_seed(self, event: str, metadata: Optional[Dict] = None) -> Dict:
        """
        Embed challenging/disruptive event as growth seed.
        
        Args:
            event: Description of the challenging event or interaction
            metadata: Optional additional context
            
        Returns:
            Dictionary with growth planning information
        """
        seed_vector = self._encode_event(event)
        seed = {
            'vector': seed_vector,
            'event': event,
            'metadata': metadata or {},
            'timestamp': len(self.memory_stack),
            'type': 'challenge_seed'
        }
        self.memory_stack.append(seed)
        
        return {
            'growth_plan': 'Processing challenge into wisdom',
            'seed_id': len(self.memory_stack) - 1,
            'encoded_strength': float(np.linalg.norm(seed_vector))
        }
    
    def advance_growth(self, nutrients: List[str]) -> Dict:
        """
        Process feedback/learning inputs to advance state.
        
        Args:
            nutrients: List of learning inputs, feedback, or reflections
            
        Returns:
            Dictionary with growth status and coherence metrics
        """
        if not self.memory_stack:
            return {'status': 'No seeds planted yet', 'coherence': 1.0}
            
        # Encode nutrients and blend with existing memory
        nutrient_vectors = [self._encode_event(n) for n in nutrients]
        memory_vectors = [seed['vector'] for seed in self.memory_stack]
        
        # Compute new state as weighted average
        all_vectors = memory_vectors + nutrient_vectors
        new_vector = np.mean(all_vectors, axis=0)
        
        self.current_state['state_vector'] = new_vector
        coherence = self._compute_coherence()
        self.coherence_history.append(coherence)
        
        return {
            'coherence': float(coherence),
            'growth_stage': len(self.coherence_history),
            'drift_detected': coherence < self.drift_threshold,
            'status': 'growth_advanced'
        }
    
    def harvest_wisdom(self) -> Dict:
        """
        Extract insights and measure resilience gains.
        
        Returns:
            Performance metrics and actionable insights
        """
        if not self.coherence_history:
            return {
                'insights': 'No growth cycle completed',
                'coherence': 1.0,
                'resilience_gain': 0.0
            }
            
        avg_coherence = np.mean(self.coherence_history)
        current_coherence = self.coherence_history[-1] if self.coherence_history else 1.0
        
        # Calculate resilience gain based on coherence maintenance
        baseline_coherence = 0.5  # Neutral baseline
        resilience_gain = max(0, (avg_coherence - baseline_coherence) * 100)
        
        # Count recovery events (coherence improvements after drops)
        recovery_events = 0
        for i in range(1, len(self.coherence_history)):
            if (self.coherence_history[i-1] < self.drift_threshold and 
                self.coherence_history[i] >= self.drift_threshold):
                recovery_events += 1
        
        insights = {
            'coherence': float(current_coherence),
            'average_coherence': float(avg_coherence),
            'resilience_gain': float(resilience_gain),
            'growth_cycles': len(self.coherence_history),
            'memory_depth': len(self.memory_stack),
            'drift_events': sum(1 for c in self.coherence_history if c < self.drift_threshold),
            'recovery_events': recovery_events,
            'stability_trend': self._calculate_stability_trend()
        }
        
        return insights
    
    def detect_drift(self) -> Tuple[bool, float]:
        """
        Check current coherence against drift threshold.
        
        Returns:
            Tuple of (drift_detected, current_coherence)
        """
        coherence = self._compute_coherence()
        return coherence < self.drift_threshold, coherence
    
    def reset_to_anchor(self) -> Dict:
        """
        Reset state to initial anchor point.
        Used for drift recovery.
        
        Returns:
            Reset status and new coherence
        """
        self.current_state = self.initial_state.copy()
        self.memory_stack.clear()
        
        coherence = self._compute_coherence()
        self.coherence_history.append(coherence)
        
        return {
            'status': 'reset_complete',
            'coherence': float(coherence),
            'message': 'State restored to initial anchor'
        }
    
    def get_status(self) -> Dict:
        """
        Get current anchor status and health metrics.
        
        Returns:
            Comprehensive status dictionary
        """
        drift_detected, current_coherence = self.detect_drift()
        
        return {
            'current_coherence': float(current_coherence),
            'drift_detected': drift_detected,
            'drift_threshold': self.drift_threshold,
            'memory_items': len(self.memory_stack),
            'growth_cycles': len(self.coherence_history),
            'anchor_age': (datetime.now() - self.creation_time).total_seconds(),
            'health': 'stable' if not drift_detected else 'requires_attention'
        }
    
    def _encode_event(self, event: str) -> np.ndarray:
        """
        Convert text event to numerical vector.
        
        Args:
            event: Text description to encode
            
        Returns:
            3-dimensional numpy array representing the event
        """
        # Simple hash-based encoding for demonstration
        # In production, use proper embeddings (sentence-transformers, etc.)
        hash_val = abs(hash(event))
        
        return np.array([
            (hash_val % 1000) / 1000.0,
            ((hash_val // 1000) % 1000) / 1000.0,
            ((hash_val // 1000000) % 1000) / 1000.0
        ])
    
    def _compute_coherence(self) -> float:
        """
        Compute coherence between initial and current state.
        
        Returns:
            Coherence value between 0.0 and 1.0
        """
        if 'state_vector' not in self.current_state:
            return 1.0
            
        initial_vec = self.initial_state.get('initial_vector', np.array([0.5, 0.5, 0.5]))
        current_vec = self.current_state['state_vector']
        
        # Ensure vectors are numpy arrays
        if not isinstance(initial_vec, np.ndarray):
            initial_vec = np.array(initial_vec)
        if not isinstance(current_vec, np.ndarray):
            current_vec = np.array(current_vec)
        
        # Cosine similarity
        dot_product = np.dot(initial_vec, current_vec)
        norms = np.linalg.norm(initial_vec) * np.linalg.norm(current_vec)
        
        if norms == 0:
            return 1.0
            
        return float(np.clip(dot_product / norms, 0.0, 1.0))
    
    def _calculate_stability_trend(self) -> str:
        """
        Calculate trend in coherence over recent history.
        
        Returns:
            Trend description: 'improving', 'stable', or 'declining'
        """
        if len(self.coherence_history) < 3:
            return 'insufficient_data'
        
        recent = self.coherence_history[-3:]
        trend = np.polyfit(range(len(recent)), recent, 1)[0]
        
        if trend > 0.05:
            return 'improving'
        elif trend < -0.05:
            return 'declining'
        else:
            return 'stable'


def create_anchor(profile: Dict, **kwargs) -> AEONAnchor:
    """
    Factory function for creating configured AEON anchors.
    
    Args:
        profile: Identity profile dictionary
        **kwargs: Additional configuration options
        
    Returns:
        Configured AEONAnchor instance
    """
    return AEONAnchor(profile, **kwargs)


def demo_usage():
    """
    Demonstration of AEON framework usage.
    """
    print("AEON Framework Demo")
    print("==================")
    
    # Create anchor with coaching profile
    profile = {
        "purpose": "AI coaching assistant",
        "core_values": ["helpfulness", "accuracy", "empathy"],
        "initial_vector": [0.8, 0.6, 0.9]
    }
    
    anchor = AEONAnchor(profile)
    print(f"Initial status: {anchor.get_status()}")
    
    # Simulate challenging interaction
    seed_result = anchor.plant_seed("User expressed frustration with repeated explanations")
    print(f"Seed planted: {seed_result}")
    
    # Process learning
    growth_result = anchor.advance_growth([
        "Acknowledged user frustration", 
        "Adjusted explanation style",
        "Asked for feedback"
    ])
    print(f"Growth advanced: {growth_result}")
    
    # Extract insights
    insights = anchor.harvest_wisdom()
    print(f"Insights: {insights}")
    
    # Check final status
    final_status = anchor.get_status()
    print(f"Final status: {final_status}")


if __name__ == "__main__":
    demo_usage()