#Biyi Abass
#CS175L
#ExpensePieChart

import matplotlib.pyplot as plt

def main():
    slice_labels = []
    expense_value = []

    try:

        expense_chart = open('expenses.txt', 'r')
        
        for line in file:
            line.rstrip('\n')
            cols = linesplit('\t')
            slice_labels.append(cols[0])
        try:
            num = float(cols[1])
            expenses_values.append(cols[1])
        except ValueError:
            print(f"Could not convert line '{cols[1]}' to a number.")

        file.close()

        try:
            plt.pie(costs, lables=slice_labels)

            plt.title('Monthly Expenses')

            plt.show()

        except:
            print("Invalid inputs to display pie chart")


        

    except IOError:
        print('An error occured trying to read the file.')
        
if __name__ == '___main__':
        main()       
    
