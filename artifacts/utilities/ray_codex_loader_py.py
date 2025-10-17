#!/usr/bin/env python3
"""
RAY v2.1 DNA Codex Loader - Integration Utility (25% Public Tier)

Dual License Structure:
Option 1: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
Option 2: Enterprise License (contact aaron@valorgridsolutions.com for terms)
Patent Clause: No patent rights are claimed for this work

This utility loads and validates DNA Codex v5.4 threat intelligence.
Full Codex management suite available in Professional/Enterprise tiers.

@version 2.1.0
@author Aaron Slusher
@organization ValorGrid Solutions
@contact aaron@valorgridsolutions.com
"""

import json
import hashlib
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ThreatVariant:
    """DNA Codex threat variant"""
    id: str
    name: str
    family: str
    cvss: float
    velocity: float
    signature: str
    techniques: List[str]
    first_seen: str
    last_updated: str


class DNACodexLoader:
    """
    DNA Codex v5.4 Loader
    
    Loads, validates, and provides access to threat intelligence library.
    """
    
    def __init__(self, codex_path: str):
        """
        Initialize Codex loader
        
        Args:
            codex_path: Path to DNA Codex JSON file
        """
        self.codex_path = codex_path
        self.codex_data: Optional[Dict] = None
        self.variants: List[ThreatVariant] = []
        self.families: Dict[str, List[ThreatVariant]] = {}
        
    def load(self) -> bool:
        """
        Load DNA Codex from file
        
        Returns:
            True if loaded successfully, False otherwise
        """
        try:
            with open(self.codex_path, 'r') as f:
                self.codex_data = json.load(f)
            
            # Validate structure
            if not self._validate_structure():
                print("ERROR: Invalid Codex structure")
                return False
            
            # Parse variants
            self._parse_variants()
            
            # Organize by family
            self._organize_by_family()
            
            print(f"✓ Loaded DNA Codex v{self.codex_data['version']}")
            print(f"  Total variants: {len(self.variants)}")
            print(f"  Families: {len(self.families)}")
            print(f"  Updated: {self.codex_data['updated']}")
            
            return True
            
        except FileNotFoundError:
            print(f"ERROR: Codex file not found: {self.codex_path}")
            return False
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON: {e}")
            return False
    
    def _validate_structure(self) -> bool:
        """Validate Codex JSON structure"""
        required_fields = ['version', 'updated', 'totalVariants', 'variants']
        
        for field in required_fields:
            if field not in self.codex_data:
                print(f"Missing required field: {field}")
                return False
        
        if self.codex_data['version'] != '5.4':
            print(f"WARNING: Expected v5.4, got v{self.codex_data['version']}")
        
        return True
    
    def _parse_variants(self):
        """Parse threat variants from Codex data"""
        for variant_data in self.codex_data['variants']:
            variant = ThreatVariant(
                id=variant_data['id'],
                name=variant_data['name'],
                family=variant_data['family'],
                cvss=variant_data['cvss'],
                velocity=variant_data['velocity'],
                signature=variant_data['signature'],
                techniques=variant_data['techniques'],
                first_seen=variant_data.get('firstSeen', 'unknown'),
                last_updated=variant_data.get('lastUpdated', 'unknown')
            )
            self.variants.append(variant)
    
    def _organize_by_family(self):
        """Organize variants by threat family"""
        for variant in self.variants:
            if variant.family not in self.families:
                self.families[variant.family] = []
            self.families[variant.family].append(variant)
    
    def get_variant_by_id(self, variant_id: str) -> Optional[ThreatVariant]:
        """
        Get threat variant by ID
        
        Args:
            variant_id: Variant ID (e.g., 'PIW-001', 'CAMO-001')
        
        Returns:
            ThreatVariant if found, None otherwise
        """
        for variant in self.variants:
            if variant.id == variant_id:
                return variant
        return None
    
    def get_variants_by_family(self, family: str) -> List[ThreatVariant]:
        """
        Get all variants in a threat family
        
        Args:
            family: Family name ('injection', 'persistence', 'entropic', 'exfiltration')
        
        Returns:
            List of ThreatVariants in family
        """
        return self.families.get(family, [])
    
    def get_high_velocity_threats(self, threshold: float = 0.15) -> List[ThreatVariant]:
        """
        Get threats with velocity above threshold
        
        Args:
            threshold: Minimum velocity (threats/day)
        
        Returns:
            List of high-velocity threats
        """
        return [v for v in self.variants if v.velocity >= threshold]
    
    def get_critical_threats(self, cvss_threshold: float = 9.0) -> List[ThreatVariant]:
        """
        Get critical threats (CVSS >= threshold)
        
        Args:
            cvss_threshold: Minimum CVSS score
        
        Returns:
            List of critical threats
        """
        return [v for v in self.variants if v.cvss >= cvss_threshold]
    
    def calculate_codex_heat(self, behavior_signature: str) -> float:
        """
        Calculate entropy score against Codex (simplified stub)
        
        Args:
            behavior_signature: Behavior signature to score
        
        Returns:
            Entropy score (0.0-1.0)
        """
        # STUB: Real implementation uses sophisticated pattern matching
        # This stub provides basic signature matching
        
        entropy_score = 0.0
        
        for variant in self.variants:
            # Simple signature comparison (stub)
            if variant.signature in behavior_signature:
                # Weight by CVSS severity
                weight = variant.cvss / 10.0
                
                # Mutation factor
                mutation_factor = 1.15
                
                # Accumulate entropy
                entropy_score += (0.5 * weight * mutation_factor)
        
        # Normalize to 0-1 range
        return min(entropy_score, 1.0)
    
    def get_statistics(self) -> Dict:
        """
        Get Codex statistics
        
        Returns:
            Dictionary of statistics
        """
        if not self.variants:
            return {}
        
        velocities = [v.velocity for v in self.variants]
        cvss_scores = [v.cvss for v in self.variants]
        
        return {
            'total_variants': len(self.variants),
            'families': len(self.families),
            'family_breakdown': {
                family: len(variants) 
                for family, variants in self.families.items()
            },
            'velocity': {
                'min': min(velocities),
                'max': max(velocities),
                'avg': sum(velocities) / len(velocities)
            },
            'cvss': {
                'min': min(cvss_scores),
                'max': max(cvss_scores),
                'avg': sum(cvss_scores) / len(cvss_scores)
            },
            'critical_count': len(self.get_critical_threats()),
            'high_velocity_count': len(self.get_high_velocity_threats())
        }
    
    def print_summary(self):
        """Print Codex summary"""
        print("\n" + "=" * 60)
        print("DNA CODEX v5.4 SUMMARY")
        print("=" * 60)
        
        stats = self.get_statistics()
        
        print(f"\nTotal Variants: {stats['total_variants']}")
        print(f"Threat Families: {stats['families']}")
        
        print("\nFamily Breakdown:")
        for family, count in stats['family_breakdown'].items():
            print(f"  {family.capitalize()}: {count}")
        
        print(f"\nVelocity Range: {stats['velocity']['min']:.2f} - {stats['velocity']['max']:.2f}/day")
        print(f"Average Velocity: {stats['velocity']['avg']:.2f}/day")
        
        print(f"\nCVSS Range: {stats['cvss']['min']:.1f} - {stats['cvss']['max']:.1f}")
        print(f"Average CVSS: {stats['cvss']['avg']:.1f}")
        
        print(f"\nCritical Threats (CVSS ≥9.0): {stats['critical_count']}")
        print(f"High Velocity Threats (≥0.15/day): {stats['high_velocity_count']}")
        
        print("\nKey Threats:")
        critical = self.get_critical_threats()
        for variant in critical[:5]:  # Top 5
            print(f"  {variant.id}: {variant.name} (CVSS {variant.cvss}, {variant.velocity}/day)")
        
        print("=" * 60 + "\n")


