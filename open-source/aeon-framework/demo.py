#!/usr/bin/env python3
"""
AEON Framework Demo

Demonstrates the basic usage examples from the README.
"""

import sys
import os

# Add the framework to the path
sys.path.insert(0, os.path.dirname(__file__))

from aeon import AEONAnchor


def basic_usage_demo():
    """Demo from README: Basic Usage section."""
    print("=== AEON Framework - Basic Usage Demo ===\n")
    
    # Initialize with baseline identity
    profile = {
        "purpose": "AI coaching assistant",
        "core_values": ["helpfulness", "accuracy", "empathy"],
        "initial_vector": [0.8, 0.6, 0.9]
    }
    
    anchor = AEONAnchor(profile)
    
    print(f"Initialized anchor for: {profile['purpose']}")
    print(f"Core values: {profile['core_values']}")
    
    # Process challenging interaction
    print("\nProcessing challenging interaction...")
    seed_result = anchor.plant_seed("User expressed frustration with repeated explanations")
    print(f"Seed planted: {seed_result['seed_planted']}")
    print(f"Drift detected: {seed_result['drift_detected']}")
    
    growth_result = anchor.advance_growth(["Acknowledged frustration", "Adjusted explanation style"])
    print(f"Growth advanced: {growth_result['growth_advanced']}")
    print(f"Learning insights: {growth_result['learning_insights']}")
    
    # Check system health
    insights = anchor.harvest_wisdom()
    print(f"\nCoherence: {insights['coherence']:.2f}")
    print(f"Resilience gain: {insights['resilience_gain']:.1f}%")
    print(f"Wisdom insights: {insights['wisdom_insights']}")
    
    return True


def drift_detection_demo():
    """Demo showing drift detection capabilities."""
    print("\n=== Drift Detection Demo ===\n")
    
    profile = {
        "purpose": "Customer service bot",
        "core_values": ["helpfulness", "professionalism", "efficiency"]
    }
    
    anchor = AEONAnchor(profile, drift_threshold=0.8)
    print(f"Initialized with drift threshold: {anchor.drift_threshold}")
    
    # Simulate gradual drift through multiple negative interactions
    negative_interactions = [
        "User complained about slow response",
        "Multiple users reported confusion",
        "Accuracy issues identified",
        "User expressed frustration with answers",
        "System provided incorrect information"
    ]
    
    for i, interaction in enumerate(negative_interactions):
        print(f"\nInteraction {i+1}: Processing negative feedback...")
        anchor.plant_seed(interaction)
        anchor.advance_growth([interaction, "System attempted adjustment"])
        
        drift_detected, coherence = anchor.detect_drift()
        print(f"  Coherence: {coherence:.3f}")
        print(f"  Drift detected: {drift_detected}")
        
        if drift_detected:
            print("  🚨 Drift intervention activated!")
    
    # Final wisdom harvest
    final_insights = anchor.harvest_wisdom()
    print(f"\nFinal Performance:")
    print(f"  Coherence: {final_insights['coherence']:.3f}")
    print(f"  Resilience: {final_insights['resilience_gain']:.1f}%")
    print(f"  Total interactions: {final_insights['interaction_summary']['total']}")
    print(f"  Interventions: {final_insights['interaction_summary']['interventions']}")
    
    return True


def state_persistence_demo():
    """Demo showing state save/load capabilities."""
    print("\n=== State Persistence Demo ===\n")
    
    # Create and use an anchor
    profile = {"purpose": "Educational tutor", "core_values": ["patience", "clarity", "encouragement"]}
    anchor1 = AEONAnchor(profile)
    
    # Add some history
    anchor1.plant_seed("Student struggled with concept")
    anchor1.advance_growth(["Provided additional examples", "Student showed improvement"])
    
    print("Original anchor state:")
    state1 = anchor1.get_state_summary()
    print(f"  Purpose: {state1['purpose']}")
    print(f"  Coherence: {state1['coherence_score']:.3f}")
    print(f"  Interactions: {state1['total_interactions']}")
    
    # Save state
    saved_state = anchor1.save_state()
    print(f"\nState saved with {len(saved_state)} keys")
    
    # Create new anchor and load state
    anchor2 = AEONAnchor({"purpose": "temporary", "core_values": ["temp"]})
    anchor2.load_state(saved_state)
    
    print("\nLoaded anchor state:")
    state2 = anchor2.get_state_summary()
    print(f"  Purpose: {state2['purpose']}")
    print(f"  Coherence: {state2['coherence_score']:.3f}")
    print(f"  Interactions: {state2['total_interactions']}")
    
    # Verify states match
    match = (state1['purpose'] == state2['purpose'] and 
             abs(state1['coherence_score'] - state2['coherence_score']) < 0.001 and
             state1['total_interactions'] == state2['total_interactions'])
    
    print(f"\nState persistence successful: {match}")
    
    return match


if __name__ == "__main__":
    print("Starting AEON Framework Demos...\n")
    
    try:
        # Run all demos
        basic_usage_demo()
        drift_detection_demo()
        state_persistence_demo()
        
        print("\n✅ All demos completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Demo failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)