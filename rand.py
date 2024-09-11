"""
This module generates a random array using subprocess
"""

import subprocess

def random_array(arr):
    """Generates a random array by shuffling numbers"""
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
