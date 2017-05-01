from rr_generator import rr_generator
from  spitter import split_set_tests, creates_holes
from fill_holes import filled_matrix
from accuracy_percentage import total_accuracy
import pdb

def init_main(matrix):
    training_set, test_set = split_set_tests(matrix)

    print "Total records of training set: \n"+str(len(training_set))
    print ""

    print "Total records of test set: \n"+str(len(test_set))
    print ""

    eigen_values,ratio_rules = rr_generator(training_set)

    test_set_with_holes = creates_holes(map(myFloat, test_set))

    rebuilded_test_set = filled_matrix(test_set_with_holes, ratio_rules)

    accuracy = total_accuracy(test_set, test_set_with_holes, rebuilded_test_set)

    print 'Total accuracy: '+str(accuracy)

# convert string list to float
def myFloat(myList):
    return map(float, myList)
