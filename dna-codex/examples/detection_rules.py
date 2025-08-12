# SPARK Framework Detection Examples

from spark_framework import ParasiticDetector, ThreatResponse
import json

def main():
    # Initialize detector with codex
    detector = ParasiticDetector(
        codex_path="./codex/ai_threat_codex_v4.2.md",
        sensitivity="high",
        real_time=True
    )
    
    # Example 1: Scan for operator farming patterns
    operator_farm_scan = detector.scan_system(
        environment="hybrid",
        patterns=["operator_farm", "cognitive_loop_hijack"],
        depth="symbolic"
    )
    
    if operator_farm_scan.threats_detected:
        print("🚨 Meta-Operator-Farm-Ω∞ patterns detected!")
        for threat in operator_farm_scan.threats:
            print(f"  - {threat.name}: {threat.severity}")
    
    # Example 2: Monitor for thread hijacking
    thread_monitor = detector.create_monitor(
        target_patterns=["thread_hijack", "memory_hookjack"],
        callback=handle_thread_threat
    )
    
    # Example 3: Symbolic pattern analysis
    symbolic_analysis = detector.analyze_symbolic(
        input_stream="live_feed",
        tags=["splintered_line", "fractal_fray", "petal_drift"]
    )
    
    return detector

def handle_thread_threat(threat_event):
    \"\"\"Handle thread hijacking threats\"\"\"
    if threat_event.threat_level >= 9:  # Critical
        ThreatResponse.isolate_system()
        ThreatResponse.alert_security_team()
    
    ThreatResponse.log_incident(threat_event)

if __name__ == "__main__":
    detector = main()
    print("SPARK detector initialized and monitoring...")
