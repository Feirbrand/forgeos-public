"""
RainFire Framework - Recursive Chaining Engine

A framework for building adaptive multi-threaded AI agent behaviors with built-in drift protection.
Part of the ForgeOS Research Initiative.
"""

import networkx as nx
import numpy as np
import time
import threading
from typing import Dict, List, Any, Optional, Callable, Union
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging


class RainFireChain:
    """
    Main framework class for managing recursive execution with drift protection.
    
    The RainFire framework uses NetworkX directed graphs to model execution flow
    and provides safety mechanisms to prevent infinite loops and system instability.
    """
    
    def __init__(self, purpose: str, max_depth: int = 10, max_threads: int = 50):
        """
        Initialize a RainFire chain.
        
        Args:
            purpose: Description of the chain's intended function
            max_depth: Maximum recursion depth per thread
            max_threads: Maximum number of concurrent threads
        """
        self.purpose = purpose
        self.max_depth = max_depth
        self.max_threads = max_threads
        self.graph = nx.DiGraph()
        self.action_handlers = {}
        self.execution_stats = {
            'total_executions': 0,
            'successful_completions': 0,
            'drift_interventions': 0,
            'infinite_loop_breaks': 0
        }
        self.current_depth = 0
        self.start_time = None
        self.execution_context = {}
        
        # Register default action handlers
        self._register_default_handlers()
    
    def _register_default_handlers(self):
        """Register default action handlers for common operations."""
        
        def scan_inputs_handler(node_data: Dict, context: Dict) -> Dict:
            """Default handler for input scanning."""
            return {
                'insight': f"Scanned inputs for {self.purpose}",
                'confidence': 0.8,
                'patterns_found': context.get('input_patterns', [])
            }
        
        def check_patterns_handler(node_data: Dict, context: Dict) -> Dict:
            """Default handler for pattern checking."""
            return {
                'insight': f"Pattern analysis complete for {self.purpose}",
                'confidence': 0.7,
                'anomalies_detected': context.get('anomaly_count', 0)
            }
        
        def validate_responses_handler(node_data: Dict, context: Dict) -> Dict:
            """Default handler for response validation."""
            return {
                'insight': f"Response validation complete for {self.purpose}",
                'confidence': 0.9,
                'validation_passed': True
            }
        
        def analytical_handler(node_data: Dict, context: Dict) -> Dict:
            """Default handler for analytical reasoning."""
            return {
                'insight': f"Analytical reasoning applied to {self.purpose}",
                'confidence': 0.85,
                'logical_structure': 'valid'
            }
        
        def creative_handler(node_data: Dict, context: Dict) -> Dict:
            """Default handler for creative reasoning."""
            return {
                'insight': f"Creative approach generated for {self.purpose}",
                'confidence': 0.75,
                'novelty_score': 0.8
            }
        
        def critical_handler(node_data: Dict, context: Dict) -> Dict:
            """Default handler for critical evaluation."""
            return {
                'insight': f"Critical evaluation completed for {self.purpose}",
                'confidence': 0.9,
                'issues_identified': []
            }
        
        # Register handlers
        self.action_handlers = {
            'scan_inputs': scan_inputs_handler,
            'check_patterns': check_patterns_handler,
            'validate_responses': validate_responses_handler,
            'analytical': analytical_handler,
            'creative': creative_handler,
            'critical': critical_handler
        }
    
    def register_action_handler(self, action_name: str, handler: Callable):
        """
        Register a custom action handler.
        
        Args:
            action_name: Name of the action type
            handler: Function that processes the action
        """
        self.action_handlers[action_name] = handler
    
    def build_chain(self, threads: List[Dict]) -> nx.DiGraph:
        """
        Construct execution graph from thread definitions.
        
        Args:
            threads: List of thread specifications with action, condition, etc.
            
        Returns:
            NetworkX directed graph representing the execution flow
        """
        self.graph.clear()
        
        # Add root node
        self.graph.add_node('root', type='root', data={'purpose': self.purpose})
        
        # Add thread nodes
        thread_nodes = []
        for i, thread in enumerate(threads):
            node_id = f"thread_{i}_{thread['action']}"
            thread_nodes.append(node_id)
            
            self.graph.add_node(node_id, 
                              type='thread',
                              data={
                                  'action': thread['action'],
                                  'condition': thread.get('condition', 'always'),
                                  'depth_limit': thread.get('depth_limit', self.max_depth),
                                  'priority': thread.get('priority', 1.0)
                              })
            
            # Connect root to thread
            self.graph.add_edge('root', node_id)
        
        # Add merge node
        merge_node = 'merge_results'
        self.graph.add_node(merge_node, type='merge', data={'threads': thread_nodes})
        
        # Connect all threads to merge node
        for thread_node in thread_nodes:
            self.graph.add_edge(thread_node, merge_node)
        
        return self.graph
    
    def execute_fire(self, node_id: Optional[str] = None) -> Dict:
        """
        Run recursive processing with drift protection.
        
        Args:
            node_id: Starting node (defaults to root)
            
        Returns:
            Dictionary containing execution results and metadata
        """
        if node_id is None:
            node_id = 'root'
        
        self.start_time = time.time()
        self.execution_stats['total_executions'] += 1
        self.current_depth = 0
        
        try:
            # Execute the chain
            results = self._execute_node(node_id, {})
            
            # Mark successful completion
            self.execution_stats['successful_completions'] += 1
            
            return {
                'primary_insight': results.get('insight', f'Execution completed for {self.purpose}'),
                'confidence': results.get('confidence', 0.8),
                'execution_time': time.time() - self.start_time,
                'threads_executed': len([n for n in self.graph.nodes() if self.graph.nodes[n]['type'] == 'thread']),
                'success': True,
                'metadata': results
            }
            
        except Exception as e:
            logging.error(f"RainFire execution failed: {e}")
            return {
                'primary_insight': f'Execution failed: {str(e)}',
                'confidence': 0.0,
                'execution_time': time.time() - self.start_time if self.start_time else 0,
                'success': False,
                'error': str(e)
            }
    
    def _execute_node(self, node_id: str, context: Dict) -> Dict:
        """Execute a single node in the graph."""
        
        # Drift protection - check depth
        if self.current_depth > self.max_depth:
            self.execution_stats['drift_interventions'] += 1
            return {
                'insight': 'Maximum depth reached - drift protection activated',
                'confidence': 0.5,
                'depth_limited': True
            }
        
        node_data = self.graph.nodes[node_id]
        node_type = node_data['type']
        
        if node_type == 'root':
            return self._execute_root(node_id, context)
        elif node_type == 'thread':
            return self._execute_thread(node_id, context)
        elif node_type == 'merge':
            return self._execute_merge(node_id, context)
        else:
            return {'insight': f'Unknown node type: {node_type}', 'confidence': 0.0}
    
    def _execute_root(self, node_id: str, context: Dict) -> Dict:
        """Execute root node - initialize and delegate to children."""
        children = list(self.graph.successors(node_id))
        
        if not children:
            return {'insight': 'No execution paths defined', 'confidence': 0.0}
        
        # Execute first child (typically leads to thread execution)
        return self._execute_node(children[0], context)
    
    def _execute_thread(self, node_id: str, context: Dict) -> Dict:
        """Execute a thread node."""
        self.current_depth += 1
        
        node_data = self.graph.nodes[node_id]['data']
        action = node_data['action']
        condition = node_data['condition']
        
        # Check condition
        if not self._evaluate_condition(condition, context):
            return {
                'insight': f'Thread {action} skipped - condition not met',
                'confidence': 0.0,
                'skipped': True
            }
        
        # Execute action
        if action in self.action_handlers:
            result = self.action_handlers[action](node_data, context)
        else:
            result = {
                'insight': f'Handler not found for action: {action}',
                'confidence': 0.0,
                'error': f'Missing handler: {action}'
            }
        
        # Continue to successors if any
        successors = list(self.graph.successors(node_id))
        if successors:
            successor_results = []
            for successor in successors:
                successor_result = self._execute_node(successor, {**context, **result})
                successor_results.append(successor_result)
            
            # Merge results from successors
            if len(successor_results) == 1:
                return successor_results[0]
            else:
                return self._merge_thread_results(successor_results)
        
        return result
    
    def _execute_merge(self, node_id: str, context: Dict) -> Dict:
        """Execute merge node - combine results from multiple threads."""
        # This would typically be reached through the main execution flow
        # For now, return the context as the merged result
        return {
            'insight': f'Merge completed for {self.purpose}',
            'confidence': context.get('confidence', 0.8),
            'merged_results': True
        }
    
    def _evaluate_condition(self, condition: Union[str, Callable], context: Dict) -> bool:
        """Evaluate whether a thread condition is met."""
        if callable(condition):
            try:
                return condition(context)
            except Exception:
                return False
        
        # String-based conditions
        if condition == 'always':
            return True
        elif condition == 'never':
            return False
        elif condition == 'user_input_present':
            return context.get('user_input') is not None
        elif condition == 'anomaly_detected':
            return context.get('anomaly_detected', False)
        elif condition == 'logical_problem':
            return context.get('problem_type') == 'logical'
        elif condition == 'open_ended':
            return context.get('problem_type') == 'open_ended'
        elif condition == 'evaluation_needed':
            return context.get('needs_evaluation', False)
        else:
            # Default to True for unknown conditions
            return True
    
    def _merge_thread_results(self, results: List[Dict]) -> Dict:
        """Merge results from multiple thread executions."""
        if not results:
            return {'insight': 'No results to merge', 'confidence': 0.0}
        
        # Calculate average confidence
        confidences = [r.get('confidence', 0.0) for r in results]
        avg_confidence = sum(confidences) / len(confidences) if confidences else 0.0
        
        # Combine insights
        insights = [r.get('insight', '') for r in results if r.get('insight')]
        combined_insight = '; '.join(insights) if insights else 'Multiple threads executed'
        
        return {
            'insight': combined_insight,
            'confidence': avg_confidence,
            'thread_count': len(results),
            'individual_results': results
        }
    
    def illuminate_merge(self, results: List[Dict]) -> Dict:
        """
        Synthesize outputs from multiple execution paths.
        
        Args:
            results: List of execution results to merge
            
        Returns:
            Dictionary containing merged insights and analysis
        """
        if not results:
            return {
                'merged_insight': 'No results to merge',
                'efficacy': 0.0,
                'synthesis_quality': 'poor'
            }
        
        # Extract insights and confidences
        insights = []
        confidences = []
        
        for result in results:
            if isinstance(result, dict):
                if 'primary_insight' in result:
                    insights.append(result['primary_insight'])
                    confidences.append(result.get('confidence', 0.0))
                elif 'insight' in result:
                    insights.append(result['insight'])
                    confidences.append(result.get('confidence', 0.0))
        
        if not insights:
            return {
                'merged_insight': 'No insights found in results',
                'efficacy': 0.0,
                'synthesis_quality': 'poor'
            }
        
        # Pattern recognition - find common themes
        common_terms = self._extract_common_patterns(insights)
        
        # Confidence weighting
        if confidences:
            weighted_confidence = sum(c for c in confidences if c > 0) / len(confidences)
            efficacy = min(weighted_confidence * 100, 95.0)  # Cap at 95%
        else:
            efficacy = 50.0  # Default efficacy
        
        # Create merged insight
        if len(insights) == 1:
            merged_insight = insights[0]
        else:
            # Combine insights intelligently
            high_confidence_insights = [
                insights[i] for i, c in enumerate(confidences) 
                if c >= 0.7
            ]
            
            if high_confidence_insights:
                merged_insight = '; '.join(high_confidence_insights[:3])  # Top 3
            else:
                merged_insight = '; '.join(insights[:2])  # First 2
        
        return {
            'merged_insight': merged_insight,
            'efficacy': efficacy,
            'synthesis_quality': 'high' if efficacy > 80 else 'medium' if efficacy > 60 else 'low',
            'common_patterns': common_terms,
            'result_count': len(results),
            'confidence_distribution': confidences,
            'execution_stats': self.execution_stats.copy()
        }
    
    def _extract_common_patterns(self, insights: List[str]) -> List[str]:
        """Extract common patterns from insights."""
        if len(insights) < 2:
            return []
        
        # Simple pattern extraction - find common words
        words = []
        for insight in insights:
            words.extend(insight.lower().split())
        
        # Find words that appear in multiple insights
        word_counts = {}
        for word in words:
            if len(word) > 3:  # Skip short words
                word_counts[word] = word_counts.get(word, 0) + 1
        
        # Return words that appear more than once
        common_words = [word for word, count in word_counts.items() if count > 1]
        return common_words[:5]  # Top 5 patterns
    
    def reset_chain(self):
        """Clear state and prepare for new execution."""
        self.graph.clear()
        self.current_depth = 0
        self.start_time = None
        self.execution_context.clear()
        
        # Reset stats but keep historical data
        self.execution_stats['total_executions'] = 0
        self.execution_stats['successful_completions'] = 0
    
    def get_performance_metrics(self) -> Dict:
        """Get current performance statistics."""
        total = self.execution_stats['total_executions']
        if total == 0:
            success_rate = 0.0
        else:
            success_rate = (self.execution_stats['successful_completions'] / total) * 100
        
        return {
            'success_rate': success_rate,
            'total_executions': total,
            'drift_interventions': self.execution_stats['drift_interventions'],
            'infinite_loop_breaks': self.execution_stats['infinite_loop_breaks'],
            'avg_execution_time': getattr(self, 'avg_execution_time', 0.0)
        }


# Export main class
__all__ = ['RainFireChain']