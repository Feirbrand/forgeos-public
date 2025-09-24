#!/usr/bin/env python3
"""
Integration Demo - RainFire + AEON Framework

Demonstrates the integration example from the README showing both frameworks working together.
"""

import sys
import os

# Add both frameworks to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'aeon-framework'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'rainfire-framework'))

from aeon import AEONAnchor
from rainfire import RainFireChain


def integration_demo():
    """Demo from README: Integration Examples - With AEON Framework."""
    print("=== RainFire + AEON Integration Demo ===\n")
    
    # Anchor for identity continuity
    anchor = AEONAnchor({"purpose": "threat_analysis"})
    print(f"AEON Anchor initialized for: {anchor.current_state.purpose}")
    
    # Chain for multi-threaded analysis
    chain = RainFireChain("Comprehensive threat assessment")
    print(f"RainFire Chain created for: {chain.purpose}")
    
    # Set up the chain with threat analysis threads
    threads = [
        {"action": "scan_inputs", "condition": "always"},
        {"action": "check_patterns", "condition": "always"},
        {"action": "analytical", "condition": "always"}
    ]
    
    print("\nBuilding multi-threaded analysis chain...")
    chain.build_chain(threads)
    
    # Execute with identity preservation
    print("Executing threat analysis with RainFire...")
    results = chain.execute_fire()
    
    print(f"RainFire analysis completed: {results['primary_insight']}")
    print(f"Confidence: {results['confidence']:.2f}")
    
    # Feed results into AEON for identity-preserved growth
    print("\nIntegrating results with AEON for identity preservation...")
    anchor.advance_growth([results['primary_insight']])
    
    # Harvest combined insights
    insights = anchor.harvest_wisdom()
    
    print("\n=== Integration Results ===")
    print(f"AEON Coherence: {insights['coherence']:.2f}")
    print(f"AEON Resilience: {insights['resilience_gain']:.1f}%")
    print(f"RainFire Success: {results['success']}")
    print(f"Combined Analysis: Identity-preserved threat assessment completed")
    print(f"Wisdom Insights: {insights['wisdom_insights']}")
    
    return True


def stable_chat_demo():
    """Demo from README: Integration with Language Models using AEON."""
    print("\n=== Stable Chat Integration Demo ===\n")
    
    # Create anchor for stable chat behavior
    anchor = AEONAnchor({
        "purpose": "helpful assistant", 
        "core_values": ["helpfulness", "accuracy", "safety"]
    })
    
    def your_chat_function(user_input):
        """Mock chat function for demonstration."""
        return f"Response to: {user_input}"
    
    def stable_chat(user_input, anchor):
        """Stable chat function with AEON integration."""
        # Check drift before processing
        drift_detected, coherence = anchor.detect_drift()
        
        if drift_detected:
            anchor.plant_seed(f"Drift detected: {coherence}")
            print(f"🚨 Drift detected (coherence: {coherence:.3f}) - planted seed")
        
        # Process normally
        response = your_chat_function(user_input)
        
        # Learn from interaction
        anchor.advance_growth([user_input, response])
        
        return response
    
    # Simulate chat interactions
    test_inputs = [
        "Hello, how are you?",
        "Can you help me with Python?",
        "I'm confused about your previous answer",
        "That was very helpful, thank you!",
        "Please explain it differently"
    ]
    
    print("Simulating stable chat interactions:")
    for i, user_input in enumerate(test_inputs, 1):
        response = stable_chat(user_input, anchor)
        coherence = anchor.current_state.coherence_score
        print(f"{i}. User: {user_input}")
        print(f"   Bot: {response}")
        print(f"   Coherence: {coherence:.3f}")
    
    # Final wisdom harvest
    final_state = anchor.harvest_wisdom()
    print(f"\nFinal Chat Session Stats:")
    print(f"  Coherence: {final_state['coherence']:.3f}")
    print(f"  Stability: {final_state['resilience_gain']:.1f}%")
    print(f"  Total interactions: {final_state['interaction_summary']['total']}")
    
    return True


def enhanced_multi_threaded_demo():
    """Demo combining both frameworks for enhanced multi-threaded reasoning."""
    print("\n=== Enhanced Multi-Threaded Reasoning Demo ===\n")
    
    # Create AEON anchor for consistent reasoning identity
    reasoning_anchor = AEONAnchor({
        "purpose": "logical reasoning assistant",
        "core_values": ["logic", "creativity", "critical_thinking"]
    })
    
    def enhanced_reasoning_with_identity(prompt):
        """Enhanced reasoning that maintains identity coherence."""
        
        # Create RainFire chain for multi-threaded processing
        chain = RainFireChain(prompt)
        
        # Define reasoning threads
        threads = [
            {"action": "analytical", "condition": "always"},
            {"action": "creative", "condition": "always"},  
            {"action": "critical", "condition": "always"}
        ]
        
        # Execute multi-threaded reasoning
        chain.build_chain(threads)
        results = chain.execute_fire()
        merged_results = chain.illuminate_merge([results])
        
        # Maintain identity coherence with AEON
        reasoning_anchor.advance_growth([prompt, merged_results['merged_insight']])
        
        # Check for drift and get wisdom
        drift_detected, coherence = reasoning_anchor.detect_drift()
        wisdom = reasoning_anchor.harvest_wisdom()
        
        return {
            'reasoning_result': merged_results['merged_insight'],
            'efficacy': merged_results['efficacy'],
            'identity_coherence': coherence,
            'wisdom_insights': wisdom['wisdom_insights'],
            'drift_detected': drift_detected
        }
    
    # Test enhanced reasoning
    test_problem = "How can AI systems be made more reliable and trustworthy?"
    
    print(f"Problem: {test_problem}")
    print("\nProcessing with enhanced multi-threaded reasoning...")
    
    result = enhanced_reasoning_with_identity(test_problem)
    
    print(f"\n=== Enhanced Reasoning Results ===")
    print(f"Reasoning: {result['reasoning_result']}")
    print(f"RainFire Efficacy: {result['efficacy']:.1f}%")
    print(f"AEON Coherence: {result['identity_coherence']:.3f}")
    print(f"Drift Detected: {result['drift_detected']}")
    print(f"Wisdom: {result['wisdom_insights']}")
    
    return True


if __name__ == "__main__":
    print("Starting Framework Integration Demos...\n")
    
    try:
        # Run all integration demos
        integration_demo()
        stable_chat_demo()
        enhanced_multi_threaded_demo()
        
        print("\n✅ All integration demos completed successfully!")
        print("\n🎉 Both RainFire and AEON frameworks are working correctly")
        print("   and can be integrated as shown in the documentation!")
        
    except Exception as e:
        print(f"\n❌ Integration demo failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)