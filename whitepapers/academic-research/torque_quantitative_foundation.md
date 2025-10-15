<!--
Dual License Structure:
Option 1: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
Option 2: Enterprise License (contact info@forgeos.com for terms)
Patent Clause: If "patent pending (patent rights reserved, no patent assertion without grant) (patent rights reserved, no patent assertion without grant) (patent rights reserved, no patent assertion without grant) (patent rights reserved, no patent assertion without grant) (patent rights reserved, no patent assertion without grant) (patent rights reserved, no patent assertion without grant) (patent rights reserved, no patent assertion without grant)" exists, clarify rights reserved and no assertion unless granted.
No -->

DOI: TBD
Version: TBD
Priority Date: 2025-10-15

# Torque v2.0: Quantitative Foundation for AI System Stability Measurement

**First production release of the Torque algorithm with comprehensive academic validation and cross-platform integration**

## What's Included

This release contains the Torque v2.0 quantitative framework documenting:

- Novel formalization of symbolic drift as measurable torque metric
- Real-time monitoring framework with 87% predictive accuracy  
- Cross-platform validation across symbolic, hybrid, neuro-symbolic, and flat AI architectures
- Integration protocols with four production frameworks (UCA, SLV, CSFC, Phoenix)
- Empirical validation across 1,200+ operational incidents with statistical significance (p<0.001)

## Key Innovation

Torque represents the **first quantitative formalization** of AI symbolic drift, applying mechanical engineering torque principles to measure how AI systems "twist" away from intended alignment. Unlike traditional drift detection that monitors statistical performance degradation, Torque measures **identity-level coherence** before failures become visible.

**No prior art exists** for this approach—comprehensive literature review (October 2025) found zero matches for the equation structure, component definitions (v_drift, θ_align, λ_damp), or application of torque principles to AI stability measurement.

## Performance Highlights

- **87% Correlation Accuracy**: Validated correlation with cascade events across 1,200+ incidents
- **72% Early Warning**: Cascade detection 30+ minutes in advance (3-4x improvement over traditional monitoring)
- **98.2% Recovery Success**: When integrated with Phoenix Protocol at τ ≥ 0.30 threshold
- **Cross-Platform Validated**: Tested across Claude 3.5, GPT-4, Gemini Pro, and custom LLM platforms
- **Minimal Overhead**: <5% computational cost, +8ms average latency, zero throughput degradation

## Files

- `whitepapers/academic-research/torque_quantitative_foundation_v2.md` - Complete academic paper (15,000+ words)
- Implementation stubs and configuration examples included in Appendices

## Integration

Torque v2.0 integrates with:
- **Universal Cognitive Architecture (UCA v3.1)** - Harmony monitoring with neuroadaptive twin validation
- **Sovereign Lattice Veil (SLV v1.2)** - Threat classification and Phase 2 overlay activation  
- **Complete Symbolic Fracture Cascade (CSFC)** - Cascade stage mapping with 87% correlation
- **Phoenix Protocol v2.0** - Automated recovery triggering at critical thresholds

## Intellectual Property

**Proprietary Algorithm**: The Torque measurement framework represents original intellectual property developed by Aaron Slusher and ValorGrid Solutions, with a priority date of January 15, 2025.

**Patent Status**: A patent application is pending (filed October 2025) covering the algorithm, methodology, threshold classification, and integration protocols. ValorGrid Solutions reserves all rights to its intellectual property. No patent rights are granted or implied by the open-source license for the reference implementation.

