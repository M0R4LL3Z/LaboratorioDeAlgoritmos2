from movies import my_list

def viewer_or_administrator(my_list_movies,my_movies,list):
   while True:
      print('1 - Acessar como espectador ')
      print('2 - Acessar como administrador')
      opc = input(':')

      if opc == '1':
         for index, movie in enumerate(my_movies):
            print(f"{movie['name']}, {movie['year']}, {movie['age_group']} anos")
         break

      else:
         access(my_list_movies,list)
         break



def access(my_list_movies,list):
   userName = input('Usuário:')
   passWord = input('Senha:')

   if my_list_movies['username'] == userName and my_list_movies['password'] == passWord:
      menu(my_list_movies,list)
   else:
      print('Usuário ou senha inválido!')

def menu(my_list_movies,list):
   while True:
      print('----- 2000 MOVIE RENTAL -----')
      print('1 - Listar filmes')
      print('2 - Alugar filme')
      print('3 - Devolver filme')
      print('4 - Ver filmes alugados')
      print('5 - Sair')
      opc = input(':')


      if opc == '1':
         list_movie(my_list_movies['movies'])

      if opc == '2':
         rent_movie(my_list_movies['movies'],list)

      if opc == '3':
         devolution(my_list_movies['movies'],list)

      if opc == '4':
         rented_movies(my_list_movies['movies'])

      if opc == '5':
         print('Sistema Encerrado')
         break
         


   return my_list_movies


def list_movie(my_list_movies):
   
   for index, movie in enumerate(my_list_movies):
      print(f"[{index + 1}] {movie['name']}, {movie['year']},{movie['amount']}, {movie['age_group']} anos")



def rent_movie(my_list_movies,list):
   name = input('Nome:')
   age = int(input('Idade:'))
   name_Movie = input('Nome do filme:')

   for index, movie in enumerate(my_list_movies):
      if name_Movie == movie["name"]:
         if age >= movie['age_group']:
            list.append(name)
            if list.count(name) > 3:
               check_rent()
               return

            else:
               print('Filme alugado')
               movie["located"].append({
                              "name": name,
                              "amount": 1
                              })
               movie["amount"] -= 1
               print(list)
               return

         else:
            print('Você não tem idade para alugar esse filme')



   return my_list_movies,list

def check_rent():
   print('Desculpe você só pode alugar 3 filmes')
   return

def devolution(my_list_movies,list):
   name = input('Nome:')
   name_Movie = input('Nome do filme:')

   for index, movie in enumerate(my_list_movies):
      if name_Movie == movie["name"]:
         for index,itens in enumerate(movie["located"]):
            if len(itens) == 0:
               print('Locação vazia')
               return
            else:
               if name == itens['name']:
                  print(itens['name'])
                  del itens['name']
                  del itens['amount']
                  movie['amount'] += 1
                  print('Filme devolvido')
                  for i in list:
                     if i == name:
                        list.remove(i)
                     return
            if name != itens['name']:
               print('Nome não encontrado')
               return

      if name_Movie != movie["name"]:
         print('Filme não encontrado')
         return

   return my_list_movies,list

def rented_movies(my_list_movies):
   for index, movie in enumerate(my_list_movies):
      for index, itens in enumerate(movie["located"]):
         if len(itens) != 0:
            print(f'{movie["name"]},{itens["name"]}')
         else:
            print('Nenhum filme alugado')
            return

def main():
   list = []
   my_list_movies = my_list.copy()
   my_movies = my_list_movies['movies']
   viewer_or_administrator(my_list_movies,my_movies,list)


main()