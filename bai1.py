product_info = ("SP001", "Áo polo nam", "Size L", 299000)

print("Mã sản phẩm:", product_info[0])
print("Tên sản phẩm:", product_info[1])
print("Số lượng thông tin sản phẩm:", len(product_info))

temp = list(product_info)
temp[3] = 279000
product_info = tuple(temp)

print("Thông tin sản phẩm sau cập nhật:", product_info)
