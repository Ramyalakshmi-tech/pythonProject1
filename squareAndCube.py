new_list=[i for i in range(1,10)]

square=list(map(lambda a:(a*a),new_list))
cube=list(map(lambda a:(a*a*a),new_list))
print(square)
print(cube)