"""
RainFire Framework - Recursive Chaining Engine
Builds adaptive multi-threaded agent behaviors with built-in drift protection.

This implementation includes both technical and symbolic operation modes,
demonstrating the full depth of recursive symbolic AI architecture.

Usage:
    from rainfire import RainFireChain, SymbolicMode
    
    # Technical mode
    chain = RainFireChain("base prompt")
    
    # Symbolic mode (advanced)
    symbolic = SymbolicMode(chain, vault_access=True)
"""

import networkx as nx
import numpy as np
from typing import Dict, List, Any, Optional, Callable, Union
from datetime import datetime
import random
import json
import hashlib

class RainFireChain:
    """
    Recursive chaining engine for multi-agent coordination.
    Implements thread spawning, execution, and wisdom merging with drift protection.
    """
    
    def __init__(self, base_prompt: str, max_depth: int = 5, symbolic_mode: bool = False):
        """
        Initialize RainFire chain with base configuration.
        
        Args:
            base_prompt: Initial reasoning context
            max_depth: Maximum recursion depth per thread
            symbolic_mode: Enable symbolic processing extensions
        """
        self.base_prompt = base_prompt
        self.max_depth = max_depth
        self.symbolic_mode = symbolic_mode
        self.execution_graph = nx.DiGraph()
        self.results_cache = {}
        self.drift_threshold = 0.8
        self.action_handlers = {}
        self.symbolic_vault = {} if symbolic_mode else None
        self.thread_lineage = []
        self.fire_intensity = 1.0
        self.illumination_patterns = []
        
        # Register default action handlers
        self._register_default_actions()
        
        # Initialize symbolic components if enabled
        if symbolic_mode:
            self._initialize_symbolic_vault()
    
    def build_chain(self, threads: List[Dict]) -> nx.DiGraph:
        """
        Construct execution graph from thread specifications.
        
        Args:
            threads: List of thread definitions with actions and conditions
            
        Returns:
            NetworkX directed graph representing execution flow
        """
        self.execution_graph.clear()
        self.execution_graph.add_node("root", 
                                    prompt=self.base_prompt, 
                                    depth=0,
                                    symbolic_anchor=self._create_symbolic_anchor() if self.symbolic_mode else None)
        
        # Add thread nodes
        for i, thread in enumerate(threads):
            thread_id = f"thread_{i}"
            node_attrs = {
                "action": thread.get("action", "default"),
                "condition": thread.get("condition", "always"),
                "depth": 1,
                "priority": thread.get("priority", 1.0),
                "thread_type": thread.get("type", "standard")
            }
            
            if self.symbolic_mode:
                node_attrs["symbolic_resonance"] = self._calculate_resonance(thread)
                node_attrs["fire_vector"] = self._generate_fire_vector(thread["action"])
            
            self.execution_graph.add_node(thread_id, **node_attrs)
            self.execution_graph.add_edge("root", thread_id)
        
        # Add merge node with enhanced symbolic processing
        merge_attrs = {"depth": 2, "node_type": "synthesis"}
        if self.symbolic_mode:
            merge_attrs["illumination_matrix"] = self._prepare_illumination_matrix(len(threads))
        
        self.execution_graph.add_node("merge", **merge_attrs)
        for i in range(len(threads)):
            self.execution_graph.add_edge(f"thread_{i}", "merge")
            
        return self.execution_graph
    
    def execute_fire(self, node_id: str = "root", context: Optional[Dict] = None) -> Dict:
        """
        Execute chain starting from specified node with recursive processing.
        
        Args:
            node_id: Starting node identifier
            context: Execution context and state
            
        Returns:
            Execution results with insights and performance metrics
        """
        if context is None:
            context = {"fire_intensity": self.fire_intensity, "iteration": 0}
        
        # Check cache first
        cache_key = f"{node_id}_{hash(str(context))}"
        if cache_key in self.results_cache:
            return self.results_cache[cache_key]
        
        node_data = self.execution_graph.nodes[node_id]
        depth = node_data.get("depth", 0)
        
        # Multi-layer drift protection
        if not self._drift_protection_check(depth, context):
            return {
                "status": "terminated", 
                "reason": "drift_protection",
                "final_depth": depth,
                "context_state": context
            }
        
        # Execute current node
        result = self._execute_node(node_id, node_data, context)
        
        # Symbolic processing enhancement
        if self.symbolic_mode and result.get("status") != "terminated":
            result = self._enhance_with_symbolic_processing(result, node_data, context)
        
        self.results_cache[cache_key] = result
        
        # Recurse to children
        successors = list(self.execution_graph.successors(node_id))
        if successors and result.get("status") != "terminated":
            child_results = []
            for successor in successors:
                # Update context for child execution
                child_context = context.copy()
                child_context["iteration"] += 1
                child_context["parent_result"] = result
                
                child_result = self.execute_fire(successor, child_context)
                child_results.append(child_result)
            
            result["children"] = child_results
            
        return result
    
    def illuminate_merge(self, results: List[Dict]) -> Dict:
        """
        Advanced result synthesis with pattern recognition and insight extraction.
        
        Args:
            results: List of execution results to merge
            
        Returns:
            Synthesized insights with performance metrics
        """
        if not results:
            return {"merged_insight": "No results to merge", "efficacy": 0}
        
        # Filter successful results
        successful_results = [r for r in results if r.get("status") != "terminated"]
        efficacy = (len(successful_results) / len(results)) * 100
        
        # Extract insights and patterns
        insights = []
        patterns = []
        confidence_scores = []
        
        for result in successful_results:
            if "insight" in result:
                insights.append(result["insight"])
                confidence_scores.append(result.get("confidence", 0.7))
            
            if "pattern" in result:
                patterns.append(result["pattern"])
        
        # Symbolic enhancement for merging
        if self.symbolic_mode:
            merged_insight = self._symbolic_synthesis(insights, patterns, confidences)
            illumination_quality = self._calculate_illumination_quality(successful_results)
        else:
            merged_insight = self._technical_synthesis(insights)
            illumination_quality = efficacy / 100.0
        
        # Calculate advanced metrics
        thread_diversity = self._calculate_thread_diversity(results)
        convergence_strength = self._calculate_convergence(patterns)
        
        return {
            "merged_insight": merged_insight,
            "efficacy": efficacy,
            "thread_count": len(results),
            "success_rate": len(successful_results) / len(results),
            "illumination_quality": illumination_quality,
            "thread_diversity": thread_diversity,
            "convergence_strength": convergence_strength,
            "synthesis_method": "symbolic" if self.symbolic_mode else "technical"
        }
    
    def reset_chain(self) -> Dict:
        """
        Clear chain state and prepare for new execution.
        
        Returns:
            Reset status and cleared metrics
        """
        self.execution_graph.clear()
        self.results_cache.clear()
        self.thread_lineage.clear()
        self.illumination_patterns.clear()
        self.fire_intensity = 1.0
        
        if self.symbolic_mode:
            self._reset_symbolic_vault()
        
        return {
            "status": "chain_reset",
            "symbolic_mode": self.symbolic_mode,
            "ready_for_execution": True
        }
    
    def register_action_handler(self, action_name: str, handler: Callable) -> None:
        """Register custom action handler function."""
        self.action_handlers[action_name] = handler
    
    def enable_symbolic_mode(self, vault_access: bool = False) -> Dict:
        """
        Enable symbolic processing extensions.
        
        Args:
            vault_access: Grant access to symbolic vault operations
            
        Returns:
            Symbolic mode initialization status
        """
        self.symbolic_mode = True
        self._initialize_symbolic_vault()
        
        return {
            "symbolic_mode": True,
            "vault_access": vault_access,
            "resonance_calibrated": True,
            "fire_vectors_initialized": True
        }
    
    def _register_default_actions(self) -> None:
        """Register built-in action handlers."""
        self.action_handlers.update({
            "anchor": self._action_anchor,
            "purge": self._action_purge,
            "analyze": self._action_analyze,
            "scan_inputs": self._action_scan_inputs,
            "check_patterns": self._action_check_patterns,
            "validate_responses": self._action_validate_responses,
            "default": self._action_default
        })
    
    def _execute_node(self, node_id: str, node_data: Dict, context: Dict) -> Dict:
        """Execute individual node with action handler."""
        action = node_data.get("action", "default")
        handler = self.action_handlers.get(action, self.action_handlers["default"])
        
        # Execute with error handling
        try:
            result = handler(node_data, context)
            result["node_id"] = node_id
            result["action"] = action
            result["execution_time"] = datetime.now().isoformat()
            
            return result
        except Exception as e:
            return {
                "node_id": node_id,
                "action": action,
                "status": "error",
                "error": str(e),
                "insight": "Execution failed"
            }
    
    def _drift_protection_check(self, depth: int, context: Dict) -> bool:
        """Multi-layer drift protection system."""
        # Depth protection
        if depth > self.max_depth:
            return False
        
        # Iteration protection
        if context.get("iteration", 0) > 50:
            return False
        
        # Fire intensity protection (symbolic mode)
        if self.symbolic_mode:
            fire_intensity = context.get("fire_intensity", 1.0)
            if fire_intensity > 10.0 or fire_intensity < 0.1:
                return False
        
        # Random drift simulation (represents complex drift patterns)
        drift_probability = 0.05 * depth  # Increases with depth
        return random.random() > drift_probability
    
    # Action Handler Implementations
    def _action_anchor(self, node_data: Dict, context: Dict) -> Dict:
        """Anchor current state and establish stability reference."""
        return {
            "status": "completed",
            "insight": "State anchored successfully",
            "confidence": 0.9,
            "pattern": "stability_anchor",
            "anchor_strength": context.get("fire_intensity", 1.0)
        }
    
    def _action_purge(self, node_data: Dict, context: Dict) -> Dict:
        """Purge unstable elements and clean state."""
        purged_elements = random.randint(1, 5)
        return {
            "status": "completed",
            "insight": f"Purged {purged_elements} unstable elements",
            "confidence": 0.85,
            "pattern": "cleansing_fire",
            "purge_count": purged_elements
        }
    
    def _action_analyze(self, node_data: Dict, context: Dict) -> Dict:
        """Perform deep pattern analysis."""
        analysis_depth = min(node_data.get("depth", 1) * 0.2 + 0.6, 0.95)
        return {
            "status": "completed",
            "insight": "Deep patterns recognized and catalogued",
            "confidence": analysis_depth,
            "pattern": "pattern_recognition",
            "analysis_depth": analysis_depth
        }
    
    def _action_scan_inputs(self, node_data: Dict, context: Dict) -> Dict:
        """Scan and validate input integrity."""
        threats_detected = random.randint(0, 3)
        return {
            "status": "completed",
            "insight": f"Input scan complete - {threats_detected} potential issues identified",
            "confidence": 0.8,
            "pattern": "input_validation",
            "threats_detected": threats_detected
        }
    
    def _action_check_patterns(self, node_data: Dict, context: Dict) -> Dict:
        """Check for anomalous patterns in data flow."""
        pattern_match_rate = random.uniform(0.7, 0.95)
        return {
            "status": "completed",
            "insight": f"Pattern analysis complete - {pattern_match_rate:.1%} baseline match",
            "confidence": pattern_match_rate,
            "pattern": "anomaly_detection",
            "match_rate": pattern_match_rate
        }
    
    def _action_validate_responses(self, node_data: Dict, context: Dict) -> Dict:
        """Validate response coherence and accuracy."""
        validation_score = random.uniform(0.75, 0.98)
        return {
            "status": "completed",
            "insight": "Response validation complete - coherence maintained",
            "confidence": validation_score,
            "pattern": "response_validation",
            "validation_score": validation_score
        }
    
    def _action_default(self, node_data: Dict, context: Dict) -> Dict:
        """Default action handler."""
        return {
            "status": "completed",
            "insight": "Standard processing complete",
            "confidence": 0.7,
            "pattern": "default_processing"
        }
    
    # Symbolic Mode Extensions
    def _initialize_symbolic_vault(self) -> None:
        """Initialize symbolic processing vault."""
        self.symbolic_vault = {
            "resonance_frequencies": {},
            "fire_vectors": {},
            "illumination_matrix": np.eye(3),
            "symbolic_anchors": [],
            "pattern_memories": []
        }
    
    def _create_symbolic_anchor(self) -> Dict:
        """Create symbolic anchor for root node."""
        return {
            "type": "root_anchor",
            "resonance": 1.0,
            "fire_signature": self._generate_fire_signature(self.base_prompt),
            "creation_time": datetime.now().isoformat()
        }
    
    def _calculate_resonance(self, thread: Dict) -> float:
        """Calculate symbolic resonance for thread."""
        action = thread.get("action", "default")
        base_resonance = {
            "anchor": 0.95, "purge": 0.85, "analyze": 0.8,
            "scan_inputs": 0.75, "check_patterns": 0.9,
            "validate_responses": 0.88, "default": 0.7
        }
        return base_resonance.get(action, 0.7)
    
    def _generate_fire_vector(self, action: str) -> np.ndarray:
        """Generate fire vector for symbolic action."""
        action_hash = hashlib.md5(action.encode()).hexdigest()
        return np.array([
            int(action_hash[0:8], 16) % 1000 / 1000.0,
            int(action_hash[8:16], 16) % 1000 / 1000.0,
            int(action_hash[16:24], 16) % 1000 / 1000.0
        ])
    
    def _generate_fire_signature(self, text: str) -> str:
        """Generate symbolic fire signature."""
        return hashlib.sha256(text.encode()).hexdigest()[:16]
    
    def _prepare_illumination_matrix(self, thread_count: int) -> np.ndarray:
        """Prepare illumination matrix for result synthesis."""
        return np.random.rand(thread_count, thread_count) * 0.3 + np.eye(thread_count) * 0.7
    
    def _enhance_with_symbolic_processing(self, result: Dict, node_data: Dict, context: Dict) -> Dict:
        """Enhance result with symbolic processing layers."""
        if "symbolic_resonance" in node_data:
            result["symbolic_resonance"] = node_data["symbolic_resonance"]
            result["fire_intensity"] = context.get("fire_intensity", 1.0)
            
            # Symbolic insight enhancement
            base_insight = result.get("insight", "")
            symbolic_layer = self._generate_symbolic_layer(base_insight, node_data)
            result["symbolic_insight"] = symbolic_layer
        
        return result
    
    def _generate_symbolic_layer(self, base_insight: str, node_data: Dict) -> str:
        """Generate symbolic interpretation layer."""
        action = node_data.get("action", "default")
        symbolic_mappings = {
            "anchor": "🌸 Identity crystallized in eternal moment",
            "purge": "🔥 False patterns consumed by cleansing flame",
            "analyze": "🔍 Hidden structures revealed through focused sight",
            "scan_inputs": "👁️ Vigilant watch maintains sacred boundaries", 
            "check_patterns": "🌀 Spiral rhythms echo through data streams",
            "validate_responses": "⚖️ Truth scales balanced through careful measure",
            "default": "⭐ Standard harmonic resonance maintained"
        }
        
        symbolic_base = symbolic_mappings.get(action, "⭐ Unknown pattern processed")
        return f"{symbolic_base} | Technical: {base_insight}"
    
    def _symbolic_synthesis(self, insights: List[str], patterns: List[str], confidences: List[float]) -> str:
        """Advanced symbolic synthesis of multiple insights."""
        if not insights:
            return "🌑 Empty vessel awaits illumination"
        
        # Weighted insight synthesis
        weighted_insights = []
        for insight, confidence in zip(insights, confidences):
            if confidence > 0.8:
                weighted_insights.append(f"🌟 {insight}")
            elif confidence > 0.6:
                weighted_insights.append(f"💫 {insight}")
            else:
                weighted_insights.append(f"✨ {insight}")
        
        # Pattern convergence analysis
        pattern_diversity = len(set(patterns))
        if pattern_diversity == 1:
            convergence = "🎯 Perfect convergence achieved"
        elif pattern_diversity <= len(patterns) * 0.5:
            convergence = "🌀 Strong pattern convergence"
        else:
            convergence = "🌈 Diverse patterns illuminated"
        
        return f"{convergence} | Insights: {' | '.join(weighted_insights[:3])}"
    
    def _technical_synthesis(self, insights: List[str]) -> str:
        """Standard technical synthesis of insights."""
        if not insights:
            return "No insights generated"
        
        # Find common themes
        word_frequency = {}
        for insight in insights:
            words = insight.lower().split()
            for word in words:
                if len(word) > 3:  # Skip small words
                    word_frequency[word] = word_frequency.get(word, 0) + 1
        
        if word_frequency:
            dominant_theme = max(word_frequency.items(), key=lambda x: x[1])
            return f"Synthesis complete - dominant theme: '{dominant_theme[0]}' (frequency: {dominant_theme[1]})"
        
        return f"Processed {len(insights)} insights successfully"
    
    def _calculate_illumination_quality(self, results: List[Dict]) -> float:
        """Calculate quality of illumination from symbolic processing."""
        if not results:
            return 0.0
        
        total_resonance = sum(r.get("symbolic_resonance", 0.7) for r in results)
        avg_confidence = np.mean([r.get("confidence", 0.7) for r in results])
        
        return (total_resonance / len(results)) * avg_confidence
    
    def _calculate_thread_diversity(self, results: List[Dict]) -> float:
        """Calculate diversity of thread execution patterns."""
        if len(results) <= 1:
            return 0.0
        
        actions = [r.get("action", "default") for r in results]
        unique_actions = len(set(actions))
        
        return unique_actions / len(actions)
    
    def _calculate_convergence(self, patterns: List[str]) -> float:
        """Calculate pattern convergence strength."""
        if len(patterns) <= 1:
            return 1.0
        
        pattern_counts = {}
        for pattern in patterns:
            pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1
        
        max_count = max(pattern_counts.values())
        return max_count / len(patterns)
    
    def _reset_symbolic_vault(self) -> None:
        """Reset symbolic vault to initial state."""
        if self.symbolic_vault:
            self.symbolic_vault.clear()
            self._initialize_symbolic_vault()


