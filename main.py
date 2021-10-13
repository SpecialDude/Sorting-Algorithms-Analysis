import inspect
import sort
from sort import Sorting
from random import choices, randint
from random import random
import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

testdata = {}
testtype = ["sorted", "unsorted", "both"]
filetype = {"csv":",", "tsv":"\t"}
exporttypes = ["csv", "json", "xlsx", "html"]
MIN = 0
MAX = 1000


def generateRandomArray1(size, l_range, h_range):
    print(f"Minimum random number: {l_range}")
    print(f"Maximum random number: {h_range}")
    return [randint(l_range, h_range) for _ in range(size)]

def generateRandomArray(size, u_range=None):
    if u_range == None:
        u_range = size
    
    print(f"Maximum random number: {u_range}")
    array = [int(random() * u_range) for _ in range(size)]

    return array

def generateSortedArray1(size, min):
    print(f"Lowest Element: {min}")
    return [i for i in range(min, size)]

def generateSortedArray(size):
    array = []
    start = 0
    stop = randint(1, 10)
    next = [10, 30, 100, 20, 50, 200, 500]
    for i in range(size):
        rNum = randint(start, stop)
        array.append(rNum)
        start = rNum + 1
        stop += int(next[randint(0, len(next) - 1)] * random()) + 1
    return array
    
def generate(algorithm, size, *args):
    print("Generating Random Array...")
    print(f"Size: {size}")
    
    if algorithm == "URAmax":      # Unsorted Random array (Max element Only)
        array = generateRandomArray(size, *args)
    elif algorithm == "URAminmax":    # Unsoreted Random array (Min and Max elements required)
        array = generateRandomArray1(size, *args)
    elif algorithm == "SRAcomplex":    # Sorted Random array [Complex]
        array = generateSortedArray(size) 
    elif algorithm == "SRAsimple":    # Sorted Random array [Simple] (Required a stating Element)
        array = generateSortedArray1(size, *args)
    
    print(f"Array Generated!!!")
    if size <= 100:
        print(f"Generated Array: {array}")
    print("\n")
    return array


def perform(array, sortAlgorithm, inplace=True):
    extra = "Sorting In Place"
    original = array[:]
    if not inplace:
        array = array[:]
        extra = "Sorting On a Copy"
    print(f"Sorting Algorithm: {sortAlgorithm.__name__}")
    print(f"Array Size: {len(array)}")
    print(f"Sort Method: {extra}")
    print("Sorting...")

    print(f"Start Time: {time.asctime()}")
    start = int(round(time.perf_counter() * 1000))
    result = sortAlgorithm(array)
    stop = int(round(time.perf_counter() * 1000))
    time_taken = stop - start
    print(f"Sorting Completed: in {time_taken} milliseconds")
    print(f"Stop Time: {time.asctime()}")
    if len(array) <= 100:
        print(f"Original Array: {original}")
        if result is not None:
            array = result
        print(f"The Sorted Array: {array}")
    print("\n")
    return time_taken


def exportOLD(data, filename, type="csv"):
    delimiter = filetype[type]
    
    for test_type, test_data in data.items():

        heading = "Array Size" + delimiter + delimiter.join(list(test_data[list(test_data.keys())[0]].keys()))
        filenamew = f"{filename} ({test_type}).{type}"
        with open(filenamew, "w+") as file_handler:
            file_handler.write(heading + "\n")
            for array_size in test_data.keys():
                array_data = list(test_data[array_size].values())
                line = f"{array_size}{delimiter}" + delimiter.join([str(i) for i in array_data])
                file_handler.write(line + "\n")
        print(f"Export completed --> {filenamew}")

def export(data, filename, type):
    
    for test_type, test_data in data.items():
        filenamew = f"{filename} ({test_type})." + type
        if type == "csv":
            test_data.to_csv(filenamew)
        elif type == "xlsx":
            test_data.to_excel(filenamew)
        elif type == "json":
            test_data.to_json(filenamew)
        elif type == "html":
            test_data.to_html(filenamew)
        print(f"Export completed --> {filenamew}")
        
        

