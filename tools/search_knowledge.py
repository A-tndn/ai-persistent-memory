#!/usr/bin/env python3
"""
Simple CLI search tool for technical knowledge base
Usage: python search_knowledge.py "github api"
"""

import json
import sys
import re

def search_knowledge(query, max_results=10):
    # Load knowledge base
    with open('technical_knowledge_searchable.json', 'r', encoding='utf-8') as f:
        kb = json.load(f)

    query_lower = query.lower()
    results = []

    for entry in kb['search_index']:
        score = 0

        # Check title match
        if query_lower in entry['title'].lower():
            score += 10

        # Check keyword matches
        for keyword in entry['keywords']:
            if query_lower in keyword.lower():
                score += 5

        # Check preview content
        if query_lower in entry['preview'].lower():
            score += 3

        if score > 0:
            results.append((score, entry))

    # Sort and return results
    results.sort(key=lambda x: x[0], reverse=True)
    return [entry for score, entry in results[:max_results]]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search_knowledge.py \"search query\"")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    results = search_knowledge(query)

    print(f"Search results for: '{query}'")
    print("-" * 50)

    if results:
        for i, result in enumerate(results):
            print(f"{i+1}. {result['title']}")
            print(f"   Categories: {', '.join(result['categories'])}")
            print(f"   Preview: {result['preview'][:100]}...")
            print()
    else:
        print("No results found.")