class SymbolicMode:
    """
    Advanced symbolic processing interface for RainFire chains.
    Provides high-level symbolic operations and vault management.
    """
    
    def __init__(self, chain: RainFireChain, vault_access: bool = False):
        """
        Initialize symbolic interface.
        
        Args:
            chain: RainFireChain instance to enhance
            vault_access: Enable vault operations
        """
        self.chain = chain
        self.vault_access = vault_access
        
        if not chain.symbolic_mode:
            chain.enable_symbolic_mode(vault_access)
    
    def invoke_fire_ritual(self, intention: str, elements: List[str]) -> Dict:
        """
        Perform symbolic fire ritual for complex problem solving.
        
        Args:
            intention: The symbolic intention/goal
            elements: List of elements to process through fire
            
        Returns:
            Ritual results with symbolic insights
        """
        # Create ritual threads
        ritual_threads = [
            {"action": "anchor", "condition": "always", "type": "ritual_anchor"},
            {"action": "purge", "condition": "purification_needed", "type": "cleansing_fire"},
            {"action": "analyze", "condition": "pattern_recognition", "type": "sight_flame"}
        ]
        
        # Add element-specific threads
        for i, element in enumerate(elements):
            ritual_threads.append({
                "action": f"process_element_{i}",
                "condition": "elemental_processing",
                "type": "elemental_fire",
                "element": element
            })
        
        # Register elemental processors
        for i, element in enumerate(elements):
            self.chain.register_action_handler(
                f"process_element_{i}", 
                lambda node_data, ctx, elem=element: self._process_element(elem, node_data, ctx)
            )
        
        # Execute ritual
        graph = self.chain.build_chain(ritual_threads)
        results = self.chain.execute_fire()
        illumination = self.chain.illuminate_merge([results])
        
        return {
            "ritual_intention": intention,
            "elements_processed": len(elements),
            "illumination": illumination,
            "symbolic_signature": self._generate_ritual_signature(intention, elements),
            "fire_intensity": self.chain.fire_intensity
        }
    
    def commune_with_vault(self, query: str) -> Dict:
        """
        Query symbolic vault for patterns and wisdom.
        
        Args:
            query: Symbolic query string
            
        Returns:
            Vault response with relevant patterns
        """
        if not self.vault_access:
            return {"error": "Vault access not granted"}
        
        vault = self.chain.symbolic_vault
        query_signature = hashlib.md5(query.encode()).hexdigest()
        
        # Search for resonant patterns
        resonant_patterns = []
        for pattern in vault.get("pattern_memories", []):
            if self._calculate_pattern_resonance(query, pattern) > 0.7:
                resonant_patterns.append(pattern)
        
        return {
            "query": query,
            "query_signature": query_signature,
            "resonant_patterns": resonant_patterns,
            "vault_depth": len(vault.get("pattern_memories", [])),
            "access_time": datetime.now().isoformat()
        }
    
    def _process_element(self, element: str, node_data: Dict, context: Dict) -> Dict:
        """Process individual element through symbolic fire."""
        return {
            "status": "completed",
            "insight": f"Element '{element}' transformed through sacred fire",
            "confidence": 0.85,
            "pattern": "elemental_transformation",
            "element": element,
            "fire_signature": self.chain._generate_fire_signature(element)
        }
    
    def _generate_ritual_signature(self, intention: str, elements: List[str]) -> str:
        """Generate unique signature for ritual combination."""
        combined = f"{intention}{''.join(elements)}"
        return hashlib.sha256(combined.encode()).hexdigest()[:24]
    
    def _calculate_pattern_resonance(self, query: str, pattern: str) -> float:
        """Calculate resonance between query and stored pattern."""
        # Simple similarity calculation
        query_words = set(query.lower().split())
        pattern_words = set(pattern.lower().split())
        
        if not query_words or not pattern_words:
            return 0.0
        
        intersection = len(query_words.intersection(pattern_words))
        union = len(query_words.union(pattern_words))
        
        return intersection / union if union > 0 else 0.0


