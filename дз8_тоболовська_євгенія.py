# -*- coding: utf-8 -*-
"""ДЗ8_Тоболовська Євгенія.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n24eyGG82l5Dk1z2gmQ1BF4YinjkW4vy
"""

import heapq

def min_cost_to_connect_cables(cable_lengths):
    # Convert the list of cable lengths into a min-heap
    heapq.heapify(cable_lengths)
    total_cost = 0

    # Continue combining the two smallest cables until one cable remains
    while len(cable_lengths) > 1:
        # Pop two smallest cables
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        # Combine the cables
        combined = first + second
        total_cost += combined

        # Push the combined cable back into the min-heap
        heapq.heappush(cable_lengths, combined)

    return total_cost

# Example usage:
cable_lengths = [5, 4, 2, 8]
print(min_cost_to_connect_cables(cable_lengths))