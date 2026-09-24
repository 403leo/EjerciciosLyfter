first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]
final_list = []
counter_list = 0

for i in range(len(first_list)):
    final_list.append(first_list[i] + " " + second_list[i])
    counter_list += 1
    


for value in final_list:
    print(f"{value}")