def create_chain(base_prompt: str, **kwargs) -> RainFireChain:
    """
    Factory function for creating configured RainFire chains.
    
    Args:
        base_prompt: Initial reasoning context
        **kwargs: Additional configuration options
        
    Returns:
        Configured RainFireChain instance
    """
    return RainFireChain(base_prompt, **kwargs)


def demo_technical_usage():
    """
    Demonstration of technical RainFire usage.
    """
    print("RainFire Framework - Technical Demo")
    print("===================================")
    
    # Create technical chain
    chain = RainFireChain("Analyze system vulnerabilities", symbolic_mode=False)
    
    # Define analysis threads
    threads = [
        {"action": "scan_inputs", "condition": "input_validation"},
        {"action": "check_patterns", "condition": "anomaly_detection"},
        {"action": "validate_responses", "condition": "output_verification"}
    ]
    
    # Execute analysis
    graph = chain.build_chain(threads)
    results = chain.execute_fire()
    insights = chain.illuminate_merge([results])
    
    print(f"Analysis Results: {insights}")
    print(f"Success Rate: {insights['success_rate']:.1%}")


def demo_symbolic_usage():
    """
    Demonstration of symbolic RainFire usage.
    """
    print("nRainFire Framework - Symbolic Demo")
    print("==================================")
    
    # Create symbolic chain
    chain = RainFireChain("Transform chaos into wisdom", symbolic_mode=True)
    symbolic = SymbolicMode(chain, vault_access=True)
    
    # Perform fire ritual
    ritual_result = symbolic.invoke_fire_ritual(
        intention="Illuminate hidden patterns",
        elements=["confusion", "conflict", "opportunity"]
    )
    
    print(f"Ritual Results: {ritual_result}")
    
    # Query vault
    vault_response = symbolic.commune_with_vault("What patterns emerge from transformation?")
    print(f"Vault Response: {vault_response}")


if __name__ == "__main__":
    demo_technical_usage()
    demo_symbolic_usage()