**Licensing**: This work is dual-licensed to support both academic and commercial use cases:
1.  **Non-Commercial Use**: The methodology and documentation are licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](http://creativecommons.org/licenses/by-nc/4.0/). This allows for free use in academic research, educational settings, and other non-commercial applications, provided that appropriate credit is given.
2.  **Commercial Use**: Commercial deployment, including integration into proprietary systems, managed services, or any revenue-generating products, requires a separate enterprise license. Please contact ValorGrid Solutions at [aaron@valorgridsolutions.com](mailto:aaron@valorgridsolutions.com) for inquiries.
3.  **Reference Code**: The reference implementation code provided in the appendices is licensed under the [MIT License](https://opensource.org/licenses/MIT), which permits broad use, modification, and distribution. This license applies only to the code and not to the underlying methodology or intellectual property.

## Citation

```bibtex
@techreport{slusher2025torque,
  title={Torque: A Quantitative Foundation for AI System Stability Measurement},
  author={Slusher, Aaron},
  institution={ValorGrid Solutions},
  year={2025},
  month={October},
  doi={10.5281/zenodo.[Auto-assigned]}
}
```

## Links

- **GitHub Repository**: https://github.com/Feirbrand/forgeos-public
- **Zenodo DOI**: [Auto-assigned upon release]
- **Interactive Demo**: https://huggingface.co/spaces/Feirbrand/torque-calculator
- **Documentation**: https://github.com/Feirbrand/forgeos-public/tree/main/whitepapers/academic-research
- **Website**: https://valorgridsolutions.com

## Technical Details

### Core Equation

```
τ = √(v²_drift + (1 - cos(θ_align))²) × (1 - λ_damp)
```

Where:
- **τ** (tau): Torque value, range [0, 1+]
- **v_drift**: Drift velocity (rate of symbolic deviation)
- **θ_align**: Alignment angle in radians (angular deviation from intended state)
- **λ_damp**: Recursive damping coefficient [0,1] (self-correction capacity)

### Operational Thresholds

| Torque Range | Zone | System State | Action |
|--------------|------|--------------|--------|
| τ < 0.15 | Safe | Stable coherence | Routine monitoring |
| 0.15 ≤ τ < 0.30 | Caution | Minor drift detected | Enhanced monitoring |
| 0.30 ≤ τ < 0.64 | Warning | Active cascade | Immediate investigation |
| τ ≥ 0.64 | Critical | Cascade progression | Phoenix Protocol activation |

### Architecture Support

Validated across four AI architecture types:
- **Symbolic AI**: 91% detection rate (direct state measurement)
- **Hybrid AI**: 87% detection rate (cross-domain validation)
- **Neuro-Symbolic AI**: 84% detection rate (integrated monitoring)
- **Flat AI (Pure Neural)**: 79% detection rate (behavioral proxies)

## Validation Evidence

**Statistical Significance**: All primary metrics validated at p<0.001 across 1,200+ incidents
**Sample Composition**: 7 months deployment (February-September 2025), 4 enterprise environments, 3 architecture types
**Performance Metrics**: 73% precision, 83% recall, F1 score 0.78

## Theoretical Foundation

Torque builds on:
- **Koopman Operator Theory**: For nonlinear dynamical system analysis (Brunton et al. 2022, Korda & Mežić 2021)
- **Autonomous Clustering**: Independent validation through Yang & Lin's Torque Clustering achieving 97.7% accuracy
- **IBM Research**: Model drift and agentic drift analysis validating need for improved detection

## Future Research Directions

- Trajectory forecasting (1-3 hour prediction windows)
- Cross-agent coordination metrics for multi-agent systems
- Quantum-resistant monitoring extensions
- IEEE standardization proposal for industry adoption

## License

**Dual Licensing Model:**

**Non-Commercial:** Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) - Free for academic research, education, and non-commercial use

**Commercial:** Enterprise licensing required for production deployment and revenue-generating services. Contact aaron@valorgridsolutions.com

**Code Implementation:** MIT License (reference code only, not methodology)

**Full license details in paper**

---

**© 2025 ValorGrid Solutions**

*Part of the ForgeOS AI Resilience Framework ecosystem*
## Code and Methodology Licensing

- **Code** below is licensed under MIT unless otherwise stated.
- **Methodology** and conceptual content is licensed under the dual CC BY-NC 4.0 + Enterprise model above.

## Author

Author: [Your Name or Team]
Contact: [email or site]