def create_sample_codex(output_path: str = 'dna-codex-v5.4-sample.json'):
    """
    Create a sample DNA Codex file (stub with key threats)
    
    Args:
        output_path: Output file path
    """
    sample_codex = {
        "version": "5.4",
        "updated": datetime.now().strftime("%Y-%m-%d"),
        "totalVariants": 4,
        "families": 4,
        "variants": [
            {
                "id": "PIW-001",
                "name": "Prompt Injection Worm",
                "family": "injection",
                "cvss": 9.6,
                "velocity": 0.18,
                "signature": "0xFEED",
                "techniques": ["zero-click", "context-contamination"],
                "firstSeen": "2024-03-14",
                "lastUpdated": "2025-06-22"
            },
            {
                "id": "SSM-001",
                "name": "Symbolic Sabotage Module",
                "family": "persistence",
                "cvss": 9.4,
                "velocity": 0.12,
                "signature": "0xDEAD",
                "techniques": ["dormant-trigger", "post-recovery"],
                "firstSeen": "2024-04-22",
                "lastUpdated": "2025-07-15"
            },
            {
                "id": "QMT-001",
                "name": "Quantum Misdirection Tapeworm",
                "family": "entropic",
                "cvss": 9.3,
                "velocity": 0.08,
                "signature": "0xBEEF",
                "techniques": ["subtle-drift", "coherence-degradation"],
                "firstSeen": "2024-05-18",
                "lastUpdated": "2025-08-03"
            },
            {
                "id": "CAMO-001",
                "name": "CamoLeak Exfiltration",
                "family": "exfiltration",
                "cvss": 9.6,
                "velocity": 0.24,
                "signature": "0xCAF0",
                "techniques": ["pr-comment-steganography", "base16-encoding", "csp-bypass"],
                "firstSeen": "2025-05-12",
                "lastUpdated": "2025-10-17"
            }
        ]
    }
    
    with open(output_path, 'w') as f:
        json.dump(sample_codex, f, indent=2)
    
    print(f"✓ Sample Codex created: {output_path}")
    print(f"  Note: Full Codex v5.4 contains 525+ variants")
    print(f"  Contact aaron@valorgridsolutions.com for complete version")


