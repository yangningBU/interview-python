def squares_and_cubes():
    return ( 
      [i ** 2 for i in range(1, 11) if i % 2 == 0] + \
      [i ** 3 for i in range(1, 11) if i % 2 == 1]
    )

print(squares_and_cubes())