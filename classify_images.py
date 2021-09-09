#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: TREVOR NAGABA
# DATE CREATED: 24/08/2021                     
# REVISED DATE: 24/08/2021
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

from get_pet_labels import get_pet_labels

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese' 
    so the classifier label = 'maltese dog, maltese terrier, maltese'.
    Recall that dog names from the classifier function can be a string of dog 
    names separated by commas when a particular breed of dog has multiple dog 
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian'(pet label) and it will match to the classifier label 
    'dalmatian, coach dog, carriage dog' if the classifier function correctly 
    classified the pet images of dalmatians.
     PLEASE NOTE: This function uses the classifier() function defined in 
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the 
     classifier() function to classify images within this function 
     Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    
        
    # Get pet labels
    pet_labels = get_pet_labels(images_dir)
    print("pet labels:"+str(pet_labels))
    
    
    # Imports only listdir function from OS module 
    from os import listdir  

    # Retrieve the filenames from folder pet_images/
    filename_list = listdir(images_dir)
    
    # NOTE: image_classication is a text string - It contains mixed case(both lower
    # and upper case letter) image labels that can be separated by commas when a 
    # label has more than one word that can describe it.
    for idx in range(0, len(filename_list), 1):
        # Create full image directory
        test_image = images_dir+filename_list[idx]
        # Run classifier
        image_classification = classifier(test_image, model)
        # Update classification to lower case and remove leading/trailing whitespaces
        clean_image_classification = image_classification.lower().strip()
        # prints result from running classifier() function
#         print("\nResults from test_classifier.py\nImage:", test_image, "using model:"
#               model, "was classified as a:", clean_image_classification)
        #results_dic = pet_labels[filename_list[idx]].append(clean_image_classification)
        # Create new results dictionary including pet label and classifier label
        # Did this only because the append/extend cose failed, which was a more eloquent solution
        results_dic[filename_list[idx]] = [pet_labels[filename_list[idx]][0], clean_image_classification]
#         print("Dictionary with classification added:"+str(results_dic))
        # Determine if pet_labels matches classifier_labels using in operator
        # - so if pet label is 'in' classifier label it's a match
        # ALSO since Key already exists because labels were added, append 
        # value to end of list for idx 2 
        # if pet image label was FOUND then there is a match 
        if results_dic[filename_list[idx]][0] in results_dic[filename_list[idx]][1]:
            results_dic[filename_list[idx]].append(1)

        # if pet image label was NOT found then there is no match
        else:
            results_dic[filename_list[idx]].append(0)
            
#         print("Final results dic:"+str(results_dic))