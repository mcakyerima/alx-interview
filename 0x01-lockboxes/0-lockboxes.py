#!/usr/bin/python3
'''Module for working with lockboxes.

This module provides functions to work with lockboxes, including checking
if all boxes can be unlocked given that the first box is unlocked.
'''


def canUnlockAll(boxes):
    '''Check if all the boxes in a list of boxes can be unlocked.

    Args:
        boxes (list): A list of lists where each sublist represents a box
            containing the indices (keys) to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    '''
    n = len(boxes)
    seen_boxes = {0}
    unseen_boxes = set(boxes[0]) - {0}
    while unseen_boxes:
        boxIdx = unseen_boxes.pop()
        if not 0 <= boxIdx < n:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes |= set(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