def makePlots(plot_type, data:dict[str, pd.DataFrame]):
    """for name, sort_data in data.items():
        plt.plot(array_sizes, sort_data.values(), label=name)
        
    plt.ylabel("Time in seconds")
    plt.xlabel("Array Size")
    plt.legend()
    plt.show()"""
    
    for test_type, test_data in data.items():
        data = pd.DataFrame(test_data)
        plt.title(f"Time Complexity of Sorting Algorithms on {test_type} Arrays")

        if plot_type in (1, 2):
            sort_algorithms = test_data.index
            array_sizes = test_data.columns
            for algorithm in sort_algorithms:
                y = test_data.loc[algorithm]
                if plot_type == 1:
                    plt.plot(array_sizes, y, label=algorithm)
                else:
                    plt.scatter(array_sizes, y, label=algorithm)
        
        elif plot_type == 3:
            pass
            '''sort_algorithms = test_data.index
            array_sizes = test_data.columns

            x_axis = np.arange(len(array_sizes))
            space = 0
            width = 0.25
            i = 1

            h = (width - space) / (len(sort_algorithms) - 1)
            for algorithm in sort_algorithms:
                time = test_data.loc[algorithm]
                plt.bar(x_axis + space, time, width=width, label=algorithm)
                space = (h * i) + (width - h)
                i += 1
            plt.xticks(x_axis + width, array_sizes)'''


        
        plt.ylabel("Time in Milliseconds")
        plt.xlabel("Array Size")
        plt.legend()
        plt.show()
            
    
def run(kwargs):
    """
    Arguments
        array_sizes:    A list of array sizes to to generate
        sort_algorithm: A list of the Sorting Algorthm to Implement
        test_type:      A string of the type of array to generate (sorted, unsorted, both)
        export_file:    A string of the file type to export the test data (csv, tsv)
        file_name:      File name to save the exported data
        visualize:      A boolean value (To visualize the test data or not)
        plot_type:      An integer value specifying the plot type (1 --> line plot, 2 --> scatter, 3 --> Histogram)
        max_element:    The maximum element in the generated array
        min_element:    The mininum element in the generated array
        file_name:      File name for the exported test data
        file_type:      File type for the exported
    """
    # test_type
    #     "sorted": perform test on sorted Arrays
    #     "unsorted": perform test on Unsorted Randomly Generated Array
    #     "both": perform both sorted and unsorted test

    print(f"\n\n========================> Generating Data <========================\n")
    test_type = kwargs["test_type"]
    array_sizes = kwargs["array_sizes"]

    generatedData = {}
    if test_type == "sorted" or test_type == "both":
        min_element = kwargs.get("min_element")
        if min_element == None:
            algorithm = "SRAcomplex"
        else:
            algorithm = "SRAsimple"
        # generatedData["sorted"] = [generateSortedArray(size, min_element) for size in array_sizes]
        generatedData["sorted"] = [generate(algorithm, size, min_element) for size in array_sizes]
    
    if test_type == "both" or test_type == "unsorted":
        args = []
        max_element = kwargs.get("max_element")
        min_element = kwargs.get("min_element")

        if max_element != None and min_element == None:
            algorithm = "URAmax"
            args.append(max_element)
        else:
            if max_element == None:
                max_element = MAX
            if min_element == None:
                min_element = MIN            
            algorithm = "URAminmax"
            args.append(min_element)
            args.append(max_element)
        
        # generatedData["unsorted"] = [generateRandomArray(size, ) for size in array_sizes]
        generatedData["unsorted"] = [generate(algorithm, size, *args) for size in array_sizes]
    
    sort_algorithms = kwargs["sort_algorithms"]
    for type, arrays in generatedData.items():
        print(f"\n\n========================> Peforming Test on {type} arrays <========================\n")
        testdata[type] = {len(array): {algorithm.__name__:perform(array, algorithm, inplace=False) for algorithm in sort_algorithms} for array in arrays}
    
    
    print(f"\n========================> Test Results <========================\n")
    TESTDATA = {}
    for test_type, data in testdata.items():
        data = pd.DataFrame(data)
        print(f"Test Type: Test on {test_type} array")
        print(data)
        TESTDATA[test_type] = data
        
        print("\n")
    
    import pprint
    pprint.pprint(testdata)

    print(f"\n========================> Exporting <========================\n")
    file_type = kwargs.get("file_type")
    file_name = kwargs.get("file_name")
    export(TESTDATA, file_name, file_type)


    visualize = kwargs.get("visualize")
    if visualize:
        print(f"\n========================> Plotting <========================\n")
        plot_type = kwargs.get("plot_type")
        makePlots(plot_type, TESTDATA)




    



