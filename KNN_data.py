<<<<<<< HEAD
# # Train
# x_ref = [[0.0, 3.3, 6.7, 10.0, 13.3, 16.7, 20.0],
#          [0.0, 3.3, 6.7, 10.0, 13.3, 16.7, 20.0],
#          [0.0, 3.3, 6.7, 10.0, 13.3, 16.7, 20.0],
#          [0.0, 3.3, 6.7, 10.0, 13.3, 16.7, 20.0]]
# y_ref = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
#          [3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3],
#          [6.7, 6.7, 6.7, 6.7, 6.7, 6.7, 6.7],
#          [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]]
# AP1_raw_data = [[-52.0,	-42.0,	-39.5,	-52.5,	-57.5,	-58.5,	-60.5],
#                 [-54.5,	-48.5,	-45.5,	-52.0,	-55.5,	-56.0,	-62.5],
#                 [-59.5,	-56.5,	-56.0,	-59.5,	-59.5,	-60.0,	-63.0],
#                 [-62.5,	-58.0,	-60.0,	-59.0,	-59.5,	-59.0,	-62.0]]
# AP2_raw_data = [[-61.5,	-66.0,	-64.5,	-61.5,	-56.5,	-47.0,	-58.5],
#                 [-66.0,	-64.0,	-63.5,	-62.5,	-57.0,	-53.5,	-56.0],
#                 [-66.5,	-67.0,	-66.5,	-58.5,	-61.0,	-68.5,	-59.5],
#                 [-65.5,	-65.5,	-67.5,	-65.5,	-64.5,	-69.0,	-67.0]]
# AP3_raw_data = [[-67.0,	-63.5,	-57.0,	-59.0,	-66.5,	-69.0,	-68.5],
#                 [-67.0,	-58.5,	-56.0,	-63.5,	-63.0,	-67.5,	-70.0],
#                 [-61.0,	-53.5,	-51.5,	-63.0,	-61.0,	-68.5,	-74.5],
#                 [-59.5,	-49.0,	-54.0,	-55.5,	-60.5,	-59.0,	-62.5]]
# AP4_raw_data = [[-71.5,	-70.5,	-66.5,	-66.0,	-66.0,	-62.5,	-69.0],
#                 [-65.0,	-66.0,	-67.0,	-65.5,	-64.5,	-62.5,	-60.0],
#                 [-66.0,	-68.0,	-63.0,	-66.0,	-59.0,	-51.5,	-55.0],
#                 [-64.5,	-64.0,	-65.5,	-63.0,	-60.5,	-49.5,	-50.5]]

# Train_data = []
=======
# Train
x_ref = [[0.0, 3.3, 6.7, 10.0, 13.3, 16.7, 20.0],
         [0.0, 3.3, 6.7, 10.0, 13.3, 16.7, 20.0],
         [0.0, 3.3, 6.7, 10.0, 13.3, 16.7, 20.0],
         [0.0, 3.3, 6.7, 10.0, 13.3, 16.7, 20.0]]
y_ref = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
         [3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3],
         [6.7, 6.7, 6.7, 6.7, 6.7, 6.7, 6.7],
         [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]]
AP1_raw_data = [[-52.0,	-42.0,	-39.5,	-52.5,	-57.5,	-58.5,	-60.5],
                [-54.5,	-48.5,	-45.5,	-52.0,	-55.5,	-56.0,	-62.5],
                [-59.5,	-56.5,	-56.0,	-59.5,	-59.5,	-60.0,	-63.0],
                [-62.5,	-58.0,	-60.0,	-59.0,	-59.5,	-59.0,	-62.0]]
AP2_raw_data = [[-61.5,	-66.0,	-64.5,	-61.5,	-56.5,	-47.0,	-58.5],
                [-66.0,	-64.0,	-63.5,	-62.5,	-57.0,	-53.5,	-56.0],
                [-66.5,	-67.0,	-66.5,	-58.5,	-61.0,	-68.5,	-59.5],
                [-65.5,	-65.5,	-67.5,	-65.5,	-64.5,	-69.0,	-67.0]]
AP3_raw_data = [[-67.0,	-63.5,	-57.0,	-59.0,	-66.5,	-69.0,	-68.5],
                [-67.0,	-58.5,	-56.0,	-63.5,	-63.0,	-67.5,	-70.0],
                [-61.0,	-53.5,	-51.5,	-63.0,	-61.0,	-68.5,	-74.5],
                [-59.5,	-49.0,	-54.0,	-55.5,	-60.5,	-59.0,	-62.5]]
AP4_raw_data = [[-71.5,	-70.5,	-66.5,	-66.0,	-66.0,	-62.5,	-69.0],
                [-65.0,	-66.0,	-67.0,	-65.5,	-64.5,	-62.5,	-60.0],
                [-66.0,	-68.0,	-63.0,	-66.0,	-59.0,	-51.5,	-55.0],
                [-64.5,	-64.0,	-65.5,	-63.0,	-60.5,	-49.5,	-50.5]]
>>>>>>> d10bbd58291490a6936d3b05c91201fd2de25e16

# for i in range(4):
#     for j in range(7):
#         x = [AP1_raw_data[i][j], AP2_raw_data[i][j], AP3_raw_data[i][j], AP4_raw_data[i][j],
#              x_ref[i][j], y_ref[i][j]]
#         Train_data.append(x)

<<<<<<< HEAD
# # Test
# x_ref = [[2, 6, 10, 14, 18, 20],
#          [2, 6, 10, 14, 18, 20],
#          [2, 6, 10, 14, 18, 20]]
# y_ref = [[2, 2, 2, 2, 2, 2],
#          [5, 5, 5, 5, 5, 5],
#          [8, 8, 8, 8, 8, 8]]
# AP1_raw_data = [[-54, -38, -43, -47, -57, -58],
#                 [-61, -56, -57, -65, -55, -57],
#                 [-55, -60, -55, -64, -55, -58]]
# AP2_raw_data = [[-73, -66, -65, -58, -45, -61],
#                 [-67, -67, -61, -60, -49, -64],
#                 [-70, -65, -66, -62, -60, -57]]
# AP3_raw_data = [[-59, -65, -54, -57, -66, -67],
#                 [-58, -52, -56, -67, -69, -63],
#                 [-60, -41, -48, -60, -67, -73]]
# AP4_raw_data = [[-67, -67, -62, -62, -65, -67],
#                 [-70, -62, -67, -60, -56, -51],
#                 [-70, -65, -66, -61, -47, -51]]
# Test_data = []
=======
for i in range(4):
    for j in range(7):
        x = [AP1_raw_data[i][j], AP2_raw_data[i][j], AP3_raw_data[i][j], AP4_raw_data[i][j],
             x_ref[i][j], y_ref[i][j]] 
        Train_data.append(x)
>>>>>>> d10bbd58291490a6936d3b05c91201fd2de25e16

# for i in range(3):
#     for j in range(6):
#         x = [AP1_raw_data[i][j], AP2_raw_data[i][j], AP3_raw_data[i][j], AP4_raw_data[i][j],
#              x_ref[i][j], y_ref[i][j]]
#         Test_data.append(x)


Train_data = [
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord]
]

Test_data = [
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord],
    [LaptopSS, DesktopSS, xcoord, ycoord]
]
