import matplotlib.pyplot as plt

def show_graph(days, red_counts, blue_counts):
    print("Generating graph...")
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(days, red_counts, color='red', label='Greedy (Red)', linewidth=2, marker='o', markersize=4)
    
    plt.plot(days, blue_counts, color='blue', label='Generous (Blue)', linewidth=2, marker='o', markersize=4)
    
    plt.title('Evolutionary Simulation: Greedy vs Generous')
    plt.xlabel('Days Passed')
    plt.ylabel('Population')
    plt.legend()
    plt.grid(True)
    
    plt.show()