def main2():
    print("Starting Program!!!")
    sorter = [func for name, func in inspect.getmembers(Sorting) if inspect.isfunction(func)]
    array_sizes = (2, 4, 8, 32, 64, 128, 512, 1024)

    print("\n\nGenerating The Needed Arrays")
    arrays = [generateRandomArray(i) for i in array_sizes]

    data = {}
    for algorithm in sorter:
        print(f"Implementing {algorithm.__name__} Algorithm\n")
        time = {len(array): perform(array, algorithm, inplace=False) for array in arrays}
        data[algorithm.__name__] = time
    
    print("\nEnd of Program!!!")
    print("\n\nGenerated Data!!!")
    print(data)

    print("Plotting The data")

    for name, sort_data in data.items():
        plt.plot(array_sizes, sort_data.values(), label=name)
        
    plt.ylabel("Time in seconds")
    plt.xlabel("Array Size")
    plt.legend()
    plt.show()

def u_input(max_choice, prompt="\n: "):
    while True:
        userin = input(prompt)
        try:
            userin = int(userin)
        except:
            print(f"{userin} --> please input a number from the choices above")
            continue

        if userin > max_choice or userin < 1:
            print(f"{userin} --> Select a number within the choice range")
            continue

        return userin

def main():
    print("\nWelcome to Sorting Algorthm Testing")

    #--------------------------> Sorting Algortihm <--------------------------
    print("\n--------------------------> Sorting Algortihm <--------------------------")
    print("\nSelect the Sorting Algorithm(s) you want to test (Choose multiple indexes seperating by a space)\n")

    test_datas = {}
    algorithms = sort.getAlgorithmNames()
    for i in range(len(algorithms)):
        print(f"{i + 1}. {algorithms[i]}")
    
    while True:
        userin = input("\n: ")

        if userin == "all" or userin == "":
            choices = None
            break

        choices = userin.split()

        try:
            for i in range(len(choices)):
                choice = choices[i]
                choice = int(choice)
                if choice > len(algorithms) or choice < 1:                    
                    raise Exception
                choice -= 1
                choices[i] = algorithms[choice]
            break
        except ValueError:
            print(f"{choice} --> Invalid Input: please input a number corresponding to the sorting algorithm")
        except Exception:
            print(f"{choice} --> The Number selected is not available")
    
    # sort_algorithms = sort.getAlgorithm(filter=choices)
    test_datas["sort_algorithms"] = sort.getAlgorithm(filter=choices)
    
    #--------------------------> Generating Data <--------------------------
    print("\n--------------------------> Data <--------------------------")
    print("Please select the type of data you want to perform test on\n")
    print("1. Sorted Data\n2. Unsorted\n3. Both")

    # test_type = testtype[u_input(3) - 1]
    test_datas["test_type"] = testtype[u_input(3) - 1]

    print("\nInput the sizes of the random data to generate (seperated by a single space)")

    while True:
        array_sizes = input("\n: ")
        
        array_sizes = array_sizes.strip().split()

        if not array_sizes:
            print("Pls input some values")
            continue

        try:
            for i in range(len(array_sizes)):
                array_sizes[i] = int(array_sizes[i])
        except:
            print(f"{array_sizes[i]} --> please input a whole integer value")
            continue
        break
    test_datas["array_sizes"] = array_sizes


    print("\n--------------------------> Test Data Exporting <--------------------------")
    print("Choose a file type to export the data")
    
    for i in range(len(exporttypes)):
        print(f"{i + 1}. {exporttypes[i]}")
    
    file_type = u_input(len(exporttypes)) - 1
    file_type = exporttypes[file_type]
    file_name = input("Enter The file name: ")

    test_datas["file_type"] = file_type
    test_datas["file_name"] = file_name

    print("\n--------------------------> Plotting <--------------------------")

    print("Show the graph of the data?")
    print("1. Yes\n2. No")
    visualize = u_input(2)
    visualize = True if visualize == 1 else False
    plot_type = None
    if visualize:
        print("Select Ploting type")
        print("1. Line Plot\n2. Scatter Plot")
        plot_type = u_input(2)
    test_datas["visualize"] = visualize
    test_datas["plot_type"] = plot_type

    print("\n___________________________________________________________________________________")
    print("\n\nStarting Test...")
    
    run(test_datas)

    
if __name__ == "__main__":
    main()
