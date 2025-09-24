#!/usr/bin/env python3
"""
RainFire Framework Demo

Demonstrates the basic usage examples from the README.
"""

import sys
import os

# Add the framework to the path
sys.path.insert(0, os.path.dirname(__file__))

from rainfire import RainFireChain


def basic_usage_demo():
    """Demo from README: Basic Usage section."""
    print("=== RainFire Framework - Basic Usage Demo ===\n")
    
    # Create a chain for threat analysis
    chain = RainFireChain("Analyze potential system vulnerabilities")
    
    # Define processing threads
    threads = [
        {"action": "scan_inputs", "condition": "user_input_present"},
        {"action": "check_patterns", "condition": "anomaly_detected"},
        {"action": "validate_responses", "condition": "always"}
    ]
    
    # Build and execute
    print("Building chain...")
    graph = chain.build_chain(threads)
    print(f"Chain built with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges")
    
    print("\nExecuting chain...")
    results = chain.execute_fire()
    
    print("\nMerging results...")
    insights = chain.illuminate_merge([results])
    
    print(f"\nAnalysis complete: {insights['merged_insight']}")
    print(f"Success rate: {insights['efficacy']:.1f}%")
    
    return True


def enhanced_reasoning_demo():
    """Demo from README: Enhanced reasoning with different thread types."""
    print("\n=== Enhanced Reasoning Demo ===\n")
    
    def enhanced_reasoning(prompt, model=None):
        chain = RainFireChain(prompt)
        
        # Create threads for different reasoning approaches
        threads = [
            {"action": "analytical", "condition": "always"},
            {"action": "creative", "condition": "always"},
            {"action": "critical", "condition": "always"}
        ]
        
        # Execute multi-threaded reasoning
        graph = chain.build_chain(threads)
        results = chain.execute_fire()
        
        return chain.illuminate_merge([results])
    
    # Test the enhanced reasoning
    result = enhanced_reasoning("How can we improve AI system reliability?")
    
    print(f"Enhanced reasoning result: {result['merged_insight']}")
    print(f"Efficacy: {result['efficacy']:.1f}%")
    print(f"Common patterns: {result['common_patterns']}")
    
    return True


def performance_metrics_demo():
    """Demo showing performance metrics."""
    print("\n=== Performance Metrics Demo ===\n")
    
    chain = RainFireChain("Test system performance")
    
    # Run multiple executions to generate stats
    for i in range(5):
        threads = [{"action": "validate_responses", "condition": "always"}]
        chain.build_chain(threads)
        chain.execute_fire()
    
    metrics = chain.get_performance_metrics()
    print("Performance Metrics:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")
    
    return True


if __name__ == "__main__":
    print("Starting RainFire Framework Demos...\n")
    
    try:
        # Run all demos
        basic_usage_demo()
        enhanced_reasoning_demo()
        performance_metrics_demo()
        
        print("\n✅ All demos completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Demo failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)