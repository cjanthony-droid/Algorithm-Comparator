import matplotlib.pyplot as plt
import numpy as np

def plot_algorithm_scenarios(algorithm_name, best_case, worst_case, average_case, filename):
    # Number of elements
    n = np.arange(1, 101)

    # Plotting the scenarios with custom style
    plt.figure(figsize=(10, 6))
    ax = plt.gca()

    # Setting the background color
    ax.set_facecolor('#133263')

    # Plotting the data with contrasting colors
    ax.plot(n, best_case, label='Best Case (O(n))', color='#55c267')
    ax.plot(n, worst_case, label='Worst Case (O(n^2))', color='#c26655')
    ax.plot(n, average_case, label='Average Case (O(n^2/2))', color='#c2c255')

    # Setting labels and title with white color
    plt.xlabel('Number of elements', color='white')
    plt.ylabel('Time complexity', color='white')
    plt.title(f'Time Complexity of {algorithm_name}', color='white')

    # Customizing the legend
    legend = plt.legend()
    plt.setp(legend.get_texts(), color='white')

    # Customizing tick parameters
    ax.tick_params(colors='white')

    # Adding grid with white lines
    plt.grid(color='white', linestyle='--', linewidth=0.5)

    # Save the plot as an image
    plt.savefig(filename, bbox_inches='tight', facecolor='#133263')
    plt.close()

# Example usage for Insertion Sort
n = np.arange(1, 101)
best_case = n  # O(n)
worst_case = n**2  # O(n^2)
average_case = n**2 / 2  # O(n^2 / 2)
plot_algorithm_scenarios("Insertion Sort", best_case, worst_case, average_case, "insertion_sort_complexity.png")
# Example usage for Bubble Sort
n = np.arange(1, 101)
best_case_bubble = n  # O(n)
worst_case_bubble = n**2  # O(n^2)
average_case_bubble = n**2 / 2  # O(n^2 / 2)

plot_algorithm_scenarios("Bubble Sort", best_case_bubble, worst_case_bubble, average_case_bubble,
                         "bubble_sort_complexity.png")
# Example usage for Selection Sort
n = np.arange(1, 101)
best_case_selection = n**2 / 2  # O(n^2 / 2)
worst_case_selection = n**2  # O(n^2)
average_case_selection = n**2 / 2  # O(n^2 / 2)

plot_algorithm_scenarios("Selection Sort", best_case_selection, worst_case_selection, average_case_selection,
                         "selection_sort_complexity.png")
# Example usage for Iterative Merge Sort
n = np.arange(1, 101)
best_case_merge_iter = n * np.log(n)  # O(n log n)
worst_case_merge_iter = n * np.log(n)  # O(n log n)
average_case_merge_iter = n * np.log(n)  # O(n log n)

plot_algorithm_scenarios("Iterative Merge Sort", best_case_merge_iter, worst_case_merge_iter, average_case_merge_iter,
                         "iterative_merge_sort_complexity.png")

# Example usage for Recursive Merge Sort
n = np.arange(1, 101)
best_case_merge_recur = n * np.log(n)  # O(n log n)
worst_case_merge_recur = n * np.log(n)  # O(n log n)
average_case_merge_recur = n * np.log(n)  # O(n log n)

plot_algorithm_scenarios("Recursive Merge Sort", best_case_merge_recur, worst_case_merge_recur, average_case_merge_recur,
                         "recursive_merge_sort_complexity.png")
# Example usage for Heap Sort
n = np.arange(1, 101)
best_case_heap = n * np.log(n)  # O(n log n)
worst_case_heap = n * np.log(n)  # O(n log n)
average_case_heap = n * np.log(n)  # O(n log n)

plot_algorithm_scenarios("Heap Sort", best_case_heap, worst_case_heap, average_case_heap,
                         "heap_sort_complexity.png")

# Example usage for Quick Sort
n = np.arange(1, 101)
best_case_quick = n * np.log(n)  # O(n log n)
worst_case_quick = n**2  # O(n^2)
average_case_quick = n * np.log(n)  # O(n log n)

plot_algorithm_scenarios("Quick Sort", best_case_quick, worst_case_quick, average_case_quick,
                         "quick_sort_complexity.png")

