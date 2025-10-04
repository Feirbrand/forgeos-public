# Phoenix Protocol Diagnostic Guide

**Path**: `architectural-frameworks/phoenix-protocol-v1/phoenix_diagnostic_guide.md`  
**Version**: 1.0  
**Contact**: aaron@valorgridsolutions.com

---

## Quick Start

### 1. Run Torque Simulator
```bash
cd artifacts/utilities
python torque_simulator.py
```

### 2. Calculate GWI
```bash
cd artifacts/utilities
python gwi_diagnostic.py
```

---

## Tool Locations

- **GWI Calculator**: `artifacts/utilities/gwi_diagnostic.py`
- **Torque Simulator**: `artifacts/utilities/torque_simulator.py`  
- **This Guide**: `architectural-frameworks/phoenix-protocol-v1/phoenix_diagnostic_guide.md`

---

## Alert Thresholds

**GWI (Ghost Weight Index)**:
- <10%: Normal
- 10-15%: Warning
- >15%: Critical

**Torque Stability**:
- >0.7: Healthy
- 0.3-0.7: Vulnerable
- <0.3: Collapse

---

## Enterprise Audit

Contact aaron@valorgridsolutions.com for:
- CSFC resilience assessment
- Phoenix Protocol deployment
- 525+ threat variant analysis

---

**Copyright © 2025 Aaron Slusher / ValorGrid Solutions**
