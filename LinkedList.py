#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 13:42:36 2020

@author: chenyuwang
"""

class ListNode:
    # Create Node Object
    # Initialize Linked List Node
    def __init__(self, value):
        self.next = None
        self.value = value

def print_all_node(head):
    # Print all node in linked list
    # Assuming that the head is first node of linked list
    while head:
        print(head.value)
        head = head.next

def count_all_node(head):
    # Count the number of nodes in linked list
    # Assuming that the head is first node of linked list
    count = 0
    while head:
        count += 1
        head = head.next

def search_by_index(head, index):
    # Search the node by index
    # Assuming index >= 0
    # Return the node if found and None otherwise
    if head is None or index < 0:
        return None
    for move in range(index):
        head = head.next
        if head is None:
            return None
    return head

def search_by_value(head, value):
    # Search the node by value
    # Return the index if found and None otherwise
    if not head:
        return None
    current_node = head
    count = 0
    while head:
        if current_node.value == value:
            return count
        current_node = head.next
        count = count + 1
    return None

def add_to_index(head, index, value):
    # Add a new node to the linked list by index
    # head: the head of the linked list
    # index: the index of the new node that we want to insert
    # value: the value of the new node
    # Assuming index >= 0
    if index < 0:
        raise ValueError('Index should be 0 or positive integer')
    if head is None:
        raise ValueError('No linked list found')
    fake_head = ListNode('Free')
    fake_head.next = head
    insert_place = search_by_index(fake_head, index)
    if insert_place is None:
        raise ValueError('Index is out of boundary')
    new_node = ListNode(value)
    new_node.next = insert_place.next
    insert_place.next = new_node
    return fake_head.next

def remove_to_index(head, index):
    # Remove a node from the linked list by index
    # head: the head of the linked list
    # index: the index of the node that we want to remove
    # Assuming index >= 0
    if index < 0:
        raise ValueError('Index should be 0 or positive integer')
    if head is None:
        raise ValueError('No linked list found')
    fake_head = ListNode('Free')
    fake_head.next = head
    remove_place = search_by_index(head, index)
    remove_node = remove_place.next
    remove_place.next = remove_node.next
    remove_node.next = None
    return fake_head.next
    
        