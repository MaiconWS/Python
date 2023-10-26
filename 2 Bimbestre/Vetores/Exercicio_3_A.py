series_favoritas = ['Breaking Bad', 'Stranger Things','The Wintcher','Game of Thrones','Westworld']

series_favorita = series_favoritas.pop(2)
series_favoritas.insert(0, series_favorita)

series_favoritas.pop()

print("Minhas séries atualizadas: ",series_favoritas)