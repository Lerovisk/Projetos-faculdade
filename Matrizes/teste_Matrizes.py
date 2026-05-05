nums = [1, 2, 3]
print(nums)

nums.append(10) # adiciona o elemento 10 ao final da lista
print(nums)


num2 = [2, 7] # extend nums com os elementos de nums2
print(num2)
nums.extend(num2) # coloca os elementos de num2 em nums
print(nums)


nums.insert(2, 4) # insere o elemento 4 na posição 2 da lista
print(nums)


nums.remove(3) # remove o elemento 3 da lista
print(nums)


print(nums.pop(0)) # remove e retorna o elemento na posição 0 da lista
print(nums)

# cria uma cópia da nums em numsCpy
numsCpy = nums.copy()
print(numsCpy)

# remove todos os elementos de nums
nums.clear()
print(nums)

# conta quantos elementos 2 existem na lista
nums = numsCpy.copy()
print(nums.count(2))

# ordena nums em ordem crescendente
nums.sort()
print(nums)

# inverte os elementos de nums
nums.reverse()
print(nums)

herois = ["Lana", "Capitão América", "Hulk", "Super-Homem", "Zendaya"]

print(max(herois))