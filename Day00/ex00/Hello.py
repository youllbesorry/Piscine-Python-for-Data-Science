ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list.pop(1)
ft_list.append("World!")

tmp_tuple = list(ft_tuple)
tmp_tuple.pop(1)
tmp_tuple.append("France!")
ft_tuple = tuple(tmp_tuple)

ft_set.remove("tutu!")
ft_set.add("Lyon!")

ft_dict.update({"Hello" : "42 Lyon Auvergne-Rhône-Alpes!"})

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)