nums = [-108, 977, 915, -19, -32, -723, -621, -9, -924, 895, -476, -959, 828, 864, -524, -691, -688, 747, -8, -471, 188, 763, 326, -1, 819, -670, 231, -606, -946, 616, -234, 237, -950, -382, -286, -975, 853, 35, -487, -679, 353, -714, 495, 538, 647, -473, -713, 241, 157, -840, -4, 904, 133, 985, -952, -837, -209, 935, 413, -232, -645, -794, -799, 584, 921, 116, -116, 321, -208, 254, -267, -651, 866, -294, 713, 348, 276, 67, 577, -690, 490, -997, -156, -344, -967, -414, -
        164, -108, 977, 915, -19, -32, -723, -621, -9, -924, 895, -476, -959, 828, 864, -524, -691, -688, 747, -8, -471, 188, 763, 326, -1, 819, -670, 231, -606, -946, 616, -234, 237, -950, -382, -286, -975, 853, 35, -487, -679, 353, -714, 495, 538, 647, -473, -713, 241, 157, -840, -4, 904, 133, 985, -952, -837, -209, 935, 413, -232, -645, -794, -799, 584, 921, 116, -116, 321, -208, 254, -267, -651, 866, -294, 713, 348, 276, 67, 577, -690, 490, -997, -156, -344, -967, -414, -164, 295]


xor = 0
for num in nums:
    xor ^= num
    print(xor)

print(xor)