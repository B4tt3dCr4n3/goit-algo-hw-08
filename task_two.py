"""Дано k відсортованих списків цілих чисел. Ваше завдання — об'єднати 
їх у один відсортований список. Тепер при виконанні завдання ви повинні 
використати мінімальну купу для ефективного злиття кількох відсортованих 
списків в один відсортований список. Реалізуйте функцію merge_k_lists, яка 
приймає на вхід список відсортованих списків та повертає відсортований список."""

import heapq

def merge_k_lists(lists):
    # Мін-купа для зберігання перших елементів кожного списку
    heap = []
    
    # Додаємо перші елементи кожного списку до купи
    for i, sorted_list in enumerate(lists):
        if sorted_list:
            heapq.heappush(heap, (sorted_list[0], i, 0))  # (значення, індекс списку, індекс елемента)
            print(f"Додаємо {sorted_list[0]} з списку {i} до купи: {heap}")
    
    merged_list = []
    
    while heap:
        value, list_idx, element_idx = heapq.heappop(heap)
        merged_list.append(value)
        print(f"Витягуємо {value} з купи: {heap}")
        
        # Якщо список ще містить елементи, додаємо наступний елемент до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_value, list_idx, element_idx + 1))
            print(f"Додаємо {next_value} з списку {list_idx} до купи: {heap}")
    
    return merged_list

# Тестування
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
