import numpy as np

# # reshape : 배열을 차원의 형태로 만들어줌
# print(type(a))

# a = np.arange(15).reshape(3,5)
# print(a)

# b = np.array([2, 3, 4])
# print(b.dtype)

# c = np.arange(15).reshape(3,1,5)
# print(c)


# # .shape : 행렬의 차원을 확인함
# print(a.shape)

# # # ndim : 행렬의 축의 수
# # print(a.ndim)

# n_arr = np.array(range(1, 11), dtype='int64')

# # n_arr.size
# print(n_arr.size)
# data_size =n_arr.size * n_arr.itemsize
# print(data_size)
# print(n_arr.itemsize)
# print(n_arr)

# p_num = np.random.rand(6)
# print(p_num)


# # 사용자로부터 2이상의 수 n을 입력으로 받아서, 입력된 수를 바탕으로 다음과 같은 nxn 크기의 다차원 배열 a를 생성하는 프로그램을 작성하시오.
# # 이 때 배열의 내용은 0과 1의 값이 체크 판 패턴으로 교차하여 나타나도록 하여라.

# np.ones : 1로 채워진 배열
# np.zeros : 0로 채워진 배열

n = int(input("2이상의 수 : "))
a = np.zeros((n, n), dtype = 'int64')

for i in range(n):
    for j in range(n):
        if (i+j)%2 == 0:
            a[i,j] = 1

print(a)