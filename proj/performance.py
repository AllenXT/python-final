import sys
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from markov import identify_speaker

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(
            f"Usage: python3 {sys.argv[0]} <filenameA> <filenameB> <filenameC> <max-k> <runs>"
        )
        sys.exit(1)

    # extract parameters from command line & convert types
    filenameA, filenameB, filenameC, max_k, runs = sys.argv[1:]
    max_k = int(max_k)
    runs = int(runs)

    # TODO: add code here to open files & read text
    textA = read_file(filenameA)
    textB = read_file(filenameB)
    textC = read_file(filenameC)

    # TODO: run performance tests as outlined in README.md
    data = []
    for k in range(1, max_k+1):
        for use_hashtable in [True, False]:
            for run in range(1, runs+1):
                start = time.perf_counter()
                tup = identify_speaker(textA, textB, textC, k, use_hashtable)
                elapsed = time.perf_counter() - start
                implementation = "hashtable" if use_hashtable else "dict"
                data.append((implementation, k, run, elapsed))
    
    # create the dataframe  
    df = pd.DataFrame(data, columns=['Implementation', 'K', 'Run', 'Time'])
    # group by the implementation and k and compute the avg time
    avg_df = df.groupby(['Implementation', 'K'])['Time'].mean().reset_index()
    
    # TODO: write execution_graph.png
    sns.set(style='whitegrid')
    sns.pointplot(x='K', y='Time', hue='Implementation', data=avg_df, linestyles='-', markers='o')
    plt.title('Average Performance Comparison(HashTable vs Python Dict)')
    plt.xlabel('K')
    plt.ylabel(f'Average Time(Runs={runs})')
    plt.savefig('execution_graph.png')