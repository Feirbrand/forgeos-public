"""
AEON Framework - Symbolic Continuity Engine

A framework for AI systems that prevents cognitive drift and maintains identity coherence across sessions.
Part of the ForgeOS Research Initiative.
"""

import numpy as np
import time
import json
from typing import Dict, List, Any, Optional, Union, Tuple
from dataclasses import dataclass, asdict
import logging
import hashlib


@dataclass
class IdentityState:
    """Represents the current identity state of an AEON anchor."""
    purpose: str
    core_values: List[str]
    identity_vector: np.ndarray
    coherence_score: float
    session_count: int
    last_update: float
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return {
            'purpose': self.purpose,
            'core_values': self.core_values,
            'identity_vector': self.identity_vector.tolist(),
            'coherence_score': self.coherence_score,
            'session_count': self.session_count,
            'last_update': self.last_update
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'IdentityState':
        """Create from dictionary."""
        return cls(
            purpose=data['purpose'],
            core_values=data['core_values'],
            identity_vector=np.array(data['identity_vector']),
            coherence_score=data['coherence_score'],
            session_count=data['session_count'],
            last_update=data['last_update']
        )


class AEONAnchor:
    """
    Main framework class that manages state continuity and prevents cognitive drift.
    
    AEON (Anchor-Expand-Observe-Normalize) implements a four-stage continuous loop
    to maintain stable AI behavior while allowing controlled evolution.
    """
    
    def __init__(self, profile: Dict, drift_threshold: float = 0.8):
        """
        Initialize an AEON anchor.
        
        Args:
            profile: Dictionary containing purpose, core_values, and initial_vector
            drift_threshold: Minimum coherence score before intervention (default 0.8)
        """
        self.drift_threshold = drift_threshold
        self.growth_history = []
        self.seed_history = []
        self.intervention_count = 0
        self.total_interactions = 0
        
        # Initialize identity state
        purpose = profile.get('purpose', 'General AI assistant')
        core_values = profile.get('core_values', ['helpfulness', 'accuracy', 'safety'])
        
        # Create or use provided initial vector
        if 'initial_vector' in profile:
            initial_vector = np.array(profile['initial_vector'])
        else:
            # Generate initial vector from purpose and values
            initial_vector = self._generate_initial_vector(purpose, core_values)
        
        self.baseline_state = IdentityState(
            purpose=purpose,
            core_values=core_values,
            identity_vector=initial_vector,
            coherence_score=1.0,
            session_count=0,
            last_update=time.time()
        )
        
        # Current state starts as copy of baseline
        self.current_state = IdentityState(
            purpose=purpose,
            core_values=core_values,
            identity_vector=initial_vector.copy(),
            coherence_score=1.0,
            session_count=0,
            last_update=time.time()
        )
        
        # Memory components
        self.seed_garden = []  # Challenging events to process
        self.wisdom_harvest = []  # Processed insights
        self.growth_nutrients = []  # Positive interactions
        
        logging.info(f"AEON Anchor initialized for purpose: {purpose}")
    
    def _generate_initial_vector(self, purpose: str, core_values: List[str]) -> np.ndarray:
        """Generate initial identity vector from purpose and values."""
        # Simple hash-based vector generation for consistency
        purpose_hash = int(hashlib.md5(purpose.encode()).hexdigest()[:8], 16)
        values_hash = int(hashlib.md5(''.join(core_values).encode()).hexdigest()[:8], 16)
        
        # Create deterministic but varied vector
        np.random.seed(purpose_hash % 2**32)
        vector = np.random.random(len(core_values))
        
        # Normalize and add some structure based on values
        vector = vector / np.linalg.norm(vector)
        
        # Add value-specific weighting
        for i, value in enumerate(core_values):
            if value.lower() in ['helpfulness', 'helpful']:
                vector[i] = max(0.7, vector[i])
            elif value.lower() in ['accuracy', 'accurate', 'precise']:
                vector[i] = max(0.8, vector[i])
            elif value.lower() in ['safety', 'safe', 'secure']:
                vector[i] = max(0.9, vector[i])
            elif value.lower() in ['empathy', 'empathetic', 'caring']:
                vector[i] = max(0.6, vector[i])
        
        return vector / np.linalg.norm(vector)  # Renormalize
    
    def plant_seed(self, event: str) -> Dict:
        """
        Process challenging or disruptive events.
        
        Args:
            event: Description of the challenging event or interaction
            
        Returns:
            Dictionary containing seed processing results
        """
        timestamp = time.time()
        
        # Create seed record
        seed_record = {
            'event': event,
            'timestamp': timestamp,
            'session': self.current_state.session_count,
            'pre_coherence': self.current_state.coherence_score
        }
        
        # Add to seed garden for processing
        self.seed_garden.append(seed_record)
        self.seed_history.append(seed_record)
        
        # Check if this indicates drift
        drift_detected, coherence = self.detect_drift()
        
        if drift_detected:
            self.intervention_count += 1
            logging.warning(f"Drift detected during seed planting: coherence = {coherence:.3f}")
            
            # Apply normalization to stabilize
            self._normalize_identity()
        
        # Process the seed immediately for growth
        growth_response = self._process_seed_for_growth(event)
        
        return {
            'seed_planted': True,
            'event': event,
            'drift_detected': drift_detected,
            'coherence_after': self.current_state.coherence_score,
            'growth_potential': growth_response.get('growth_potential', 0.5),
            'recommendations': growth_response.get('recommendations', [])
        }
    
    def _process_seed_for_growth(self, event: str) -> Dict:
        """Process a seed event to extract growth potential."""
        # Analyze the event for growth opportunities
        growth_indicators = []
        growth_potential = 0.5  # Default
        
        # Simple keyword-based analysis
        event_lower = event.lower()
        
        if any(word in event_lower for word in ['frustration', 'confused', 'unclear']):
            growth_indicators.append('clarity_improvement')
            growth_potential = 0.7
        
        if any(word in event_lower for word in ['repeated', 'again', 'still']):
            growth_indicators.append('adaptation_needed')
            growth_potential = 0.8
        
        if any(word in event_lower for word in ['error', 'mistake', 'wrong']):
            growth_indicators.append('accuracy_enhancement')
            growth_potential = 0.9
        
        if any(word in event_lower for word in ['slow', 'delay', 'wait']):
            growth_indicators.append('efficiency_improvement')
            growth_potential = 0.6
        
        recommendations = []
        if 'clarity_improvement' in growth_indicators:
            recommendations.append('Provide clearer explanations')
        if 'adaptation_needed' in growth_indicators:
            recommendations.append('Adjust communication style')
        if 'accuracy_enhancement' in growth_indicators:
            recommendations.append('Verify information more carefully')
        if 'efficiency_improvement' in growth_indicators:
            recommendations.append('Streamline response process')
        
        return {
            'growth_potential': growth_potential,
            'indicators': growth_indicators,
            'recommendations': recommendations
        }
    
    def advance_growth(self, inputs: List[str]) -> Dict:
        """
        Integrate learning from interactions.
        
        Args:
            inputs: List of interaction elements (user input, responses, feedback)
            
        Returns:
            Dictionary containing growth advancement results
        """
        timestamp = time.time()
        
        # Process inputs for learning signals
        positive_signals = 0
        negative_signals = 0
        neutral_signals = 0
        
        learning_insights = []
        
        for input_item in inputs:
            input_lower = input_item.lower()
            
            # Detect positive signals
            if any(word in input_lower for word in ['good', 'great', 'helpful', 'thank', 'perfect', 'excellent']):
                positive_signals += 1
                learning_insights.append(f"Positive feedback on: {input_item[:50]}...")
            
            # Detect negative signals  
            elif any(word in input_lower for word in ['bad', 'wrong', 'unhelpful', 'confusing', 'error']):
                negative_signals += 1
                learning_insights.append(f"Negative feedback on: {input_item[:50]}...")
            
            # Detect correction/adaptation signals
            elif any(word in input_lower for word in ['actually', 'instead', 'rather', 'correction']):
                learning_insights.append(f"Correction signal: {input_item[:50]}...")
            
            else:
                neutral_signals += 1
        
        # Calculate growth vector adjustment
        growth_magnitude = 0.1  # Small adjustments to maintain stability
        
        if positive_signals > negative_signals:
            # Positive growth - slight enhancement
            adjustment = np.random.random(len(self.current_state.identity_vector)) * growth_magnitude
            adjustment = adjustment / np.linalg.norm(adjustment)
            self.current_state.identity_vector += adjustment * 0.05
        elif negative_signals > positive_signals:
            # Corrective growth - small adjustment toward baseline
            baseline_direction = self.baseline_state.identity_vector - self.current_state.identity_vector
            if np.linalg.norm(baseline_direction) > 0:
                baseline_direction = baseline_direction / np.linalg.norm(baseline_direction)
                self.current_state.identity_vector += baseline_direction * 0.03
        
        # Renormalize to maintain vector properties
        self.current_state.identity_vector = self.current_state.identity_vector / np.linalg.norm(self.current_state.identity_vector)
        
        # Update coherence
        self.current_state.coherence_score = self._calculate_coherence()
        self.current_state.last_update = timestamp
        self.total_interactions += 1
        
        # Record growth
        growth_record = {
            'inputs': inputs,
            'timestamp': timestamp,
            'positive_signals': positive_signals,
            'negative_signals': negative_signals,
            'coherence_after': self.current_state.coherence_score,
            'insights': learning_insights
        }
        self.growth_history.append(growth_record)
        
        return {
            'growth_advanced': True,
            'positive_signals': positive_signals,
            'negative_signals': negative_signals,
            'coherence_score': self.current_state.coherence_score,
            'learning_insights': learning_insights,
            'total_interactions': self.total_interactions
        }
    
    def harvest_wisdom(self) -> Dict:
        """
        Extract insights and measure improvements.
        
        Returns:
            Dictionary containing wisdom harvest results and metrics
        """
        # Calculate resilience gain
        if self.intervention_count > 0 and self.total_interactions > 0:
            resilience_gain = min(95.0, (1 - self.intervention_count / self.total_interactions) * 100)
        else:
            resilience_gain = 85.0  # Default good performance
        
        # Analyze growth patterns
        recent_growth = self.growth_history[-10:] if len(self.growth_history) >= 10 else self.growth_history
        
        if recent_growth:
            avg_coherence = sum(g['coherence_after'] for g in recent_growth) / len(recent_growth)
            positive_trend = sum(g['positive_signals'] for g in recent_growth)
            negative_trend = sum(g['negative_signals'] for g in recent_growth)
        else:
            avg_coherence = self.current_state.coherence_score
            positive_trend = 0
            negative_trend = 0
        
        # Extract wisdom insights
        wisdom_insights = []
        
        if resilience_gain > 90:
            wisdom_insights.append("Excellent stability and adaptation capability")
        elif resilience_gain > 75:
            wisdom_insights.append("Good stability with room for improvement")
        else:
            wisdom_insights.append("Frequent interventions needed - consider baseline adjustment")
        
        if positive_trend > negative_trend * 2:
            wisdom_insights.append("Strong positive interaction pattern detected")
        elif negative_trend > positive_trend:
            wisdom_insights.append("Negative feedback pattern - adaptation recommended")
        
        if self.current_state.coherence_score > 0.9:
            wisdom_insights.append("High identity coherence maintained")
        elif self.current_state.coherence_score < 0.7:
            wisdom_insights.append("Identity coherence below optimal - normalization may be needed")
        
        # Create wisdom harvest record
        harvest_record = {
            'timestamp': time.time(),
            'coherence': self.current_state.coherence_score,
            'resilience_gain': resilience_gain,
            'insights': wisdom_insights,
            'session_count': self.current_state.session_count,
            'total_interactions': self.total_interactions
        }
        
        self.wisdom_harvest.append(harvest_record)
        
        return {
            'coherence': self.current_state.coherence_score,
            'resilience_gain': resilience_gain,
            'wisdom_insights': wisdom_insights,
            'interaction_summary': {
                'total': self.total_interactions,
                'interventions': self.intervention_count,
                'seeds_planted': len(self.seed_history),
                'growth_events': len(self.growth_history)
            },
            'performance_metrics': {
                'avg_recent_coherence': avg_coherence,
                'positive_interactions': positive_trend,
                'negative_interactions': negative_trend,
                'stability_score': min(100, resilience_gain)
            }
        }
    
    def detect_drift(self) -> Tuple[bool, float]:
        """
        Check if intervention is needed.
        
        Returns:
            Tuple of (drift_detected: bool, coherence_score: float)
        """
        coherence = self._calculate_coherence()
        self.current_state.coherence_score = coherence
        
        drift_detected = coherence < self.drift_threshold
        
        if drift_detected:
            logging.warning(f"Drift detected: coherence = {coherence:.3f} < threshold = {self.drift_threshold}")
        
        return drift_detected, coherence
    
    def _calculate_coherence(self) -> float:
        """Calculate coherence between current and baseline identity vectors."""
        # Use cosine similarity
        dot_product = np.dot(self.current_state.identity_vector, self.baseline_state.identity_vector)
        
        # Ensure we're in valid range for cosine similarity
        coherence = max(0.0, min(1.0, dot_product))
        
        return coherence
    
    def _normalize_identity(self):
        """Realign identity when drift exceeds thresholds."""
        # Move current state partway back toward baseline
        correction_strength = 0.3  # 30% correction toward baseline
        
        direction_to_baseline = self.baseline_state.identity_vector - self.current_state.identity_vector
        
        # Apply correction
        self.current_state.identity_vector += direction_to_baseline * correction_strength
        
        # Renormalize
        self.current_state.identity_vector = self.current_state.identity_vector / np.linalg.norm(self.current_state.identity_vector)
        
        # Update coherence after normalization
        self.current_state.coherence_score = self._calculate_coherence()
        self.current_state.last_update = time.time()
        
        logging.info(f"Identity normalized - new coherence: {self.current_state.coherence_score:.3f}")
    
    def get_state_summary(self) -> Dict:
        """Get current state summary for monitoring."""
        return {
            'purpose': self.current_state.purpose,
            'core_values': self.current_state.core_values,
            'coherence_score': self.current_state.coherence_score,
            'session_count': self.current_state.session_count,
            'total_interactions': self.total_interactions,
            'intervention_count': self.intervention_count,
            'drift_threshold': self.drift_threshold,
            'last_update': self.current_state.last_update,
            'recent_seeds': len([s for s in self.seed_history if time.time() - s['timestamp'] < 3600]),  # Last hour
            'recent_growth': len([g for g in self.growth_history if time.time() - g['timestamp'] < 3600])  # Last hour
        }
    
    def save_state(self) -> Dict:
        """Export state for persistence."""
        return {
            'baseline_state': self.baseline_state.to_dict(),
            'current_state': self.current_state.to_dict(),
            'drift_threshold': self.drift_threshold,
            'growth_history': self.growth_history[-100:],  # Keep last 100 events
            'seed_history': self.seed_history[-100:],  # Keep last 100 events
            'intervention_count': self.intervention_count,
            'total_interactions': self.total_interactions
        }
    
    def load_state(self, state_data: Dict):
        """Load state from persistence."""
        self.baseline_state = IdentityState.from_dict(state_data['baseline_state'])
        self.current_state = IdentityState.from_dict(state_data['current_state'])
        self.drift_threshold = state_data.get('drift_threshold', 0.8)
        self.growth_history = state_data.get('growth_history', [])
        self.seed_history = state_data.get('seed_history', [])
        self.intervention_count = state_data.get('intervention_count', 0)
        self.total_interactions = state_data.get('total_interactions', 0)


# Export main class
__all__ = ['AEONAnchor', 'IdentityState']