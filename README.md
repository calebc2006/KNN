# KNN

KNN.py is the actual algorithm
Basically it works by finding euclidean (straight line) distance from the input vector <AP1_RSSI, AP2_RSSI, AP3_RSSI, AP4_RSSI> to each training/reference point which is also a 4d vector of recieved signal intensities from each AP. You can change the number of APs - the more the better. Using the top k nearest reference/training points in that 4d space, the prediction is made by using a weighted sum of the k locations, inversely proportional to square of the euclidean distance (change ORDER variable to change to linear, inverse cube relation etc). Would be interesting to figure out which order works best but it would make the most sense in a physics context if it were an inverse square relation since everything seems to follow that.

KNN_data.py is where you insert your data

KNN_errors.csv is where the output is written (open in excel to plot graph if you don't like the look of matplotlib graphs)
