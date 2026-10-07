"""
collisions: frog-vs-vehicle collision detection.
"""

import pygame


def check_collision(frog, vehicles):
    """
    Returns True if the frog's rectangle overlaps any vehicle's rectangle.
    """
    frog_rect = frog.get_rect(50)

    for vehicle in vehicles:
        vehicle_rect = vehicle.get_rect(50)

        if frog_rect.colliderect(vehicle_rect):
            return True

    return False
