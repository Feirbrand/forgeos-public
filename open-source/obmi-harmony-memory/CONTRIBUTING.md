# Contributing to OBMI Harmonic Memory

## Overview

OBMI Harmonic Memory is a theoretical research project exploring bio-inspired AI memory architectures. We welcome contributions that advance the theoretical understanding and conceptual implementation of harmonic memory principles.

## Contribution Categories

### 1. Theoretical Research
- Academic papers and references
- Neuroscience research connections
- Mathematical models and proofs
- Conceptual framework enhancements

### 2. Conceptual Implementation
- Code that demonstrates theoretical principles
- Simulation and visualization tools
- Example applications and use cases
- Performance benchmarking scripts

### 3. Documentation
- Architecture explanations
- Integration examples
- Tutorial content
- API documentation

## What We Accept

### Research Contributions
- Citations to relevant neuroscience literature
- Mathematical formulations of harmonic principles
- Theoretical performance analyses
- Conceptual diagrams and visualizations

### Code Contributions
- Implementations that demonstrate core concepts
- Simulation tools for theta-gamma coupling
- Fractal pattern generators
- Integration examples with existing frameworks

### Documentation Improvements
- Clearer explanations of theoretical concepts
- Better code examples
- Integration guides for other projects
- Performance analysis documentation

## What We Don't Accept

### Proprietary Implementations
This project maintains a theoretical focus. We do not accept:
- Production-ready implementations claiming operational use
- Code that references undisclosed proprietary systems
- Performance metrics from undisclosed real-world deployments
- Integration with proprietary AI systems not publicly documented

### Unsubstantiated Claims
- Performance improvements without theoretical basis
- Biological analogies without neuroscience citations
- Integration claims without proof-of-concept code
- Architectural advantages without mathematical foundation

## Contribution Process

### 1. Research Contributions
1. **Issue First**: Open an issue describing the theoretical contribution
2. **Literature Review**: Ensure proper citation of existing research
3. **Documentation**: Submit as markdown files in `/docs/research/`
4. **Peer Review**: Allow community review of theoretical claims

### 2. Code Contributions
1. **Fork the Repository**: Create your own fork for development
2. **Feature Branch**: Create a descriptive branch name (e.g., `harmonic-visualization`)
3. **Implementation**: Follow our coding standards (see below)
4. **Testing**: Include unit tests for your code
5. **Documentation**: Update relevant documentation
6. **Pull Request**: Submit with clear description of contribution

### 3. Documentation Improvements
1. **Identify Gap**: Find areas needing better documentation
2. **Research**: Ensure accuracy of theoretical claims
3. **Clear Writing**: Use accessible language while maintaining precision
4. **Examples**: Include code examples where appropriate
5. **Review**: Submit for community feedback

## Coding Standards

### Python Code Style
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Include comprehensive docstrings
- Maintain compatibility with Python 3.8+

### Documentation Standards
```python
def harmonic_function(theta_freq: float, gamma_freq: float) -> np.ndarray:
    """
    Generate harmonic signal based on theta-gamma coupling.
    
    This function demonstrates the theoretical principle of theta-gamma
    phase coupling as observed in biological memory systems.
    
    Args:
        theta_freq: Theta frequency in Hz (typically 4-8 Hz)
        gamma_freq: Gamma frequency in Hz (typically 30-80 Hz)
    
    Returns:
        np.ndarray: Harmonic signal demonstrating coupled oscillations
        
    References:
        - Buzsáki, G. (2006). Rhythms of the Brain. Oxford University Press.
        - Lisman, J. E., & Jensen, O. (2013). The theta-gamma neural code.
    """
```

### Testing Requirements
- Unit tests for all public functions
- Integration tests for complex workflows  
- Performance benchmarks for algorithms
- Documentation tests for examples

## Review Process

### Theoretical Contributions
1. **Academic Review**: Verify citations and theoretical accuracy
2. **Community Discussion**: Open for community feedback via issues
3. **Integration**: Merge if aligned with project goals

### Code Contributions
1. **Automated Testing**: All tests must pass
2. **Code Review**: At least one maintainer review required
3. **Documentation Review**: Ensure proper documentation
4. **Integration Testing**: Verify compatibility with existing code

## Research Ethics

### Academic Integrity
- Properly cite all sources and references
- Do not claim original discovery of well-established principles
- Acknowledge limitations and assumptions in theoretical work
- Distinguish between empirical claims and theoretical speculation

### Open Science Principles
- Make research reproducible through clear documentation
- Provide data and code for theoretical demonstrations
- Encourage peer review and community validation
- Maintain transparency about theoretical vs. empirical claims

## Community Guidelines

### Respectful Collaboration
- Focus on ideas rather than personalities
- Provide constructive feedback on contributions
- Acknowledge different perspectives on theoretical questions
- Maintain professional discourse in all interactions

### Quality Standards
- Theoretical contributions must be well-researched
- Code must be clean, tested, and documented
- Claims must be substantiated or clearly marked as speculative
- Integration examples should be realistic and practical

## Getting Started

### For Researchers
1. Review existing theoretical documentation in `/docs/`
2. Check open issues for research opportunities
3. Familiarize yourself with neuroscience literature on memory
4. Start with documentation contributions to understand the framework

### For Developers
1. Set up development environment: `pip install -r requirements-dev.txt`
2. Run existing examples to understand the codebase
3. Review coding standards and testing requirements
4. Start with small enhancements or bug fixes

### For Documentation Contributors
1. Identify areas needing better explanation
2. Review existing documentation for style and format
3. Test all code examples for accuracy
4. Submit improvements via pull requests

## Questions and Support

- **Theoretical Questions**: Open a discussion in the repository
- **Implementation Help**: Check existing issues or create new ones
- **Integration Support**: Refer to integration examples documentation
- **General Questions**: Use the repository discussions feature

## Recognition

Contributors are recognized through:
- Commit attribution in the repository
- Acknowledgment in theoretical publications
- Community recognition for significant contributions
- Co-authorship opportunities for major theoretical advances

---

*By contributing to OBMI Harmonic Memory, you help advance the theoretical understanding of bio-inspired AI memory architectures. Your contributions support open science principles and collaborative research in artificial intelligence.*