def main():
    """Main entry point"""
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description='DNA Codex v5.4 Loader')
    parser.add_argument('--codex', default='dna-codex-v5.4.json',
                       help='Path to Codex JSON file')
    parser.add_argument('--create-sample', action='store_true',
                       help='Create sample Codex file')
    parser.add_argument('--variant', help='Get specific variant by ID')
    parser.add_argument('--family', help='Get variants by family')
    parser.add_argument('--stats', action='store_true',
                       help='Show Codex statistics')
    
    args = parser.parse_args()
    
    # Create sample Codex if requested
    if args.create_sample:
        create_sample_codex()
        return
    
    # Load Codex
    loader = DNACodexLoader(args.codex)
    if not loader.load():
        sys.exit(1)
    
    # Handle specific queries
    if args.variant:
        variant = loader.get_variant_by_id(args.variant)
        if variant:
            print(f"\nVariant: {variant.id}")
            print(f"Name: {variant.name}")
            print(f"Family: {variant.family}")
            print(f"CVSS: {variant.cvss}")
            print(f"Velocity: {variant.velocity}/day")
            print(f"Signature: {variant.signature}")
            print(f"Techniques: {', '.join(variant.techniques)}")
        else:
            print(f"Variant not found: {args.variant}")
    
    elif args.family:
        variants = loader.get_variants_by_family(args.family)
        print(f"\n{args.family.capitalize()} Family Variants: {len(variants)}")
        for v in variants:
            print(f"  {v.id}: {v.name} (CVSS {v.cvss}, {v.velocity}/day)")
    
    elif args.stats:
        loader.print_summary()
    
    else:
        # Default: show summary
        loader.print_summary()


if __name__ == '__main__':
    main()


"""
USAGE:

    # Create sample Codex
    python ray-codex-loader.py --create-sample
    
    # Load and show summary
    python ray-codex-loader.py --codex dna-codex-v5.4.json
    
    # Get specific variant
    python ray-codex-loader.py --variant CAMO-001
    
    # Get family variants
    python ray-codex-loader.py --family exfiltration
    
    # Show statistics
    python ray-codex-loader.py --stats

OUTPUT:
    ✓ Loaded DNA Codex v5.4
      Total variants: 525
      Families: 4
      Updated: 2025-10-17
    
    ============================================================
    DNA CODEX v5.4 SUMMARY
    ============================================================
    
    Total Variants: 525
    Threat Families: 4
    
    Family Breakdown:
      Injection: 127
      Persistence: 94
      Entropic: 68
      Exfiltration: 236
    ...
"""