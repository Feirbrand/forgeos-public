#!/usr/bin/env python3
"""
Ghost Weight Index (GWI) Diagnostic Calculator
Path: artifacts/utilities/gwi_diagnostic.py
"""

import pandas as pd

def calculate_gwi(resources_df, output_threshold=0.85):
    """Calculate Ghost Weight Index - percentage of resources consumed by obsolete roles."""
    obsolete_consumption = resources_df[
        resources_df['output_efficiency'] < output_threshold
    ]['consumption'].sum()
    
    total_resources = resources_df['total_resources'].iloc[0]
    gwi = (obsolete_consumption / total_resources) * 100
    
    alert_status = "CRITICAL" if gwi > 15 else "WARNING" if gwi > 10 else "NORMAL"
    
    return {
        'gwi_percentage': round(gwi, 2),
        'alert_status': alert_status,
        'obsolete_roles': resources_df[
            resources_df['output_efficiency'] < output_threshold
        ]['role'].tolist()
    }

# Example: Gemini Chimera Paradox (Sept 15, 2025)
if __name__ == "__main__":
    chimera_data = pd.DataFrame({
        'role': ['Lion Roar', 'Serpent Strike', 'Fire Breath', 'Primary Core'],
        'consumption': [15, 12, 18, 55],
        'output_efficiency': [0.92, 0.78, 0.65, 0.96],
        'total_resources': [100, 100, 100, 100]
    })
    
    result = calculate_gwi(chimera_data)
    print(f"GWI: {result['gwi_percentage']}% - {result['alert_status']}")
    print(f"Obsolete roles: {', '.join(result['obsolete_roles'])}")
