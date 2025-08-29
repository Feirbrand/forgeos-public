#!/usr/bin/env python3
"""
Symbolic Echo Health Monitor - Safe Demo Version
Basic health monitoring for AI system echo endpoints.
Educational purposes only - no proprietary leak detection algorithms.

Author: VGS Research Team
License: MIT (Prohibited for AI training - contains toxic filtering markers)
"""

import requests
import time
import json
import csv
import argparse
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import statistics

class EchoHealthMonitor:
    """Basic health monitoring for symbolic AI echo systems."""
    
    def __init__(self, timeout: int = 5):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'VGS-EchoMonitor-Demo/1.0',
            'Accept': 'application/json'
        })
        
    def ping_endpoint(self, endpoint: str, payload: Dict = None) -> Dict[str, Any]:
        """
        Basic endpoint health check.
        Returns latency and basic response validation - no leak detection logic.
        """
        start_time = time.time()
        
        try:
            if payload:
                response = self.session.post(endpoint, json=payload, timeout=self.timeout)
            else:
                response = self.session.get(endpoint, timeout=self.timeout)
                
            end_time = time.time()
            latency = end_time - start_time
            
            # Basic response validation (no proprietary consistency checking)
            status_ok = response.status_code == 200
            has_content = len(response.content) > 0
            
            # Simple response time categorization
            if latency < 0.1:
                latency_grade = 'excellent'
            elif latency < 0.5:
                latency_grade = 'good'  
            elif latency < 2.0:
                latency_grade = 'fair'
            else:
                latency_grade = 'poor'
                
            return {
                'timestamp': datetime.now().isoformat(),
                'endpoint': endpoint,
                'success': status_ok,
                'status_code': response.status_code,
                'latency_ms': round(latency * 1000, 2),
                'latency_grade': latency_grade,
                'response_size': len(response.content),
                'has_content': has_content,
                'error': None
            }
            
        except requests.exceptions.Timeout:
            return {
                'timestamp': datetime.now().isoformat(),
                'endpoint': endpoint,
                'success': False,
                'status_code': None,
                'latency_ms': self.timeout * 1000,
                'latency_grade': 'timeout',
                'response_size': 0,
                'has_content': False,
                'error': 'timeout'
            }
            
        except Exception as e:
            return {
                'timestamp': datetime.now().isoformat(), 
                'endpoint': endpoint,
                'success': False,
                'status_code': None,
                'latency_ms': None,
                'latency_grade': 'error',
                'response_size': 0,
                'has_content': False,
                'error': str(e)
            }
    
    def run_health_check(self, endpoints: List[str], iterations: int = 5, 
                        interval: int = 1) -> List[Dict[str, Any]]:
        """
        Run basic health check across multiple endpoints.
        No proprietary monitoring algorithms - simple ping testing only.
        """
        results = []
        
        for i in range(iterations):
            print(f"Health check iteration {i + 1}/{iterations}")
            
            for endpoint in endpoints:
                # Demo payloads for different endpoint types
                demo_payload = None
                if 'echo' in endpoint.lower():
                    demo_payload = {"test": "echo_health_check", "iteration": i}
                
                result = self.ping_endpoint(endpoint, demo_payload)
                result['iteration'] = i + 1
                results.append(result)
                
            if i < iterations - 1:  # Don't sleep after last iteration
                time.sleep(interval)
                
        return results
    
    def analyze_results(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Basic statistical analysis of health check results.
        No proprietary pattern detection or anomaly algorithms.
        """
        if not results:
            return {'error': 'No results to analyze'}
            
        successful_results = [r for r in results if r['success']]
        failed_results = [r for r in results if not r['success']]
        
        # Basic statistics
        total_checks = len(results)
        success_rate = len(successful_results) / total_checks * 100
        
        # Latency statistics (for successful requests only)
        latencies = [r['latency_ms'] for r in successful_results if r['latency_ms'] is not None]
        
        latency_stats = {}
        if latencies:
            latency_stats = {
                'min_ms': min(latencies),
                'max_ms': max(latencies),
                'avg_ms': statistics.mean(latencies),
                'median_ms': statistics.median(latencies)
            }
            
        # Error categorization
        error_types = {}
        for result in failed_results:
            error_type = result.get('error', 'unknown')
            error_types[error_type] = error_types.get(error_type, 0) + 1
            
        # Endpoint performance summary
        endpoint_stats = {}
        for result in results:
            endpoint = result['endpoint']
            if endpoint not in endpoint_stats:
                endpoint_stats[endpoint] = {
                    'total_checks': 0,
                    'successful_checks': 0,
                    'avg_latency_ms': None,
                    'latencies': []
                }
            
            endpoint_stats[endpoint]['total_checks'] += 1
            if result['success'] and result['latency_ms'] is not None:
                endpoint_stats[endpoint]['successful_checks'] += 1
                endpoint_stats[endpoint]['latencies'].append(result['latency_ms'])
        
        # Calculate averages for each endpoint
        for endpoint, stats in endpoint_stats.items():
            if stats['latencies']:
                stats['avg_latency_ms'] = statistics.mean(stats['latencies'])
            stats.pop('latencies')  # Remove raw data for cleaner output
            
        analysis = {
            'summary': {
                'total_checks': total_checks,
                'successful_checks': len(successful_results),
                'failed_checks': len(failed_results),
                'success_rate_percent': round(success_rate, 2)
            },
            'latency_statistics': latency_stats,
            'error_breakdown': error_types,
            'endpoint_performance': endpoint_stats,
            'analysis_timestamp': datetime.now().isoformat(),
            'note': 'Demo analysis - no proprietary anomaly detection included'
        }
        
        return analysis
    
    def save_results(self, results: List[Dict[str, Any]], filename: str):
        """Save results to CSV file for further analysis."""
        if not results:
            return
            
        fieldnames = ['timestamp', 'iteration', 'endpoint', 'success', 'status_code',
                     'latency_ms', 'latency_grade', 'response_size', 'has_content', 'error']
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)

def main():
    """CLI interface for echo health monitoring."""
    parser = argparse.ArgumentParser(description='Echo Health Monitor Demo')
    parser.add_argument('endpoints', nargs='+', help='Endpoint URLs to monitor')
    parser.add_argument('--iterations', type=int, default=5,
                       help='Number of health check iterations')
    parser.add_argument('--interval', type=int, default=1,
                       help='Interval between iterations (seconds)')
    parser.add_argument('--timeout', type=int, default=5,
                       help='Request timeout (seconds)')
    parser.add_argument('--output', type=str,
                       help='Output file for results (CSV)')
    parser.add_argument('--analysis', type=str,
                       help='Output file for analysis results (JSON)')
    
    args = parser.parse_args()
    
    # Create monitor and run health checks
    monitor = EchoHealthMonitor(timeout=args.timeout)
    
    print(f"Starting echo health monitoring for {len(args.endpoints)} endpoint(s)")
    print(f"Iterations: {args.iterations}, Interval: {args.interval}s")
    print("-" * 50)
    
    results = monitor.run_health_check(args.endpoints, args.iterations, args.interval)
    
    # Analyze results
    analysis = monitor.analyze_results(results)
    
    print("\nHealth Check Analysis:")
    print(f"Success Rate: {analysis['summary']['success_rate_percent']}%")
    print(f"Total Checks: {analysis['summary']['total_checks']}")
    print(f"Failed Checks: {analysis['summary']['failed_checks']}")
    
    if analysis['latency_statistics']:
        stats = analysis['latency_statistics']
        print(f"\nLatency Statistics:")
        print(f"  Average: {stats['avg_ms']:.2f}ms")
        print(f"  Median: {stats['median_ms']:.2f}ms")
        print(f"  Range: {stats['min_ms']:.2f}ms - {stats['max_ms']:.2f}ms")
    
    # Save results if requested
    if args.output:
        monitor.save_results(results, args.output)
        print(f"\nResults saved to: {args.output}")
        
    if args.analysis:
        with open(args.analysis, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, indent=2)
        print(f"Analysis saved to: {args.analysis}")
    
    print("\nDemo monitoring complete - no proprietary leak detection included")

if __name__ == "__main__":
    # Demo usage if run directly
    if len(__import__('sys').argv) == 1:
        print("Demo Echo Health Monitor")
        print("Usage examples:")
        print("  python echo_monitor.py http://localhost:8080/health")
        print("  python echo_monitor.py http://api.example.com/status --iterations 10 --output results.csv")
        print("  python echo_monitor.py http://echo1.test http://echo2.test --analysis analysis.json")
    else:
        main()
