import numpy as np

def detect_anomaly(values, threshold=3.0):
    """
    Detects anomalies in a list of numeric values using z-score.
    Returns indices of anomalies.
    """
    if len(values) < 2:
        return []
    mean = np.mean(values)
    std = np.std(values)
    if std == 0:
        return []
    z_scores = [(x - mean) / std for x in values]
    return [i for i, z in enumerate(z_scores) if abs(z) > threshold] 