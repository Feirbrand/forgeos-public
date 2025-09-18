# harmonic_memory.py
# Conceptual simulation of OBMI Harmonic Memory Theory
# Demonstrates bio-inspired theta-gamma coupling for memory threading
# and fractal patterns for self-similar recall.
# Theoretical only - for educational/research purposes.
# License: MIT

import numpy as np
from scipy.signal import hilbert
from typing import Union, Tuple, List

class OBMIMemorySimulator:
    """
    Theoretical OBMI (Observer-Bridge-Mind) Harmonic Memory Simulator.
    
    This class implements a conceptual model inspired by neuroscience research
    on theta-gamma phase coupling and biological memory consolidation patterns.
    
    Layers:
    - Observer: Reads input data (e.g., symbolic context)
    - Bridge: Packages data into harmonic format using theta-gamma coupling
    - Mind: Consolidates and recalls using fractal self-similarity
    
    Args:
        theta_freq (float): Low-frequency rhythm for context (4-8 Hz typical)
        gamma_freq (float): High-frequency for detail encoding (30-100 Hz typical) 
        coupling_strength (float): Modulation intensity (0-1)
        fractal_depth (int): Levels of self-similar recall processing
    """
    
    def __init__(self, theta_freq: float = 7, gamma_freq: float = 40, 
                 coupling_strength: float = 0.5, fractal_depth: int = 3):
        self.theta_freq = theta_freq
        self.gamma_freq = gamma_freq  
        self.coupling_strength = coupling_strength
        self.fractal_depth = fractal_depth
        
        # Validate parameters
        self._validate_parameters()
    
    def _validate_parameters(self) -> None:
        """Validate initialization parameters are within reasonable ranges."""
        if not (4 <= self.theta_freq <= 8):
            raise ValueError("Theta frequency should be between 4-8 Hz for biological realism")
        if not (30 <= self.gamma_freq <= 100):
            raise ValueError("Gamma frequency should be between 30-100 Hz for biological realism")
        if not (0 <= self.coupling_strength <= 1):
            raise ValueError("Coupling strength should be between 0-1")
        if not (1 <= self.fractal_depth <= 10):
            raise ValueError("Fractal depth should be between 1-10 levels")
    
    def observe(self, input_data: Union[List, np.ndarray]) -> np.ndarray:
        """
        Observer Layer: Read and normalize input data.
        
        Simulates the Observer component reading symbolic context and
        preparing it for harmonic processing.
        
        Args:
            input_data: Input symbolic context as array-like data
            
        Returns:
            Normalized input ready for Bridge processing
        """
        if not isinstance(input_data, np.ndarray):
            input_data = np.array(input_data, dtype=float)
        
        if len(input_data) == 0:
            raise ValueError("Input data cannot be empty")
            
        # Normalize for processing (prevent overflow in harmonic generation)
        max_val = np.max(np.abs(input_data))
        if max_val == 0:
            return input_data
        return input_data / max_val
    
    def bridge(self, observed_data: np.ndarray, duration: float = 10, 
               sampling_rate: int = 1000) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Bridge Layer: Package into harmonic format using theta-gamma coupling.
        
        Implements theoretical theta-gamma phase coupling mechanism inspired
        by biological memory consolidation research.
        
        Args:
            observed_data: Normalized input from Observer layer
            duration: Signal duration in seconds
            sampling_rate: Samples per second
            
        Returns:
            Tuple of (coupled_signal, phase, amplitude)
        """
        t = np.linspace(0, duration, int(duration * sampling_rate))
        
        # Generate biological-inspired oscillations
        theta = np.sin(2 * np.pi * self.theta_freq * t)
        gamma = np.sin(2 * np.pi * self.gamma_freq * t)
        
        # Implement theta-gamma phase coupling with observed data integration
        # Gamma amplitude modulated by theta phase, incorporating input context
        phase_modulation = np.cos(2 * np.pi * self.theta_freq * t)
        coupled_signal = (theta + 
                         self.coupling_strength * gamma * phase_modulation + 
                         observed_data.mean())
        
        # Extract harmonic characteristics using Hilbert transform
        analytic_signal = hilbert(coupled_signal)
        phase = np.angle(analytic_signal)
        amplitude = np.abs(analytic_signal)
        
        return coupled_signal, phase, amplitude
    
    def mind_recall(self, bridged_signal: np.ndarray) -> np.ndarray:
        """
        Mind Layer: Consolidate and recall using fractal self-similarity.
        
        Implements theoretical fractal recall mechanism where memory patterns
        are processed through self-similar iterations at multiple scales.
        
        Args:
            bridged_signal: Harmonic signal from Bridge layer
            
        Returns:
            Processed signal with fractal recall characteristics
        """
        recalled = bridged_signal.copy()
        
        # Apply fractal self-similar processing
        for depth in range(self.fractal_depth):
            # Scale factor decreases with depth (self-similar scaling)
            scale_factor = 1.0 / (2 ** depth)
            
            # Generate scaled version and integrate
            scaled_version = recalled * scale_factor
            
            # Maintain original signal length while incorporating self-similarity
            if len(scaled_version) >= len(recalled):
                recalled = recalled + scaled_version[:len(recalled)]
            else:
                # Tile the scaled version to match length
                tiles_needed = len(recalled) // len(scaled_version) + 1
                tiled_scaled = np.tile(scaled_version, tiles_needed)[:len(recalled)]
                recalled = recalled + tiled_scaled
                
        # Normalize to prevent unbounded growth
        max_val = np.max(np.abs(recalled))
        if max_val > 0:
            recalled = recalled / max_val
            
        return recalled
    
    def process_complete(self, input_data: Union[List, np.ndarray],
                        duration: float = 10, sampling_rate: int = 1000) -> dict:
        """
        Complete OBMI processing pipeline.
        
        Runs input through all three layers: Observer -> Bridge -> Mind
        
        Args:
            input_data: Raw input for processing
            duration: Signal duration for Bridge processing
            sampling_rate: Sampling rate for harmonic generation
            
        Returns:
            Dictionary containing results from all processing stages
        """
        # Observer stage
        observed = self.observe(input_data)
        
        # Bridge stage  
        coupled_signal, phase, amplitude = self.bridge(observed, duration, sampling_rate)
        
        # Mind stage
        recalled = self.mind_recall(coupled_signal)
        
        return {
            'observed': observed,
            'coupled_signal': coupled_signal,
            'phase': phase,
            'amplitude': amplitude, 
            'recalled': recalled,
            'parameters': {
                'theta_freq': self.theta_freq,
                'gamma_freq': self.gamma_freq,
                'coupling_strength': self.coupling_strength,
                'fractal_depth': self.fractal_depth
            }
        }

# Example theoretical usage and validation
if __name__ == "__main__":
    # Demonstrate basic functionality
    simulator = OBMIMemorySimulator()
    
    # Test with synthetic symbolic input
    input_context = np.sin(np.linspace(0, 4*np.pi, 1000))  # Simulated memory trace
    
    # Process through complete pipeline
    results = simulator.process_complete(input_context, duration=5)
    
    print("OBMI Harmonic Memory Simulation Results:")
    print(f"Input shape: {results['observed'].shape}")
    print(f"Coupled signal shape: {results['coupled_signal'].shape}")
    print(f"Recalled memory shape: {results['recalled'].shape}")
    print(f"Processing parameters: {results['parameters']}")
    
    # Verify signal characteristics
    print(f"Signal energy preservation: {np.mean(results['amplitude']**2):.4f}")
    print(f"Phase coherence measure: {np.std(np.diff(results['phase'])):.4f}")
    print("Theoretical harmonic memory threading completed successfully.")