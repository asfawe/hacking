import matplotlib.pyplot as plt

Magma256 =[
        [0x00, 0x00, 0x03],
        [0x00, 0x00, 0x04],
        [0x00, 0x00, 0x06],
        [0x01, 0x00, 0x07],
        [0x01, 0x01, 0x09],
        [0x01, 0x01, 0x0B],
        [0x02, 0x02, 0x0D],
        [0x02, 0x02, 0x0F],
        [0x03, 0x03, 0x11],
        [0x04, 0x03, 0x13],
        [0x04, 0x04, 0x15],
        [0x05, 0x04, 0x17],
        [0x06, 0x05, 0x19],
        [0x07, 0x05, 0x1B],
        [0x08, 0x06, 0x1D],
        [0x09, 0x07, 0x1F],
        [0x0A, 0x07, 0x22],
        [0x0B, 0x08, 0x24],
        [0x0C, 0x09, 0x26],
        [0x0D, 0x0A, 0x28],
        [0x0E, 0x0A, 0x2A],
        [0x0F, 0x0B, 0x2C],
        [0x10, 0x0C, 0x2F],
        [0x11, 0x0C, 0x31],
        [0x12, 0x0D, 0x33],
        [0x14, 0x0D, 0x35],
        [0x15, 0x0E, 0x38],
        [0x16, 0x0E, 0x3A],
        [0x17, 0x0F, 0x3C],
        [0x18, 0x0F, 0x3F],
        [0x1A, 0x10, 0x41],
        [0x1B, 0x10, 0x44],
        [0x1C, 0x10, 0x46],
        [0x1E, 0x10, 0x49],
        [0x1F, 0x11, 0x4B],
        [0x20, 0x11, 0x4D],
        [0x22, 0x11, 0x50],
        [0x23, 0x11, 0x52],
        [0x25, 0x11, 0x55],
        [0x26, 0x11, 0x57],
        [0x28, 0x11, 0x59],
        [0x2A, 0x11, 0x5C],
        [0x2B, 0x11, 0x5E],
        [0x2D, 0x10, 0x60],
        [0x2F, 0x10, 0x62],
        [0x30, 0x10, 0x65],
        [0x32, 0x10, 0x67],
        [0x34, 0x10, 0x68],
        [0x35, 0x0F, 0x6A],
        [0x37, 0x0F, 0x6C],
        [0x39, 0x0F, 0x6E],
        [0x3B, 0x0F, 0x6F],
        [0x3C, 0x0F, 0x71],
        [0x3E, 0x0F, 0x72],
        [0x40, 0x0F, 0x73],
        [0x42, 0x0F, 0x74],
        [0x43, 0x0F, 0x75],
        [0x45, 0x0F, 0x76],
        [0x47, 0x0F, 0x77],
        [0x48, 0x10, 0x78],
        [0x4A, 0x10, 0x79],
        [0x4B, 0x10, 0x79],
        [0x4D, 0x11, 0x7A],
        [0x4F, 0x11, 0x7B],
        [0x50, 0x12, 0x7B],
        [0x52, 0x12, 0x7C],
        [0x53, 0x13, 0x7C],
        [0x55, 0x13, 0x7D],
        [0x57, 0x14, 0x7D],
        [0x58, 0x15, 0x7E],
        [0x5A, 0x15, 0x7E],
        [0x5B, 0x16, 0x7E],
        [0x5D, 0x17, 0x7E],
        [0x5E, 0x17, 0x7F],
        [0x60, 0x18, 0x7F],
        [0x61, 0x18, 0x7F],
        [0x63, 0x19, 0x7F],
        [0x65, 0x1A, 0x80],
        [0x66, 0x1A, 0x80],
        [0x68, 0x1B, 0x80],
        [0x69, 0x1C, 0x80],
        [0x6B, 0x1C, 0x80],
        [0x6C, 0x1D, 0x80],
        [0x6E, 0x1E, 0x81],
        [0x6F, 0x1E, 0x81],
        [0x71, 0x1F, 0x81],
        [0x73, 0x1F, 0x81],
        [0x74, 0x20, 0x81],
        [0x76, 0x21, 0x81],
        [0x77, 0x21, 0x81],
        [0x79, 0x22, 0x81],
        [0x7A, 0x22, 0x81],
        [0x7C, 0x23, 0x81],
        [0x7E, 0x24, 0x81],
        [0x7F, 0x24, 0x81],
        [0x81, 0x25, 0x81],
        [0x82, 0x25, 0x81],
        [0x84, 0x26, 0x81],
        [0x85, 0x26, 0x81],
        [0x87, 0x27, 0x81],
        [0x89, 0x28, 0x81],
        [0x8A, 0x28, 0x81],
        [0x8C, 0x29, 0x80],
        [0x8D, 0x29, 0x80],
        [0x8F, 0x2A, 0x80],
        [0x91, 0x2A, 0x80],
        [0x92, 0x2B, 0x80],
        [0x94, 0x2B, 0x80],
        [0x95, 0x2C, 0x80],
        [0x97, 0x2C, 0x7F],
        [0x99, 0x2D, 0x7F],
        [0x9A, 0x2D, 0x7F],
        [0x9C, 0x2E, 0x7F],
        [0x9E, 0x2E, 0x7E],
        [0x9F, 0x2F, 0x7E],
        [0xA1, 0x2F, 0x7E],
        [0xA3, 0x30, 0x7E],
        [0xA4, 0x30, 0x7D],
        [0xA6, 0x31, 0x7D],
        [0xA7, 0x31, 0x7D],
        [0xA9, 0x32, 0x7C],
        [0xAB, 0x33, 0x7C],
        [0xAC, 0x33, 0x7B],
        [0xAE, 0x34, 0x7B],
        [0xB0, 0x34, 0x7B],
        [0xB1, 0x35, 0x7A],
        [0xB3, 0x35, 0x7A],
        [0xB5, 0x36, 0x79],
        [0xB6, 0x36, 0x79],
        [0xB8, 0x37, 0x78],
        [0xB9, 0x37, 0x78],
        [0xBB, 0x38, 0x77],
        [0xBD, 0x39, 0x77],
        [0xBE, 0x39, 0x76],
        [0xC0, 0x3A, 0x75],
        [0xC2, 0x3A, 0x75],
        [0xC3, 0x3B, 0x74],
        [0xC5, 0x3C, 0x74],
        [0xC6, 0x3C, 0x73],
        [0xC8, 0x3D, 0x72],
        [0xCA, 0x3E, 0x72],
        [0xCB, 0x3E, 0x71],
        [0xCD, 0x3F, 0x70],
        [0xCE, 0x40, 0x70],
        [0xD0, 0x41, 0x6F],
        [0xD1, 0x42, 0x6E],
        [0xD3, 0x42, 0x6D],
        [0xD4, 0x43, 0x6D],
        [0xD6, 0x44, 0x6C],
        [0xD7, 0x45, 0x6B],
        [0xD9, 0x46, 0x6A],
        [0xDA, 0x47, 0x69],
        [0xDC, 0x48, 0x69],
        [0xDD, 0x49, 0x68],
        [0xDE, 0x4A, 0x67],
        [0xE0, 0x4B, 0x66],
        [0xE1, 0x4C, 0x66],
        [0xE2, 0x4D, 0x65],
        [0xE4, 0x4E, 0x64],
        [0xE5, 0x50, 0x63],
        [0xE6, 0x51, 0x62],
        [0xE7, 0x52, 0x62],
        [0xE8, 0x54, 0x61],
        [0xEA, 0x55, 0x60],
        [0xEB, 0x56, 0x60],
        [0xEC, 0x58, 0x5F],
        [0xED, 0x59, 0x5F],
        [0xEE, 0x5B, 0x5E],
        [0xEE, 0x5D, 0x5D],
        [0xEF, 0x5E, 0x5D],
        [0xF0, 0x60, 0x5D],
        [0xF1, 0x61, 0x5C],
        [0xF2, 0x63, 0x5C],
        [0xF3, 0x65, 0x5C],
        [0xF3, 0x67, 0x5B],
        [0xF4, 0x68, 0x5B],
        [0xF5, 0x6A, 0x5B],
        [0xF5, 0x6C, 0x5B],
        [0xF6, 0x6E, 0x5B],
        [0xF6, 0x70, 0x5B],
        [0xF7, 0x71, 0x5B],
        [0xF7, 0x73, 0x5C],
        [0xF8, 0x75, 0x5C],
        [0xF8, 0x77, 0x5C],
        [0xF9, 0x79, 0x5C],
        [0xF9, 0x7B, 0x5D],
        [0xF9, 0x7D, 0x5D],
        [0xFA, 0x7F, 0x5E],
        [0xFA, 0x80, 0x5E],
        [0xFA, 0x82, 0x5F],
        [0xFB, 0x84, 0x60],
        [0xFB, 0x86, 0x60],
        [0xFB, 0x88, 0x61],
        [0xFB, 0x8A, 0x62],
        [0xFC, 0x8C, 0x63],
        [0xFC, 0x8E, 0x63],
        [0xFC, 0x90, 0x64],
        [0xFC, 0x92, 0x65],
        [0xFC, 0x93, 0x66],
        [0xFD, 0x95, 0x67],
        [0xFD, 0x97, 0x68],
        [0xFD, 0x99, 0x69],
        [0xFD, 0x9B, 0x6A],
        [0xFD, 0x9D, 0x6B],
        [0xFD, 0x9F, 0x6C],
        [0xFD, 0xA1, 0x6E],
        [0xFD, 0xA2, 0x6F],
        [0xFD, 0xA4, 0x70],
        [0xFE, 0xA6, 0x71],
        [0xFE, 0xA8, 0x73],
        [0xFE, 0xAA, 0x74],
        [0xFE, 0xAC, 0x75],
        [0xFE, 0xAE, 0x76],
        [0xFE, 0xAF, 0x78],
        [0xFE, 0xB1, 0x79],
        [0xFE, 0xB3, 0x7B],
        [0xFE, 0xB5, 0x7C],
        [0xFE, 0xB7, 0x7D],
        [0xFE, 0xB9, 0x7F],
        [0xFE, 0xBB, 0x80],
        [0xFE, 0xBC, 0x82],
        [0xFE, 0xBE, 0x83],
        [0xFE, 0xC0, 0x85],
        [0xFE, 0xC2, 0x86],
        [0xFE, 0xC4, 0x88],
        [0xFE, 0xC6, 0x89],
        [0xFE, 0xC7, 0x8B],
        [0xFE, 0xC9, 0x8D],
        [0xFE, 0xCB, 0x8E],
        [0xFD, 0xCD, 0x90],
        [0xFD, 0xCF, 0x92],
        [0xFD, 0xD1, 0x93],
        [0xFD, 0xD2, 0x95],
        [0xFD, 0xD4, 0x97],
        [0xFD, 0xD6, 0x98],
        [0xFD, 0xD8, 0x9A],
        [0xFD, 0xDA, 0x9C],
        [0xFD, 0xDC, 0x9D],
        [0xFD, 0xDD, 0x9F],
        [0xFD, 0xDF, 0xA1],
        [0xFD, 0xE1, 0xA3],
        [0xFC, 0xE3, 0xA5],
        [0xFC, 0xE5, 0xA6],
        [0xFC, 0xE6, 0xA8],
        [0xFC, 0xE8, 0xAA],
        [0xFC, 0xEA, 0xAC],
        [0xFC, 0xEC, 0xAE],
        [0xFC, 0xEE, 0xB0],
        [0xFC, 0xF0, 0xB1],
        [0xFC, 0xF1, 0xB3],
        [0xFC, 0xF3, 0xB5],
        [0xFC, 0xF5, 0xB7],
        [0xFB, 0xF7, 0xB9],
        [0xFB, 0xF9, 0xBB],
        [0xFB, 0xFA, 0xBD],
        [0xFB, 0xFC, 0xBF],
]

# 데이터를 정규화합니다.
colors = [[x/255 for x in triplet] for triplet in Magma256]

# 색상 바를 그립니다.
fig, ax = plt.subplots(1, 1, figsize=(6, 2), subplot_kw=dict(xticks=[], yticks=[], frame_on=False))

for sp in ax.spines.values():
    sp.set_visible(False)

plt.imshow([colors], aspect='equal')
plt.show()
